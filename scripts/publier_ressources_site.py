#!/usr/bin/env python3
"""Publier les PDF de travail dans la documentation MkDocs."""

from __future__ import annotations

import argparse
import filecmp
import os
import re
import shutil
import subprocess
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import quote


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = PROJECT_ROOT / "docs"
SOURCE_ROOT = (
    Path.home()
    / "ENSEIGNEMENT"
    / "IA_AGENT_MATHS"
    / "GPT-première"
    / "Version en cours"
)

AUTO_DOCS_START = "<!-- AUTO-DOCS:START -->"
AUTO_DOCS_END = "<!-- AUTO-DOCS:END -->"

DESTINATION_DIRS = {
    "COURS": "cours",
    "TD": "td",
    "CORRIGE": "corriges",
    "AUTOMATISMES": "automatismes",
    "MINITEST": "automatismes",
    "DS": "ds",
}

LABELS = {
    "COURS": "Cours",
    "TD": "TD",
    "AUTOMATISMES": "Automatismes",
    "MINITEST": "Mini-test",
    "DS": "DS",
}

# Formulations pédagogiques des thèmes actuellement publiés. Si un nouveau
# thème n'est pas encore répertorié ici, le titre de la page Markdown sert de
# repli afin de ne jamais afficher le nom technique du fichier en majuscules.
TOPIC_TITLES = {
    "RENTREE_DIAGNOSTIC_LOGIQUE_INTERVALLES": (
        "Rentrée : diagnostic, logique et intervalles"
    ),
    "SECOND_DEGRE_FONCTION_CARRE_FORME_CANONIQUE": (
        "Second degré : fonction carré et forme canonique"
    ),
    "SECOND_DEGRE_FORMES_RACINES_SIGNE_DISCRIMINANT": (
        "Second degré : formes, racines, signe et discriminant"
    ),
    "SECOND_DEGRE_INEQUATIONS_OPTIMISATION_PROBLEMES": (
        "Second degré : inéquations, optimisation et problèmes"
    ),
    "PRODUIT_SCALAIRE_DEFINITION_PROJECTION_COORDONNEES": (
        "Produit scalaire : définition, projection et coordonnées"
    ),
    "PRODUIT_SCALAIRE_IDENTITES_AL_KASHI_LIEUX_POINTS": (
        "Produit scalaire : identités, Al-Kashi et lieux de points"
    ),
}

KIND_ORDER = {
    "COURS": 0,
    "TD": 1,
    "CORRIGE": 2,
    "AUTOMATISMES": 3,
    "MINITEST": 4,
    "DS": 5,
}

# Le cas CORRIGE_TD_Nxx existe déjà dans les ressources de travail. Il doit
# être testé avant TD_Nxx pour ne pas finir par erreur dans docs/td.
RESOURCE_PATTERNS = (
    (
        "CORRIGE",
        re.compile(
            r"^CORRIG(?:E|É)(?:_(?:TD|DS))?_N(?P<number>\d{2})(?:_|$)",
            re.IGNORECASE,
        ),
    ),
    (
        "COURS",
        re.compile(r"^COURS_N(?P<number>\d{2})(?:_|$)", re.IGNORECASE),
    ),
    (
        "TD",
        re.compile(r"^TD_N(?P<number>\d{2})(?:_|$)", re.IGNORECASE),
    ),
    (
        "AUTOMATISMES",
        re.compile(
            r"^AUTOMATISMES_N(?P<number>\d{2})(?:_|$)",
            re.IGNORECASE,
        ),
    ),
    (
        "MINITEST",
        re.compile(r"^MINITEST_N(?P<number>\d{2})(?:_|$)", re.IGNORECASE),
    ),
    (
        "DS",
        re.compile(r"^DS_N(?P<number>\d{2})(?:_|$)", re.IGNORECASE),
    ),
)


@dataclass(frozen=True)
class Resource:
    source: Path
    destination: Path
    kind: str
    notion: str


