#!/usr/bin/env python3
"""Interface Tkinter pour choisir et publier les ressources du site MkDocs."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import tkinter as tk
import ast
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from tkinter import messagebox, scrolledtext, simpledialog, ttk


# Permet aussi bien « python scripts/publier_ressources_gui.py » qu'un import
# du module depuis la racine du projet.
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import publier_ressources_site as publisher


PUBLIC_SITE_URL = (
    f"https://vnicolle56610.github.io/{publisher.PROJECT_ROOT.name}/"
)


def find_mkdocs_executable() -> str | None:
    """Trouver MkDocs dans le projet avant de consulter le PATH."""
    candidates = (
        publisher.PROJECT_ROOT / ".venv" / "bin" / "mkdocs",
        publisher.PROJECT_ROOT / "venv" / "bin" / "mkdocs",
        publisher.PROJECT_ROOT / ".venv" / "Scripts" / "mkdocs.exe",
        publisher.PROJECT_ROOT / "venv" / "Scripts" / "mkdocs.exe",
    )
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)
    return shutil.which("mkdocs")


def relative_path(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def resource_description(resource: publisher.Resource) -> str:
    source = relative_path(resource.source, publisher.SOURCE_ROOT)
    label = publisher.LABELS[resource.kind]
    return f"{resource.notion} — {label} : {source}"


def path_description(path: Path) -> str:
    return relative_path(path, publisher.PROJECT_ROOT)


@dataclass(frozen=True)
class DeployPreflightResult:
    ok: bool
    user_message: str
    details: str


@dataclass(frozen=True)
class PreparedPublication:
    worktree: Path
    base_sha: str
    staged_paths: tuple[str, ...]


@dataclass(frozen=True)
class DeploymentResult:
    source_sha: str
    command_output: str
    post_deploy_details: str
    cleanup_warnings: tuple[str, ...]


def run_git(project_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=project_root,
        text=True,
        capture_output=True,
        check=False,
    )


def git_output(completed: subprocess.CompletedProcess[str]) -> str:
    return "\n".join(
        part.strip()
        for part in (completed.stdout, completed.stderr)
        if part.strip()
    )


def format_command_output(completed: subprocess.CompletedProcess[str]) -> str:
    return git_output(completed)


def classify_git_status(porcelain: str) -> str:
    statuses = porcelain.splitlines()
    if any(line.startswith("??") for line in statuses):
        return "fichiers non suivis"
    if any("D" in line[:2] for line in statuses):
        return "fichiers supprimés localement"
    return "fichiers locaux non enregistrés dans Git"


def decode_git_path(path: str) -> str:
    if len(path) >= 2 and path.startswith('"') and path.endswith('"'):
        try:
            decoded = ast.literal_eval(path)
        except (SyntaxError, ValueError):
            return path
        if isinstance(decoded, str):
            return decoded
    return path


def parse_git_status_porcelain_line(line: str) -> tuple[str, str]:
    if len(line) < 3:
        raise ValueError(f"Sortie git status --porcelain invalide : {line!r}")
    if len(line) >= 4 and line[2] == " ":
        return line[:2], decode_git_path(line[3:])
    if line[1] == " ":
        return f"{line[0]} ", decode_git_path(line[2:])
    raise ValueError(f"Sortie git status --porcelain invalide : {line!r}")


def parse_git_name_status_line(line: str) -> tuple[str, str]:
    status, separator, path = line.partition("\t")
    if not separator or not status or not path:
        raise ValueError(f"Sortie git diff --name-status invalide : {line!r}")
    return status, decode_git_path(path)


def classify_staging_status(
    porcelain: str,
) -> tuple[list[str], list[str], list[str], list[str]]:
    added: list[str] = []
    modified: list[str] = []
    deleted: list[str] = []
    untracked: list[str] = []

    for line in porcelain.splitlines():
        if not line:
            continue
        status, path = parse_git_status_porcelain_line(line)
        if status == "??":
            untracked.append(path)
            continue
        if "D" in status:
            deleted.append(path)
        elif "A" in status:
            added.append(path)
        elif status.strip():
            modified.append(path)

    return added, modified, deleted, untracked


def paths_to_stage(
    added: list[str],
    modified: list[str],
    untracked: list[str],
) -> list[str]:
    return sorted({*added, *modified, *untracked}, key=str.casefold)


def publication_report_paths(
    report: publisher.PublicationReport,
    project_root: Path,
) -> set[str]:
    paths: set[str] = set()
    for path in (*report.copied_files, *report.modified_pages):
        paths.add(relative_path(path, project_root))
    return paths


def existing_status_paths(
    worktree: Path,
    added: list[str],
    modified: list[str],
    untracked: list[str],
) -> set[str]:
    existing: set[str] = set()
    missing: list[str] = []
    for path in paths_to_stage(added, modified, untracked):
        if (worktree / path).exists():
            existing.add(path)
        else:
            missing.append(path)
    if missing:
        raise RuntimeError(
            "Préparation bloquée : Git signale des fichiers à stageer "
            "qui n'existent pas dans le worktree.\n\n"
            + "\n".join(f"- {path}" for path in missing)
        )
    return existing


def validate_preview_paths_exist(
    worktree: Path,
    preview_paths: set[str],
) -> None:
    missing = sorted(
        path for path in preview_paths if not (worktree / path).exists()
    )
    if missing:
        raise RuntimeError(
            "Préparation bloquée : le preview annonce des fichiers modifiés "
            "ou ajoutés absents du worktree.\n\n"
            + "\n".join(f"- {path}" for path in missing)
        )


def stageable_paths_from_status(
    worktree: Path,
    report: publisher.PublicationReport,
    added: list[str],
    modified: list[str],
    untracked: list[str],
) -> tuple[str, ...]:
    preview_paths = publication_report_paths(report, worktree)
    validate_preview_paths_exist(worktree, preview_paths)

    real_paths = existing_status_paths(worktree, added, modified, untracked)
    unexpected = sorted(real_paths - preview_paths, key=str.casefold)
    if unexpected:
        raise RuntimeError(
            "Préparation bloquée : l'état Git contient des changements "
            "qui ne figurent pas dans le preview.\n\n"
            + "\n".join(f"- {path}" for path in unexpected)
        )
    return tuple(sorted(real_paths & preview_paths, key=str.casefold))


def ensure_no_staged_deletion(worktree: Path) -> tuple[bool, str]:
    completed = run_git(worktree, "diff", "--cached", "--name-status")
    output = git_output(completed)
    if completed.returncode != 0:
        return False, output
    deleted = []
    try:
        for line in output.splitlines():
            if not line:
                continue
            status, path = parse_git_name_status_line(line)
            if status.startswith(("D", "R")):
                deleted.append(f"{status}\t{path}")
    except ValueError as error:
        return False, str(error)
    if deleted:
        return False, "\n".join(deleted)
    return True, output


def deployed_site_path(staged_path: str) -> str | None:
    if not staged_path.startswith("docs/"):
        return None
    docs_path = Path(staged_path.removeprefix("docs/"))
    if docs_path.suffix.casefold() != ".md":
        return docs_path.as_posix()
    if docs_path.name == "index.md":
        return docs_path.with_suffix(".html").as_posix()
    return (docs_path.parent / docs_path.stem / "index.html").as_posix()


def deployed_site_paths(staged_paths: tuple[str, ...]) -> tuple[str, ...]:
    paths = {
        output_path
        for staged_path in staged_paths
        if (output_path := deployed_site_path(staged_path)) is not None
    }
    return tuple(sorted(paths, key=str.casefold))


def check_deploy_preflight(project_root: Path) -> DeployPreflightResult:
    technical_details: list[str] = []

    inside = run_git(project_root, "rev-parse", "--is-inside-work-tree")
    technical_details.append(f"$ git rev-parse --is-inside-work-tree\n{git_output(inside)}")
    if inside.returncode != 0 or inside.stdout.strip() != "true":
        return DeployPreflightResult(
            False,
            "Déploiement bloqué : ce dossier n'est pas un dépôt Git.",
            "\n\n".join(technical_details),
        )

    branch = run_git(project_root, "branch", "--show-current")
    technical_details.append(f"$ git branch --show-current\n{git_output(branch)}")
    if branch.returncode != 0 or branch.stdout.strip() != "main":
        current = branch.stdout.strip() or "branche détachée ou inconnue"
        return DeployPreflightResult(
            False,
            f"Déploiement bloqué : la branche courante est « {current} », pas « main ».",
            "\n\n".join(technical_details),
        )

    status = run_git(project_root, "status", "--porcelain")
    technical_details.append(f"$ git status --porcelain\n{git_output(status)}")
    if status.returncode != 0:
        return DeployPreflightResult(
            False,
            "Déploiement bloqué : impossible de vérifier l'état Git local.",
            "\n\n".join(technical_details),
        )
    if status.stdout.strip():
        reason = classify_git_status(status.stdout)
        return DeployPreflightResult(
            False,
            (
                "Déploiement bloqué : les fichiers locaux ne correspondent pas "
                f"à la version enregistrée sur GitHub ({reason})."
            ),
            "\n\n".join(technical_details),
        )

    origin = run_git(project_root, "remote", "get-url", "origin")
    technical_details.append(f"$ git remote get-url origin\n{git_output(origin)}")
    if origin.returncode != 0:
        return DeployPreflightResult(
            False,
            "Déploiement bloqué : le remote Git « origin » est introuvable.",
            "\n\n".join(technical_details),
        )

    fetch = run_git(project_root, "fetch", "origin")
    technical_details.append(f"$ git fetch origin\n{git_output(fetch)}")
    if fetch.returncode != 0:
        return DeployPreflightResult(
            False,
            "Déploiement bloqué : impossible d'actualiser origin/main.",
            "\n\n".join(technical_details),
        )

    head = run_git(project_root, "rev-parse", "HEAD")
    technical_details.append(f"$ git rev-parse HEAD\n{git_output(head)}")
    origin_main = run_git(project_root, "rev-parse", "--verify", "origin/main")
    technical_details.append(f"$ git rev-parse --verify origin/main\n{git_output(origin_main)}")
    if head.returncode != 0 or origin_main.returncode != 0:
        return DeployPreflightResult(
            False,
            "Déploiement bloqué : origin/main est inaccessible.",
            "\n\n".join(technical_details),
        )

    if head.stdout.strip() != origin_main.stdout.strip():
        return DeployPreflightResult(
            False,
            (
                "Déploiement bloqué : le commit local main ne correspond pas "
                "exactement à origin/main."
            ),
            "\n\n".join(technical_details),
        )

    return DeployPreflightResult(
        True,
        "Pré-vol Git validé : main est propre et synchronisé avec origin/main.",
        "\n\n".join(technical_details),
    )


def add_section(lines: list[str], title: str, items: list[str]) -> None:
    lines.append(f"{title} : {len(items)}")
    if items:
        lines.extend(f"  - {item}" for item in items)
    else:
        lines.append("  (aucun)")
    lines.append("")


def add_staging_section(lines: list[str], title: str, items: list[str]) -> None:
    lines.append(title)
    lines.append("-" * len(title))
    if items:
        lines.extend(f"- {item}" for item in items)
    else:
        lines.append("(aucun)")
    lines.append("")


def format_report(report: publisher.PublicationReport) -> str:
    """Produire un bilan adapté à la zone de texte de l'interface."""
    if report.dry_run:
        heading = "PRÉVISUALISATION — aucune écriture effectuée"
        copied_title = "Fichiers qui seraient copiés"
        pages_title = "Pages Markdown qui seraient modifiées"
    else:
        heading = "BILAN DE LA PUBLICATION"
        copied_title = "Fichiers copiés"
        pages_title = "Pages Markdown modifiées"

    lines = [
        heading,
        "=" * len(heading),
        "",
        f"PDF trouvés : {report.pdf_count}",
        f"PDF reconnus : {len(report.resources)}",
        f"PDF non reconnus : {report.ignored_pdf_count}",
        "",
    ]

    add_section(
        lines,
        "Fichiers sélectionnés",
        [
            resource_description(resource)
            for resource in report.selected_resources
        ],
    )
    add_section(
        lines,
        copied_title,
        [path_description(path) for path in report.copied_files],
    )
    add_section(
        lines,
        "Fichiers sélectionnés déjà à jour",
        [path_description(path) for path in report.unchanged_files],
    )
    add_section(
        lines,
        pages_title,
        [path_description(path) for path in report.modified_pages],
    )
    add_section(
        lines,
        "Pages Markdown déjà à jour",
        [path_description(path) for path in report.unchanged_pages],
    )
    add_section(
        lines,
        "Fichiers ignorés car non sélectionnés",
        [
            resource_description(resource)
            for resource in report.ignored_resources
        ],
    )
    add_section(
        lines,
        "Fichiers déjà présents dans docs/ mais non sélectionnés",
        [
            path_description(path)
            for path in report.present_unselected_files
        ],
    )
    add_section(
        lines,
        "Pages Markdown introuvables",
        list(report.missing_pages),
    )
    add_section(lines, "Avertissements", list(report.warnings))

    lines.append(
        "Aucun fichier PDF déjà présent dans docs/ n'est supprimé "
        "automatiquement."
    )
    return "\n".join(lines)


class PublicationApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.resources: list[publisher.Resource] = []
        self.pdf_count = 0
        self.ignored_pdf_count = 0
        self.variables: dict[publisher.Resource, tk.BooleanVar] = {}
        self.mkdocs_process: subprocess.Popen[bytes] | None = None
        self.prepared_worktree: Path | None = None
        self.prepared_publication: PreparedPublication | None = None
        self.pushed_source_sha: str | None = None

        self.status = tk.StringVar(value="Analyse des ressources…")
        self._build_interface()
        self.root.protocol("WM_DELETE_WINDOW", self.quit)
        self.root.after(0, self.scan_resources)

    def _build_interface(self) -> None:
        self.root.title(f"Publication des ressources — Maths {publisher.NIVEAU}")
        self.root.geometry("980x820")
        self.root.minsize(780, 620)

        main = ttk.Frame(self.root, padding=12)
        main.grid(row=0, column=0, sticky="nsew")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        main.columnconfigure(0, weight=1)
        main.rowconfigure(2, weight=3)
        main.rowconfigure(7, weight=2)

        ttk.Label(
            main,
            text="Choisir les documents à publier",
            font=("TkDefaultFont", 16, "bold"),
        ).grid(row=0, column=0, sticky="w")

        ttk.Label(
            main,
            text=f"Source : {publisher.SOURCE_ROOT}",
        ).grid(row=1, column=0, sticky="w", pady=(2, 8))

        documents_box = ttk.LabelFrame(main, text="Documents disponibles")
        documents_box.grid(row=2, column=0, sticky="nsew")
        documents_box.rowconfigure(0, weight=1)
        documents_box.columnconfigure(0, weight=1)

        self.canvas = tk.Canvas(
            documents_box,
            borderwidth=0,
            highlightthickness=0,
        )
        scrollbar = ttk.Scrollbar(
            documents_box,
            orient="vertical",
            command=self.canvas.yview,
        )
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.documents_frame = ttk.Frame(self.canvas, padding=8)
        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.documents_frame,
            anchor="nw",
        )
        self.documents_frame.bind(
            "<Configure>",
            lambda _event: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            ),
        )
        self.canvas.bind(
            "<Configure>",
            lambda event: self.canvas.itemconfigure(
                self.canvas_window,
                width=event.width,
            ),
        )

        selection_buttons = ttk.Frame(main)
        selection_buttons.grid(row=3, column=0, sticky="ew", pady=(8, 4))
        self.safe_button = ttk.Button(
            selection_buttons,
            text="Sélection sûre",
            command=self.select_safe,
        )
        self.safe_button.pack(side="left", padx=(0, 6))
        self.clear_button = ttk.Button(
            selection_buttons,
            text="Tout décocher",
            command=self.clear_all,
        )
        self.clear_button.pack(side="left", padx=6)
        self.all_button = ttk.Button(
            selection_buttons,
            text="Tout cocher",
            command=self.select_all,
        )
        self.all_button.pack(side="left", padx=6)

        action_buttons = ttk.Frame(main)
        action_buttons.grid(row=4, column=0, sticky="ew", pady=(4, 8))
        self.preview_button = ttk.Button(
            action_buttons,
            text="Prévisualiser",
            command=self.preview,
        )
        self.preview_button.pack(side="left", padx=(0, 6))
        self.publish_button = ttk.Button(
            action_buttons,
            text="Publier la sélection",
            command=self.publish,
        )
        self.publish_button.pack(side="left", padx=6)
        self.prepare_online_button = ttk.Button(
            action_buttons,
            text="Préparer la mise en ligne",
            command=self.prepare_online_publication,
            state="disabled",
        )
        self.prepare_online_button.pack(side="left", padx=6)
        self.commit_push_button = ttk.Button(
            action_buttons,
            text="Commit + push la source",
            command=self.commit_and_push_prepared_publication,
            state="disabled",
        )
        self.commit_push_button.pack(side="left", padx=6)
        self.deploy_button = ttk.Button(
            action_buttons,
            text="Déployer sur GitHub Pages",
            command=self.deploy_github_pages,
            state="disabled",
        )
        self.deploy_button.pack(side="left", padx=6)
        self.serve_button = ttk.Button(
            action_buttons,
            text="Aperçu local (mkdocs serve)",
            command=self.launch_mkdocs,
        )
        self.serve_button.pack(side="left", padx=6)
        ttk.Button(
            action_buttons,
            text="Quitter",
            command=self.quit,
        ).pack(side="right")

        ttk.Label(
            main,
            text=(
                "Publier la sélection met à jour les fichiers locaux ; "
                "l’aperçu local reste sur cet ordinateur ; déployer sur "
                "GitHub Pages met le site en ligne."
            ),
            wraplength=920,
        ).grid(row=5, column=0, sticky="w", pady=(0, 8))

        ttk.Label(
            main,
            text="Prévisualisation et bilan",
            font=("TkDefaultFont", 11, "bold"),
        ).grid(row=6, column=0, sticky="w")

        self.output = scrolledtext.ScrolledText(
            main,
            height=14,
            wrap="word",
            font=("TkFixedFont", 10),
            state="disabled",
        )
        self.output.grid(row=7, column=0, sticky="nsew", pady=(4, 8))

        ttk.Separator(main).grid(row=8, column=0, sticky="ew")
        ttk.Label(main, textvariable=self.status).grid(
            row=9,
            column=0,
            sticky="w",
            pady=(6, 0),
        )

        self.resource_buttons = (
            self.safe_button,
            self.clear_button,
            self.all_button,
            self.preview_button,
            self.publish_button,
        )
        self._set_resource_buttons_state("disabled")

    def _set_resource_buttons_state(self, state: str) -> None:
        for button in self.resource_buttons:
            button.configure(state=state)

    def _set_output(self, text: str) -> None:
        self.output.configure(state="normal")
        self.output.delete("1.0", tk.END)
        self.output.insert("1.0", text)
        self.output.configure(state="disabled")
        self.output.see("1.0")

    def _append_output(self, text: str) -> None:
        self.output.configure(state="normal")
        self.output.insert(tk.END, f"\n\n{text}")
        self.output.configure(state="disabled")
        self.output.see(tk.END)

    def _set_busy(self, busy: bool) -> None:
        self.root.configure(cursor="watch" if busy else "")
        self.root.update_idletasks()

    def _mkdocs_executable_or_error(self) -> str | None:
        executable = find_mkdocs_executable()
        if executable is not None:
            return executable

        messagebox.showerror(
            "MkDocs indisponible",
            "MkDocs est introuvable dans .venv, dans venv et dans le "
            "PATH.\n\nInstallez MkDocs dans l'environnement Python du "
            "projet.",
            parent=self.root,
        )
        self.status.set("MkDocs n'est pas disponible.")
        return None

    def _cleanup_prepared_worktree(self) -> None:
        if self.prepared_worktree is None:
            return
        self._remove_git_worktree(self.prepared_worktree)
        self.prepared_worktree = None
        self.prepared_publication = None
        self.pushed_source_sha = None
        self.commit_push_button.configure(state="disabled")

    def _remove_git_worktree(self, worktree: Path) -> str | None:
        cleanup_errors: list[str] = []
        if (worktree / ".git").exists():
            completed = subprocess.run(
                ["git", "worktree", "remove", "--force", str(worktree)],
                cwd=publisher.PROJECT_ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            if completed.returncode != 0:
                cleanup_errors.append(format_command_output(completed))
        try:
            shutil.rmtree(worktree, ignore_errors=True)
        except OSError as error:
            cleanup_errors.append(str(error))
        return "\n".join(item for item in cleanup_errors if item) or None

    def _remap_resources_to_docs_root(
        self,
        docs_root: Path,
        selected: list[publisher.Resource],
    ) -> tuple[list[publisher.Resource], list[publisher.Resource]]:
        selected_set = set(selected)
        remapped_resources: list[publisher.Resource] = []
        remapped_selected: list[publisher.Resource] = []

        for resource in self.resources:
            relative_destination = resource.destination.relative_to(
                publisher.DOCS_ROOT
            )
            remapped = publisher.Resource(
                source=resource.source,
                destination=docs_root / relative_destination,
                kind=resource.kind,
                notion=resource.notion,
            )
            remapped_resources.append(remapped)
            if resource in selected_set:
                remapped_selected.append(remapped)

        return remapped_resources, remapped_selected

    def _run_command(
        self,
        cwd: Path,
        *args: str,
    ) -> tuple[subprocess.CompletedProcess[str], str]:
        completed = subprocess.run(
            list(args),
            cwd=cwd,
            text=True,
            capture_output=True,
            check=False,
        )
        output = "\n".join(
            part.strip()
            for part in (completed.stdout, completed.stderr)
            if part.strip()
        )
        return completed, output

    def _git_output_or_error(self, cwd: Path, *args: str) -> str:
        completed, output = self._run_command(cwd, "git", *args)
        if completed.returncode != 0:
            command = "git " + " ".join(args)
            raise RuntimeError(f"Commande Git échouée : {command}\n\n{output}")
        return output

    def _rev_parse(self, cwd: Path, ref: str) -> str:
        return self._git_output_or_error(cwd, "rev-parse", "--verify", ref).strip()

    def _validate_gh_pages_artifact(
        self,
        cwd: Path,
        source_sha: str,
        site_directory: Path,
        expected_outputs: tuple[str, ...],
    ) -> str:
        fetch_output = self._git_output_or_error(cwd, "fetch", "origin")
        current_origin_main = self._rev_parse(cwd, "origin/main")
        if current_origin_main != source_sha:
            raise RuntimeError(
                "Contrôle post-déploiement échoué : origin/main a changé.\n\n"
                f"Source déployée : {source_sha}\n"
                f"origin/main actuel : {current_origin_main}"
            )

        gh_pages_sha = self._rev_parse(cwd, "origin/gh-pages")
        required_paths = [".nojekyll", "sitemap.xml", *expected_outputs]
        missing_build_paths = [
            path for path in required_paths if not (site_directory / path).exists()
        ]
        if missing_build_paths:
            raise RuntimeError(
                "Contrôle post-déploiement échoué : fichier(s) absent(s) "
                "dans le build MkDocs.\n\n"
                + "\n".join(f"- {path}" for path in missing_build_paths)
            )

        missing_paths: list[str] = []
        for path in required_paths:
            check = run_git(cwd, "cat-file", "-e", f"origin/gh-pages:{path}")
            if check.returncode != 0:
                missing_paths.append(path)
        if missing_paths:
            raise RuntimeError(
                "Contrôle post-déploiement échoué : fichier(s) absent(s) "
                "dans origin/gh-pages.\n\n"
                + "\n".join(f"- {path}" for path in missing_paths)
            )

        lines = [
            f"Source SHA : {source_sha}",
            f"origin/gh-pages : {gh_pages_sha}",
            f"Fetch après déploiement : {fetch_output or '(aucune sortie)'}",
            "Contrôles gh-pages :",
        ]
        lines.extend(f"- {path}" for path in required_paths)
        return "\n".join(lines)

    def _deploy_from_clean_worktree(
        self,
        executable: str,
        source_sha: str,
        expected_resources: tuple[str, ...],
    ) -> DeploymentResult:
        deploy_worktree = Path(
            tempfile.mkdtemp(
                prefix=f"{publisher.PROJECT_ROOT.name}-deploy-{source_sha[:12]}-"
            )
        )
        site_directory = Path(
            tempfile.mkdtemp(prefix=f"{publisher.PROJECT_ROOT.name}-gh-pages-")
        )
        cleanup_warnings: list[str] = []
        command_output = ""
        post_deploy_details = ""
        try:
            fetch, fetch_output = self._run_command(
                publisher.PROJECT_ROOT,
                "git",
                "fetch",
                "origin",
            )
            if fetch.returncode != 0:
                raise RuntimeError(
                    "Impossible d'actualiser origin/main avant déploiement.\n\n"
                    + fetch_output
                )

            origin_main = self._rev_parse(publisher.PROJECT_ROOT, "origin/main")
            if origin_main != source_sha:
                raise RuntimeError(
                    "Déploiement bloqué : origin/main a changé avant le "
                    "déploiement.\n\n"
                    f"Source attendue : {source_sha}\n"
                    f"origin/main actuel : {origin_main}"
                )

            add_worktree, add_worktree_output = self._run_command(
                publisher.PROJECT_ROOT,
                "git",
                "worktree",
                "add",
                "--detach",
                str(deploy_worktree),
                "origin/main",
            )
            if add_worktree.returncode != 0:
                raise RuntimeError(
                    "Impossible de créer le worktree de déploiement.\n\n"
                    + add_worktree_output
                )

            status = self._git_output_or_error(
                deploy_worktree, "status", "--porcelain"
            )
            if status.strip():
                raise RuntimeError(
                    "Déploiement bloqué : le worktree de déploiement "
                    "n'est pas propre.\n\n"
                    + status
                )

            deploy_head = self._rev_parse(deploy_worktree, "HEAD")
            deploy_origin_main = self._rev_parse(deploy_worktree, "origin/main")
            if deploy_head != source_sha or deploy_origin_main != source_sha:
                raise RuntimeError(
                    "Déploiement bloqué : la source du worktree ne correspond "
                    "pas au SHA attendu.\n\n"
                    f"Source attendue : {source_sha}\n"
                    f"HEAD : {deploy_head}\n"
                    f"origin/main : {deploy_origin_main}"
                )

            build, build_output = self._run_command(
                deploy_worktree,
                executable,
                "build",
                "--strict",
                "--site-dir",
                str(site_directory),
            )
            if build.returncode != 0:
                raise RuntimeError(
                    "mkdocs build --strict a échoué avant déploiement.\n\n"
                    + build_output
                )

            deploy = subprocess.run(
                [
                    executable,
                    "gh-deploy",
                    "--strict",
                    "--force",
                    "--site-dir",
                    str(site_directory),
                ],
                cwd=deploy_worktree,
                text=True,
                capture_output=True,
                check=False,
            )
            command_output = format_command_output(deploy)
            if deploy.returncode != 0:
                raise RuntimeError(
                    command_output
                    or f"mkdocs gh-deploy a renvoyé le code {deploy.returncode}."
                )

            post_deploy_details = self._validate_gh_pages_artifact(
                deploy_worktree,
                source_sha,
                site_directory,
                expected_resources,
            )
        finally:
            cleanup_error = self._remove_git_worktree(deploy_worktree)
            if cleanup_error:
                cleanup_warnings.append(cleanup_error)
            try:
                shutil.rmtree(site_directory, ignore_errors=True)
            except OSError as error:
                cleanup_warnings.append(str(error))
        return DeploymentResult(
            source_sha=source_sha,
            command_output=command_output,
            post_deploy_details=post_deploy_details,
            cleanup_warnings=tuple(cleanup_warnings),
        )

    def _prepare_report(
        self,
        worktree: Path,
        publication_report: publisher.PublicationReport,
        build_output: str,
        added: list[str],
        modified: list[str],
        deleted: list[str],
        untracked: list[str],
    ) -> str:
        lines = [
            "PRÉPARATION DE LA MISE EN LIGNE",
            "================================",
            "",
            f"Worktree temporaire : {worktree}",
            "",
            format_report(publication_report),
            "",
            "BUILD STRICT",
            "------------",
            build_output or "mkdocs build --strict terminé sans sortie.",
            "",
        ]
        add_staging_section(lines, "AJOUTÉS", added)
        add_staging_section(lines, "MODIFIÉS", modified)
        add_staging_section(lines, "SUPPRIMÉS", deleted)
        add_staging_section(lines, "NON SUIVIS", untracked)
        lines.extend(
            [
                "Aucun commit, push ou déploiement n'a été exécuté.",
            ]
        )
        return "\n".join(lines)

    def scan_resources(self) -> None:
        try:
            if not publisher.SOURCE_ROOT.is_dir():
                raise FileNotFoundError(
                    f"Dossier source introuvable : {publisher.SOURCE_ROOT}"
                )
            if not publisher.DOCS_ROOT.is_dir():
                raise FileNotFoundError(
                    f"Dossier MkDocs introuvable : {publisher.DOCS_ROOT}"
                )

            (
                self.resources,
                self.pdf_count,
                self.ignored_pdf_count,
            ) = publisher.discover_resources(
                publisher.SOURCE_ROOT,
                publisher.DOCS_ROOT,
            )
        except (OSError, ValueError) as error:
            self.status.set("Impossible d'analyser les ressources.")
            self._set_output(f"ERREUR\n\n{error}")
            messagebox.showerror("Erreur d'analyse", str(error), parent=self.root)
            return

        self._display_resource_checkboxes()

        if self.pdf_count == 0:
            message = (
                "Aucun PDF trouvé dans le dossier source :\n"
                f"{publisher.SOURCE_ROOT}"
            )
            self.status.set("Aucun PDF trouvé.")
            self._set_output(message)
            messagebox.showwarning("Aucun PDF", message, parent=self.root)
            return

        if not self.resources:
            message = (
                f"{self.pdf_count} PDF trouvé(s), mais aucun nom de fichier "
                "n'est reconnu."
            )
            self.status.set("Aucun PDF reconnu.")
            self._set_output(message)
            messagebox.showwarning(
                "Aucun PDF reconnu",
                message,
                parent=self.root,
            )
            return

        self._set_resource_buttons_state("normal")
        self._update_selection_status()
        self._set_output(
            f"{len(self.resources)} document(s) reconnu(s) parmi "
            f"{self.pdf_count} PDF.\n\n"
            "Choisissez les documents puis utilisez « Prévisualiser » "
            "avant de publier."
        )

    def _display_resource_checkboxes(self) -> None:
        for child in self.documents_frame.winfo_children():
            child.destroy()
        self.variables.clear()

        if not self.resources:
            ttk.Label(
                self.documents_frame,
                text="Aucun document reconnu.",
            ).grid(row=0, column=0, sticky="w")
            return

        resources_by_notion: dict[
            str, list[publisher.Resource]
        ] = defaultdict(list)
        for resource in sorted(
            self.resources,
            key=lambda item: (
                item.notion,
                publisher.KIND_ORDER[item.kind],
                item.source.name.casefold(),
            ),
        ):
            resources_by_notion[resource.notion].append(resource)

        self.documents_frame.columnconfigure(0, weight=1)
        for row, notion in enumerate(sorted(resources_by_notion)):
            notion_resources = resources_by_notion[notion]
            try:
                topic = publisher.notion_display_topic(
                    notion,
                    notion_resources,
                    publisher.DOCS_ROOT,
                )
            except (OSError, ValueError):
                topic = None
            title = f"{notion} — {topic}" if topic else notion

            notion_frame = ttk.LabelFrame(
                self.documents_frame,
                text=title,
                padding=(10, 5),
            )
            notion_frame.grid(
                row=row,
                column=0,
                sticky="ew",
                pady=(0, 8),
            )
            notion_frame.columnconfigure(0, weight=1)

            kind_counts = Counter(
                resource.kind for resource in notion_resources
            )
            for resource_row, resource in enumerate(notion_resources):
                variable = tk.BooleanVar(
                    value=resource.kind in publisher.SAFE_DEFAULT_KINDS
                )
                self.variables[resource] = variable
                label = publisher.selection_label(
                    resource,
                    duplicate_kind=kind_counts[resource.kind] > 1,
                )
                ttk.Checkbutton(
                    notion_frame,
                    text=label,
                    variable=variable,
                    command=self._update_selection_status,
                ).grid(
                    row=resource_row,
                    column=0,
                    sticky="w",
                    pady=2,
                )

    def selected_resources(self) -> list[publisher.Resource]:
        return [
            resource
            for resource in self.resources
            if self.variables[resource].get()
        ]

    def _update_selection_status(self) -> None:
        self.deploy_button.configure(state="disabled")
        self.prepare_online_button.configure(state="disabled")
        self.commit_push_button.configure(state="disabled")
        self.prepared_publication = None
        selected_count = len(self.selected_resources())
        self.status.set(
            f"{selected_count} document(s) sélectionné(s) sur "
            f"{len(self.resources)}."
        )

    def select_safe(self) -> None:
        for resource, variable in self.variables.items():
            variable.set(resource.kind in publisher.SAFE_DEFAULT_KINDS)
        self._update_selection_status()

    def clear_all(self) -> None:
        for variable in self.variables.values():
            variable.set(False)
        self._update_selection_status()

    def select_all(self) -> None:
        confirmed = messagebox.askyesno(
            "Tout sélectionner",
            "Cette sélection inclura les mini-tests, les devoirs et tous "
            "les corrigés.\n\nVoulez-vous vraiment tout cocher ?",
            parent=self.root,
        )
        if not confirmed:
            return
        for variable in self.variables.values():
            variable.set(True)
        self._update_selection_status()

    def _run_publication(
        self,
        selected: list[publisher.Resource],
        dry_run: bool,
    ) -> publisher.PublicationReport:
        if not publisher.SOURCE_ROOT.is_dir():
            raise FileNotFoundError(
                f"Dossier source introuvable : {publisher.SOURCE_ROOT}"
            )
        if not publisher.DOCS_ROOT.is_dir():
            raise FileNotFoundError(
                f"Dossier MkDocs introuvable : {publisher.DOCS_ROOT}"
            )
        for resource in selected:
            if not resource.source.is_file():
                raise FileNotFoundError(
                    f"PDF source introuvable : {resource.source}"
                )

        return publisher.publish_selected_resources(
            self.resources,
            selected,
            publisher.DOCS_ROOT,
            self.pdf_count,
            self.ignored_pdf_count,
            dry_run=dry_run,
        )

    def preview(self) -> None:
        selected = self.selected_resources()
        self._set_busy(True)
        try:
            report = self._run_publication(selected, dry_run=True)
        except (OSError, ValueError) as error:
            self._set_output(f"ERREUR DE PRÉVISUALISATION\n\n{error}")
            messagebox.showerror(
                "Prévisualisation impossible",
                str(error),
                parent=self.root,
            )
            self.status.set("Échec de la prévisualisation.")
            return
        finally:
            self._set_busy(False)

        self._set_output(format_report(report))
        self.status.set(
            "Prévisualisation terminée : aucune écriture effectuée."
        )

    def publish(self) -> None:
        selected = self.selected_resources()
        confirmation = (
            f"Publier {len(selected)} document(s) sélectionné(s) ?\n\n"
            "Les liens des documents non sélectionnés seront retirés des "
            "zones AUTO-DOCS. Les PDF déjà présents dans docs/ ne seront "
            "pas supprimés."
        )
        if not messagebox.askyesno(
            "Confirmer la publication",
            confirmation,
            parent=self.root,
        ):
            return

        self.deploy_button.configure(state="disabled")
        self.commit_push_button.configure(state="disabled")
        self._set_busy(True)
        try:
            report = self._run_publication(selected, dry_run=False)
        except (OSError, ValueError) as error:
            message = (
                f"{error}\n\nLa publication a été interrompue. Certains "
                "fichiers ont éventuellement été copiés avant l'erreur ; "
                "aucun PDF existant n'a été supprimé."
            )
            self._set_output(f"ERREUR DE PUBLICATION\n\n{message}")
            messagebox.showerror(
                "Erreur de publication",
                message,
                parent=self.root,
            )
            self.status.set("Publication interrompue.")
            return
        finally:
            self._set_busy(False)

        self._set_output(format_report(report))
        self.prepare_online_button.configure(state="normal")
        self.deploy_button.configure(state="disabled")
        self.status.set(
            f"Publication terminée : {len(report.copied_files)} fichier(s) "
            f"copié(s), {len(report.modified_pages)} page(s) modifiée(s). "
            "La préparation de mise en ligne est maintenant disponible."
        )

        if report.missing_pages or report.warnings:
            details = []
            if report.missing_pages:
                details.append(
                    "Pages introuvables : "
                    + ", ".join(report.missing_pages)
                )
            if report.warnings:
                details.append(
                    f"{len(report.warnings)} autre(s) avertissement(s)."
                )
            messagebox.showwarning(
                "Publication terminée avec avertissements",
                "\n".join(details)
                + "\n\nConsultez le bilan pour plus de détails. Vous "
                "pouvez ensuite déployer les pages disponibles.",
                parent=self.root,
            )
        else:
            messagebox.showinfo(
                "Publication terminée",
                "Les fichiers locaux ont été mis à jour.\n\n"
                "Cliquez maintenant sur « Préparer la mise en ligne » "
                "pour construire un worktree propre depuis origin/main.",
                parent=self.root,
            )

    def prepare_online_publication(self) -> None:
        executable = self._mkdocs_executable_or_error()
        if executable is None:
            return

        selected = self.selected_resources()
        if not selected:
            messagebox.showwarning(
                "Aucune sélection",
                "Aucun document n'est sélectionné.",
                parent=self.root,
            )
            return

        confirmed = messagebox.askyesno(
            "Préparer la mise en ligne",
            "Cette opération va créer un worktree temporaire propre depuis "
            "origin/main, y rejouer la sélection actuelle, puis lancer "
            "mkdocs build --strict.\n\n"
            "Aucun commit, push ou déploiement ne sera effectué.\n\n"
            "Continuer ?",
            parent=self.root,
        )
        if not confirmed:
            return

        self._set_busy(True)
        self._cleanup_prepared_worktree()
        worktree = Path(
            tempfile.mkdtemp(prefix=f"{publisher.PROJECT_ROOT.name}-prepare-")
        )
        build_dir = Path(
            tempfile.mkdtemp(prefix=f"{publisher.PROJECT_ROOT.name}-build-")
        )
        try:
            fetch, fetch_output = self._run_command(
                publisher.PROJECT_ROOT,
                "git",
                "fetch",
                "origin",
            )
            if fetch.returncode != 0:
                raise RuntimeError(
                    "Impossible d'actualiser origin/main.\n\n"
                    + fetch_output
                )

            base_sha = self._rev_parse(publisher.PROJECT_ROOT, "origin/main")
            add_worktree, add_worktree_output = self._run_command(
                publisher.PROJECT_ROOT,
                "git",
                "worktree",
                "add",
                "--detach",
                str(worktree),
                "origin/main",
            )
            if add_worktree.returncode != 0:
                raise RuntimeError(
                    "Impossible de créer le worktree temporaire.\n\n"
                    + add_worktree_output
                )

            docs_root = worktree / "docs"
            resources, selected_resources = self._remap_resources_to_docs_root(
                docs_root,
                selected,
            )
            publication_report = publisher.publish_selected_resources(
                resources,
                selected_resources,
                docs_root,
                self.pdf_count,
                self.ignored_pdf_count,
                dry_run=False,
            )

            build, build_output = self._run_command(
                worktree,
                executable,
                "build",
                "--strict",
                "--site-dir",
                str(build_dir),
            )
            if build.returncode != 0:
                raise RuntimeError(
                    "mkdocs build --strict a échoué dans le worktree.\n\n"
                    + build_output
                )

            status, status_output = self._run_command(
                worktree,
                "git",
                "status",
                "--porcelain",
            )
            if status.returncode != 0:
                raise RuntimeError(
                    "Impossible de lire l'état Git du worktree.\n\n"
                    + status_output
                )
            added, modified, deleted, untracked = classify_staging_status(
                status_output
            )
            if deleted:
                raise RuntimeError(
                    "Préparation bloquée : une suppression est détectée "
                    "dans le worktree préparé.\n\n"
                    + "\n".join(f"- {path}" for path in deleted)
                )
            staged_paths = stageable_paths_from_status(
                worktree,
                publication_report,
                added,
                modified,
                untracked,
            )

            self.prepared_worktree = worktree
            self.prepared_publication = PreparedPublication(
                worktree=worktree,
                base_sha=base_sha,
                staged_paths=staged_paths,
            )
            self._set_output(
                self._prepare_report(
                    worktree,
                    publication_report,
                    build_output,
                    added,
                    modified,
                    deleted,
                    untracked,
                )
            )
            self.status.set(
                "Worktree propre préparé depuis origin/main. "
                "Aucun commit, push ou déploiement n'a été exécuté."
            )
            self.commit_push_button.configure(state="normal")
            messagebox.showinfo(
                "Préparation terminée",
                "Le worktree temporaire a été préparé et le build strict "
                "a réussi.\n\n"
                f"{worktree}\n\n"
                "Aucun commit, push ou déploiement n'a été exécuté.",
                parent=self.root,
            )
        except (OSError, RuntimeError, ValueError) as error:
            self._remove_git_worktree(worktree)
            self._set_output(f"ERREUR DE PRÉPARATION\n\n{error}")
            messagebox.showerror(
                "Préparation impossible",
                str(error),
                parent=self.root,
            )
            self.status.set("Préparation de mise en ligne interrompue.")
        finally:
            shutil.rmtree(build_dir, ignore_errors=True)
            self._set_busy(False)

    def commit_and_push_prepared_publication(self) -> None:
        prepared = self.prepared_publication
        if prepared is None:
            messagebox.showwarning(
                "Aucune préparation",
                "Préparez d'abord la mise en ligne.",
                parent=self.root,
            )
            return
        if not prepared.worktree.is_dir():
            self.prepared_publication = None
            self.commit_push_button.configure(state="disabled")
            messagebox.showerror(
                "Worktree introuvable",
                "Le worktree temporaire préparé n'existe plus.",
                parent=self.root,
            )
            return
        if not prepared.staged_paths:
            messagebox.showinfo(
                "Aucun changement",
                "Aucun fichier n'est à commiter dans le worktree préparé.",
                parent=self.root,
            )
            return

        message = simpledialog.askstring(
            "Message de commit",
            "Message de commit :",
            initialvalue="Publication ressources Première spécialité",
            parent=self.root,
        )
        if message is None:
            return
        message = message.strip()
        if not message:
            messagebox.showwarning(
                "Message vide",
                "Le message de commit ne peut pas être vide.",
                parent=self.root,
            )
            return

        confirmed = messagebox.askyesno(
            "Confirmer commit + push",
            "Cette opération va créer un commit dans le worktree temporaire "
            "puis pousser HEAD vers origin/main.\n\n"
            "Aucun gh-deploy ne sera exécuté.\n\n"
            "Continuer ?",
            parent=self.root,
        )
        if not confirmed:
            return

        self._set_busy(True)
        try:
            self._git_output_or_error(
                prepared.worktree,
                "add",
                "--",
                *prepared.staged_paths,
            )
            cached_stat = self._git_output_or_error(
                prepared.worktree,
                "diff",
                "--cached",
                "--stat",
            )
            no_delete, cached_name_status = ensure_no_staged_deletion(
                prepared.worktree
            )
            if not no_delete:
                raise RuntimeError(
                    "Commit bloqué : une suppression est stageée.\n\n"
                    + cached_name_status
                )
            if not cached_name_status.strip():
                raise RuntimeError("Commit bloqué : aucun changement stageé.")

            fetch_output = self._git_output_or_error(
                prepared.worktree,
                "fetch",
                "origin",
            )
            current_origin_main = self._rev_parse(
                prepared.worktree, "origin/main"
            )
            if current_origin_main != prepared.base_sha:
                raise RuntimeError(
                    "Push bloqué : origin/main a changé depuis la préparation.\n\n"
                    f"Base préparée : {prepared.base_sha}\n"
                    f"origin/main actuel : {current_origin_main}"
                )

            commit_output = self._git_output_or_error(
                prepared.worktree,
                "commit",
                "-m",
                message,
            )
            commit_sha = self._rev_parse(prepared.worktree, "HEAD")
            ancestor = run_git(
                prepared.worktree,
                "merge-base",
                "--is-ancestor",
                prepared.base_sha,
                commit_sha,
            )
            if ancestor.returncode != 0:
                raise RuntimeError(
                    "Push bloqué : le commit créé n'est pas descendant "
                    "direct de la base préparée."
                )

            push_output = self._git_output_or_error(
                prepared.worktree,
                "push",
                "origin",
                "HEAD:refs/heads/main",
            )
            self._git_output_or_error(prepared.worktree, "fetch", "origin")
            final_origin_main = self._rev_parse(prepared.worktree, "origin/main")
            if final_origin_main != commit_sha:
                raise RuntimeError(
                    "Source Git non synchronisée après push.\n\n"
                    f"Commit local : {commit_sha}\n"
                    f"origin/main : {final_origin_main}"
                )

            self._append_output(
                "COMMIT + PUSH SOURCE\n"
                "====================\n\n"
                "✓ Build strict réussi\n"
                "✓ Diff contrôlé\n"
                f"✓ Commit créé : {commit_sha}\n"
                "✓ origin/main mis à jour\n"
                "✓ Source Git synchronisée\n\n"
                "DIFF STAGÉ --STAT\n"
                "-----------------\n"
                f"{cached_stat or '(aucun)'}\n\n"
                "DIFF STAGÉ --NAME-STATUS\n"
                "------------------------\n"
                f"{cached_name_status}\n\n"
                "SORTIE FETCH AVANT PUSH\n"
                "-----------------------\n"
                f"{fetch_output or '(aucune sortie)'}\n\n"
                "SORTIE COMMIT\n"
                "-------------\n"
                f"{commit_output}\n\n"
                "SORTIE PUSH\n"
                "-----------\n"
                f"{push_output or '(aucune sortie)'}\n\n"
                "Aucun déploiement GitHub Pages n'a été exécuté."
            )
            self.status.set(
                "Source Git synchronisée. Le déploiement GitHub Pages "
                "est maintenant disponible."
            )
            self.pushed_source_sha = commit_sha
            self.commit_push_button.configure(state="disabled")
            self.deploy_button.configure(state="normal")
            messagebox.showinfo(
                "Source synchronisée",
                "Le commit a été créé et origin/main est à jour.\n\n"
                f"{commit_sha}\n\n"
                "Aucun déploiement GitHub Pages n'a été exécuté.",
                parent=self.root,
            )
        except (OSError, RuntimeError, ValueError) as error:
            self._append_output(f"ERREUR COMMIT + PUSH SOURCE\n\n{error}")
            messagebox.showerror(
                "Commit + push impossible",
                str(error),
                parent=self.root,
            )
            self.status.set("Commit + push source interrompu.")
        finally:
            self._set_busy(False)

    def deploy_github_pages(self) -> None:
        executable = self._mkdocs_executable_or_error()
        if executable is None:
            return

        source_sha = self.pushed_source_sha
        prepared = self.prepared_publication
        if source_sha is None or prepared is None:
            messagebox.showerror(
                "Déploiement bloqué",
                "Déploiement bloqué : aucune source préparée et poussée "
                "n'est disponible dans cette session.",
                parent=self.root,
            )
            self.status.set("Déploiement bloqué : source non synchronisée.")
            return
        expected_resources = tuple(
            deployed_site_paths(prepared.staged_paths)
        )

        confirmed = messagebox.askyesno(
            "Déployer le site public",
            "Cette opération va créer un nouveau worktree temporaire propre "
            "depuis origin/main, vérifier le SHA source, construire avec "
            "mkdocs build --strict, puis lancer gh-deploy depuis ce worktree.\n\n"
            f"Source Git :\n{source_sha}\n\n"
            f"Adresse publique :\n{PUBLIC_SITE_URL}\n\n"
            "Continuer ?",
            parent=self.root,
        )
        if not confirmed:
            return

        self._set_busy(True)
        try:
            result = self._deploy_from_clean_worktree(
                executable,
                source_sha,
                expected_resources,
            )
        except (OSError, RuntimeError, ValueError) as error:
            self._append_output(
                "ERREUR DE DÉPLOIEMENT GITHUB PAGES\n"
                "===================================\n\n"
                + str(error)
            )
            messagebox.showerror(
                "Déploiement GitHub Pages impossible",
                "Le site public n'a pas été actualisé.\n\n"
                "Consultez le bilan pour connaître l'erreur Git ou MkDocs.",
                parent=self.root,
            )
            self.status.set("Le déploiement GitHub Pages a échoué.")
            return
        finally:
            self._set_busy(False)

        cleanup_details = ""
        if result.cleanup_warnings:
            cleanup_details = (
                "\n\nAVERTISSEMENT NETTOYAGE\n"
                "-----------------------\n"
                + "\n".join(result.cleanup_warnings)
            )
        self._append_output(
            "DÉPLOIEMENT GITHUB PAGES\n"
            "========================\n\n"
            "✓ Source enregistrée dans Git\n"
            "✓ origin/main synchronisé\n"
            "✓ Build strict réussi\n"
            "✓ Déploiement GitHub Pages réussi\n"
            f"✓ Site construit depuis {result.source_sha}\n\n"
            "CONTRÔLES APRÈS DÉPLOIEMENT\n"
            "---------------------------\n"
            f"{result.post_deploy_details}\n\n"
            "SORTIE GH-DEPLOY\n"
            "----------------\n"
            f"{result.command_output or '(aucune sortie)'}"
            f"{cleanup_details}\n\n"
            f"Site public actualisé : {PUBLIC_SITE_URL}\n\n"
            "Le dossier site/ du projet principal n'a pas été modifié."
        )
        self.deploy_button.configure(state="disabled")
        self.status.set(
            "Déploiement terminé. GitHub Pages peut demander quelques "
            "secondes pour actualiser le site public."
        )
        messagebox.showinfo(
            "Site public déployé",
            "Le déploiement GitHub Pages est terminé.\n\n"
            f"{PUBLIC_SITE_URL}\n\n"
            "L'actualisation publique peut prendre quelques secondes.",
            parent=self.root,
        )

    def launch_mkdocs(self) -> None:
        if (
            self.mkdocs_process is not None
            and self.mkdocs_process.poll() is None
        ):
            messagebox.showinfo(
                "Serveur déjà lancé",
                "mkdocs serve est déjà en cours d'exécution.",
                parent=self.root,
            )
            return

        executable = self._mkdocs_executable_or_error()
        if executable is None:
            return

        try:
            self.mkdocs_process = subprocess.Popen(
                [executable, "serve"],
                cwd=publisher.PROJECT_ROOT,
            )
        except OSError as error:
            messagebox.showerror(
                "Impossible de lancer MkDocs",
                str(error),
                parent=self.root,
            )
            self.status.set("Échec du lancement de MkDocs.")
            return

        self.status.set(
            "Aperçu local disponible sur http://127.0.0.1:8000/ — "
            "il ne modifie pas le site public."
        )
        self.root.after(750, self._poll_mkdocs)

    def _poll_mkdocs(self) -> None:
        if self.mkdocs_process is None:
            return
        return_code = self.mkdocs_process.poll()
        if return_code is None:
            self.root.after(750, self._poll_mkdocs)
            return

        self.status.set(
            f"mkdocs serve s'est arrêté avec le code {return_code}."
        )
        self.mkdocs_process = None

    def quit(self) -> None:
        self._cleanup_prepared_worktree()
        if (
            self.mkdocs_process is not None
            and self.mkdocs_process.poll() is None
        ):
            self.mkdocs_process.terminate()
            try:
                self.mkdocs_process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                self.mkdocs_process.kill()
        self.root.destroy()


def main() -> int:
    try:
        root = tk.Tk()
    except tk.TclError as error:
        print(
            "Impossible d'ouvrir l'interface Tkinter "
            f"(affichage graphique indisponible) : {error}",
            file=sys.stderr,
        )
        return 1

    PublicationApp(root)
    root.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
