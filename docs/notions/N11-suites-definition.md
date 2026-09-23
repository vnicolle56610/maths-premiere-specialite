---
title: "Suites : définition et premiers raisonnements"
description: Cours et exercices de Première spécialité pour définir une suite, calculer des termes et raisonner par récurrence simple.
---

# N11 — Suites : définition et premiers raisonnements

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N10-variations-extremums/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N10 — Variations et extremums</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N12-suites-arithmetiques-geometriiques/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N12 — Suites arithmétiques et géométriques</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

Les suites décrivent des phénomènes discrets, étape par étape. Cette notion introduit les définitions explicites ou récurrentes, le calcul de termes et les premiers raisonnements sur le sens de variation. Elle prépare les suites arithmétiques, géométriques et les modèles discrets.

## Objectifs

- Calculer des termes d’une suite.
- Passer entre définition explicite et récurrente simple.
- Étudier les premières propriétés d’une suite.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N11 — Suites : définition et premiers raisonnements](../cours/COURS_N11_SUITES_DEFINITION.pdf)
- [TD N11 — Suites : définition et premiers raisonnements](../td/TD_N11_SUITES_DEFINITION.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Une suite numérique associe à chaque rang `n` un nombre noté `uₙ` ; on note la suite `(uₙ)`. Dans l'écriture `uₙ`, `n` est le rang et `uₙ` le terme de rang `n` ; le premier terme peut être `u₀` ou `u₁` selon l'énoncé.

Une suite est définie par une **formule explicite** lorsque `uₙ` est donné directement en fonction de `n` : on peut alors calculer un terme sans connaître les précédents.

Une suite est définie **par récurrence** lorsqu'on donne un terme initial et une relation permettant de calculer chaque terme à partir du précédent, par exemple `u₀` et `uₙ₊₁=2uₙ+3`. Sans terme initial, la suite n'est pas entièrement déterminée.

Une suite `(uₙ)` peut être représentée par les points de coordonnées `(n ; uₙ)` : les abscisses étant des entiers, on obtient un nuage de points, pas une courbe continue.

## Exemple

Soit la suite définie pour tout `n∈ℕ` par `uₙ=2n²-3n+1`.

`u₂ = 2×4 - 3×2 + 1 = 3` et `u₁₀ = 2×100 - 3×10 + 1 = 171`

Avec une formule explicite, on calcule directement `u₁₀` sans passer par tous les termes précédents.

## Voir aussi

- PROLONGEMENT : [N12](N12-suites-arithmetiques-geometriiques.md) (Les suites usuelles donnent des modèles rapides.)