@dataclass
class PublicationReport:
    pdf_count: int = 0
    ignored_pdf_count: int = 0
    resources: list[Resource] = field(default_factory=list)
    copied_files: list[Path] = field(default_factory=list)
    unchanged_files: list[Path] = field(default_factory=list)
    modified_pages: list[Path] = field(default_factory=list)
    unchanged_pages: list[Path] = field(default_factory=list)
    missing_pages: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def classify_pdf(path: Path) -> tuple[str, str] | None:
    """Retourner (type, notion) si le nom du PDF est reconnu."""
    if path.suffix.casefold() != ".pdf":
        return None

    for kind, pattern in RESOURCE_PATTERNS:
        match = pattern.match(path.stem)
        if match:
            return kind, f"N{match.group('number')}"
    return None


def ensure_inside_docs(path: Path, docs_root: Path) -> None:
    """Interdire toute destination qui sortirait de docs/, même par symlink."""
    resolved_docs = docs_root.resolve()
    resolved_path = path.resolve(strict=False)
    if not resolved_path.is_relative_to(resolved_docs):
        raise ValueError(f"Destination interdite hors de docs/ : {path}")


def discover_resources(
    source_root: Path, docs_root: Path
) -> tuple[list[Resource], int, int]:
    """Rechercher récursivement les PDF et construire leurs destinations."""
    resources: list[Resource] = []
    pdf_count = 0
    ignored_pdf_count = 0

    for path in sorted(source_root.rglob("*"), key=lambda item: str(item).casefold()):
        if not path.is_file() or path.suffix.casefold() != ".pdf":
            continue

        pdf_count += 1
        classification = classify_pdf(path)
        if classification is None:
            ignored_pdf_count += 1
            continue

        kind, notion = classification
        destination = docs_root / DESTINATION_DIRS[kind] / path.name
        ensure_inside_docs(destination, docs_root)
        resources.append(Resource(path, destination, kind, notion))

    destinations: dict[Path, Path] = {}
    for resource in resources:
        previous_source = destinations.setdefault(
            resource.destination, resource.source
        )
        if previous_source != resource.source:
            raise ValueError(
                "Deux PDF auraient la même destination : "
                f"{previous_source} et {resource.source}"
            )

    return resources, pdf_count, ignored_pdf_count


def copy_resources(resources: list[Resource], report: PublicationReport) -> None:
    """Copier uniquement les PDF absents ou dont le contenu diffère."""
    for resource in resources:
        destination = resource.destination
        destination.parent.mkdir(parents=True, exist_ok=True)

        if (
            destination.exists()
            and destination.is_file()
            and filecmp.cmp(resource.source, destination, shallow=False)
        ):
            report.unchanged_files.append(destination)
            continue

        shutil.copy2(resource.source, destination)
        report.copied_files.append(destination)


def find_notion_page(docs_root: Path, notion: str) -> Path | None:
    """Trouver l'unique page docs/notions/Nxx-*.md."""
    matches = sorted((docs_root / "notions").glob(f"{notion}-*.md"))
    if not matches:
        return None
    if len(matches) > 1:
        names = ", ".join(str(path) for path in matches)
        raise ValueError(f"Plusieurs pages correspondent à {notion} : {names}")
    return matches[0]


def topic_slug_from_filename(path: Path) -> str | None:
    """Extraire la partie descriptive située après Nxx dans le nom."""
    match = re.search(r"(?:^|_)N\d{2}(?:_|$)", path.stem, re.IGNORECASE)
    if match is None or match.end() == len(path.stem):
        return None
    return path.stem[match.end():].upper()


def notion_topic_from_heading(text: str, notion: str) -> str | None:
    """Extraire le sujet lisible depuis un titre « # Nxx — Sujet »."""
    heading = re.search(
        rf"^#[ \t]+{re.escape(notion)}[ \t]+(?:—|-)[ \t]+(.+?)[ \t]*\r?$",
        text,
        flags=re.MULTILINE | re.IGNORECASE,
    )
    return heading.group(1).strip() if heading else None


