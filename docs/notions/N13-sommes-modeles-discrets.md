---
title: Sommes et modèles discrets
description: Cours et exercices de Première spécialité pour calculer des sommes et exploiter des modèles discrets.
---

# N13 — Sommes et modèles discrets

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N12-suites-arithmetiques-geometriiques/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N12 — Suites arithmétiques et géométriques</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N14-algorithmique/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N14 — Algorithmique</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

Les sommes permettent d’additionner les termes d’une suite et de modéliser des accumulations. Cette notion travaille les formules utiles, les interprétations et les choix de modèle. Elle prépare aussi le dialogue avec l’algorithmique.

## Objectifs

- Calculer une somme de termes consécutifs.
- Choisir une formule adaptée au type de suite.
- Interpréter une accumulation dans un modèle discret.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N13 — Sommes et modèles discrets](../cours/COURS_N13_SOMMES_MODELES_DISCRETS.pdf)
- [TD N13 — Sommes et modèles discrets](../td/TD_N13_SOMMES_MODELES_DISCRETS.pdf)
- [Automatismes N13 — Sommes et modèles discrets](../automatismes/AUTOMATISMES_N13_SOMMES_MODELES_DISCRETS.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Une somme cumulée additionne plusieurs termes consécutifs d'une suite. La notation `Σ` (sigma) `Σₖ₌₀ⁿ uₖ` se lit « somme des `uₖ`, pour `k` allant de `0` à `n` » et signifie `u₀+u₁+⋯+uₙ`.

Pour une suite **arithmétique**, la somme de termes consécutifs vaut : nombre de termes × (premier terme + dernier terme) / 2. En particulier, `u₀+u₁+⋯+uₙ = (n+1) × (u₀+uₙ)/2`.

Pour une suite **géométrique** de premier terme `u₀` et de raison `q≠1` : `u₀+u₁+⋯+uₙ = u₀ × (1-qⁿ⁺¹)/(1-q)`.

Un terme isolé `uₙ` est une valeur ; une somme `u₀+⋯+uₙ` est un total : il ne faut pas confondre les deux.

## Exemple

Calculons `3+6+12+24+48`, une somme géométrique de premier terme `3`, de raison `2`, avec `5` termes :

`3+6+12+24+48 = 3 × (1-2⁵)/(1-2) = 3×31 = 93`

## Voir aussi

- PRÉREQUIS : [N12](N12-suites-arithmetiques-geometriiques.md) (Les suites usuelles donnent les formules de base.)
- PROLONGEMENT : [N14](N14-algorithmique.md) (Les algorithmes permettent de simuler ces modèles.)
