---
title: Suites arithmétiques et géométriques
description: Cours et exercices de Première spécialité sur les suites arithmétiques, géométriques et leurs modèles.
---

# N12 — Suites arithmétiques et géométriques

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N11-suites-definition/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N11 — Suites : définition et premiers raisonnements</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N13-sommes-modeles-discrets/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N13 — Sommes et modèles discrets</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

Les suites arithmétiques et géométriques modélisent des évolutions régulières. On apprend à reconnaître le type de suite, calculer un terme général et interpréter la raison. Ces modèles serviront ensuite pour les sommes, les algorithmes et les situations d’évolution.

## Objectifs

!!! objectifs ""

    - Identifier une suite arithmétique ou géométrique.
    - Calculer un terme général et une raison.
    - Interpréter un modèle discret dans un contexte.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N12 — Suites arithmétiques et géométriques](../cours/COURS_N12_SUITES_ARITHMETIQUES_GEOMETRIQUES.pdf)
- [TD N12 — Suites arithmétiques et géométriques](../td/TD_N12_SUITES_ARITHMETIQUES_GEOMETRIQUES.pdf)
- [Automatismes N12 — Suites arithmétiques et géométriques](../automatismes/AUTOMATISMES_N12_SUITES_ARITHMETIQUES_GEOMETRIQUES.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

!!! essentiel ""

    Une suite `(uₙ)` est **arithmétique** lorsqu'il existe un réel `r` tel que, pour tout rang `n`, `uₙ₊₁=uₙ+r` ; `r` est la raison. La différence entre deux termes consécutifs est alors constante. Si le premier terme est `u₀`, alors `uₙ=u₀+nr` pour tout `n`.

    Une suite `(uₙ)` est **géométrique** lorsqu'il existe un réel `q` tel que, pour tout rang `n`, `uₙ₊₁=q×uₙ` ; `q` est la raison. Si les termes sont non nuls, le quotient entre deux termes consécutifs est alors constant. Si le premier terme est `u₀`, alors `uₙ=u₀×qⁿ` pour tout `n`.

    Une évolution avec ajout constant se modélise par une suite arithmétique ; une évolution à taux fixe se modélise par une suite géométrique.

## Exemple

!!! exemple ""

    Soit `(uₙ)` arithmétique telle que `u₀=12` et `r=5`. Alors `uₙ=12+5n`, donc :

    `u₂₀ = 12 + 5×20 = 112`

## Repère historique — Que relie une addition régulière à une multiplication régulière ?

!!! historique ""

    Michael Stifel, *Arithmetica integra*, 1544
    {: .frise data-annee="1544" }

    Dans son *Arithmetica integra*, publiée en 1544, Michael Stifel met en correspondance les nombres `1, 2, 3, 4, 5…` et les puissances `2, 4, 8, 16, 32…`. Il prolonge aussi cette correspondance : 0 est associé à 1, puis −1 à la moitié et −2 au quart. Ce rapprochement entre progressions arithmétiques et géométriques constitue un jalon de l’histoire des logarithmes.

    **Le lien avec le cours :** en notation actuelle, limitons-nous aux rangs `n ≥ 0`. Les suites `aₙ = n` et `bₙ = 2ⁿ` sont respectivement arithmétique de raison 1 et géométrique de raison 2. Passer au rang suivant revient à ajouter 1 dans la première et à multiplier par 2 dans la seconde.

    La règle `2³ × 2⁴ = 2⁷` montre aussi qu’une multiplication de puissances correspond à une addition de leurs exposants. Pour reconnaître les deux modèles, on examine donc ce qui reste constant : la différence ou, lorsque les termes sont non nuls, le quotient de deux termes consécutifs.

    *Source : [MacTutor, université de St Andrews — Michael Stifel](https://mathshistory.st-andrews.ac.uk/Biographies/Stifel/) (en anglais).*

## Voir aussi

- PRÉREQUIS : [N11](N11-suites-definition.md) (Les définitions de suites sont nécessaires.)
- PROLONGEMENT : [N13](N13-sommes-modeles-discrets.md) (Les sommes exploitent ces suites particulières.)