def student_link_title(
    resource: Resource,
    fallback_topic: str | None = None,
) -> str:
    """Construire uniquement le texte visible du lien destiné aux élèves."""
    notion = resource.notion

    if resource.kind == "CORRIGE":
        upper_stem = resource.source.stem.upper()
        if re.match(r"^CORRIG(?:E|É)_TD_N\d{2}(?:_|$)", upper_stem):
            return f"Corrigé TD {notion}"
        if re.match(r"^CORRIG(?:E|É)_DS_N\d{2}(?:_|$)", upper_stem):
            return f"Corrigé DS {notion}"
        return f"Corrigé {notion}"

    if resource.kind in {"AUTOMATISMES", "MINITEST", "DS"}:
        return f"{LABELS[resource.kind]} {notion}"

    topic_slug = topic_slug_from_filename(resource.source)
    topic = TOPIC_TITLES.get(topic_slug or "", fallback_topic)
    title = f"{LABELS[resource.kind]} {notion}"
    return f"{title} — {topic}" if topic else title


def relative_link(markdown_page: Path, target: Path) -> str:
    relative_path = Path(os.path.relpath(target, start=markdown_page.parent))
    return quote(relative_path.as_posix(), safe="/")


def render_document_lines(
    markdown_page: Path,
    resources: list[Resource],
    fallback_topic: str | None = None,
) -> str:
    lines = []
    for resource in sorted(
        resources,
        key=lambda item: (
            KIND_ORDER[item.kind],
            item.destination.name.casefold(),
        ),
    ):
        title = student_link_title(resource, fallback_topic)
        link = relative_link(markdown_page, resource.destination)
        lines.append(f"- [{title}]({link})")
    return "\n".join(lines)


def detect_newline(text: str) -> str:
    return "\r\n" if "\r\n" in text else "\n"


def add_auto_docs_zone(text: str, content: str, newline: str) -> str:
    """Ajouter une zone sans supprimer le contenu manuel déjà présent."""
    block = (
        f"{AUTO_DOCS_START}{newline}"
        f"{content}{newline}"
        f"{AUTO_DOCS_END}"
    )
    documents_heading = re.search(
        r"^##[ \t]+Documents[ \t]*\r?$",
        text,
        flags=re.MULTILINE | re.IGNORECASE,
    )

    if documents_heading:
        line_end = text.find(newline, documents_heading.end())
        if line_end == -1:
            return f"{text}{newline}{newline}{block}{newline}"

        insertion_point = line_end + len(newline)
        insertion = f"{newline}{block}{newline}"
        return (
            text[:insertion_point]
            + insertion
            + text[insertion_point:]
        )

    if not text:
        prefix = ""
    elif text.endswith(("\n", "\r")):
        prefix = newline
    else:
        prefix = newline * 2

    return (
        f"{text}{prefix}"
        f"## Documents{newline}{newline}"
        f"{block}{newline}"
    )


def replace_auto_docs_zone(text: str, content: str, newline: str) -> str:
    """Remplacer strictement le contenu situé entre les deux marqueurs."""
    start_count = text.count(AUTO_DOCS_START)
    end_count = text.count(AUTO_DOCS_END)

    if start_count == 0 and end_count == 0:
        return add_auto_docs_zone(text, content, newline)
    if start_count != 1 or end_count != 1:
        raise ValueError(
            "Zone AUTO-DOCS mal formée : il faut exactement un marqueur "
            "START et un marqueur END"
        )

    content_start = text.index(AUTO_DOCS_START) + len(AUTO_DOCS_START)
    content_end = text.index(AUTO_DOCS_END)
    if content_end < content_start:
        raise ValueError("Zone AUTO-DOCS mal formée : END précède START")

    return (
        text[:content_start]
        + newline
        + content
        + newline
        + text[content_end:]
    )


def update_notion_pages(
    resources: list[Resource],
    docs_root: Path,
    report: PublicationReport,
) -> None:
    resources_by_notion: dict[str, list[Resource]] = defaultdict(list)
    for resource in resources:
        resources_by_notion[resource.notion].append(resource)

    for notion in sorted(resources_by_notion):
        try:
            markdown_page = find_notion_page(docs_root, notion)
        except ValueError as error:
            report.warnings.append(str(error))
            continue

        if markdown_page is None:
            report.missing_pages.append(notion)
            continue

        original_bytes = markdown_page.read_bytes()
        original_text = original_bytes.decode("utf-8")
        newline = detect_newline(original_text)
        fallback_topic = notion_topic_from_heading(original_text, notion)
        content = render_document_lines(
            markdown_page,
            resources_by_notion[notion],
            fallback_topic,
        ).replace("\n", newline)

        try:
            updated_text = replace_auto_docs_zone(
                original_text, content, newline
            )
        except ValueError as error:
            report.warnings.append(f"{markdown_page}: {error}")
            continue

        updated_bytes = updated_text.encode("utf-8")
        if updated_bytes == original_bytes:
            report.unchanged_pages.append(markdown_page)
            continue

        markdown_page.write_bytes(updated_bytes)
        report.modified_pages.append(markdown_page)


def publish(source_root: Path, docs_root: Path) -> PublicationReport:
    if not source_root.is_dir():
        raise FileNotFoundError(f"Dossier source introuvable : {source_root}")
    if not docs_root.is_dir():
        raise FileNotFoundError(f"Dossier MkDocs introuvable : {docs_root}")

    resources, pdf_count, ignored_pdf_count = discover_resources(
        source_root, docs_root
    )
    report = PublicationReport(
        pdf_count=pdf_count,
        ignored_pdf_count=ignored_pdf_count,
        resources=resources,
    )

    copy_resources(resources, report)
    update_notion_pages(resources, docs_root, report)
    return report


def display_paths(title: str, paths: list[Path], project_root: Path) -> None:
    print(f"{title} : {len(paths)}")
    for path in sorted(paths, key=lambda item: str(item).casefold()):
        try:
            displayed_path = path.relative_to(project_root)
        except ValueError:
            displayed_path = path
        print(f"  - {displayed_path}")


def display_report(report: PublicationReport, project_root: Path) -> None:
    print("\n=== Bilan de la publication ===")
    print(f"PDF trouvés       : {report.pdf_count}")
    print(f"PDF reconnus      : {len(report.resources)}")
    print(f"PDF ignorés       : {report.ignored_pdf_count}")
    display_paths("Fichiers copiés", report.copied_files, project_root)
    print(f"Fichiers déjà à jour : {len(report.unchanged_files)}")
    display_paths("Pages modifiées", report.modified_pages, project_root)
    print(f"Pages déjà à jour : {len(report.unchanged_pages)}")

    if report.missing_pages:
        notions = ", ".join(sorted(report.missing_pages))
        print(f"Pages introuvables : {notions}")

    if report.warnings:
        print(f"Avertissements : {len(report.warnings)}")
        for warning in report.warnings:
            print(f"  - {warning}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Publie les PDF de travail dans docs/ et met à jour les pages "
            "de notions."
        )
    )
    parser.add_argument(
        "--serve",
        action="store_true",
        help="lance « mkdocs serve » après la publication",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print(f"Source : {SOURCE_ROOT}")
    print(f"Docs   : {DOCS_ROOT}")

    try:
        report = publish(SOURCE_ROOT, DOCS_ROOT)
    except (FileNotFoundError, OSError, ValueError) as error:
        print(f"\nERREUR : {error}")
        return 1

    display_report(report, PROJECT_ROOT)

    if not args.serve:
        return 0

    print("\nLancement de mkdocs serve…")
    try:
        completed = subprocess.run(
            ["mkdocs", "serve"],
            cwd=PROJECT_ROOT,
            check=False,
        )
    except FileNotFoundError:
        print("ERREUR : la commande « mkdocs » est introuvable.")
        return 127
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
