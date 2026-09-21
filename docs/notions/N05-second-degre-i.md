---
title: "Second degré I : fonction carré et forme canonique"
description: Cours et exercices de Première spécialité sur la fonction carré, les paraboles et la forme canonique.
---

# N05 — Second degré I : fonction carré et forme canonique

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N04-reperages-vecteurs/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N04 — Repérage et vecteurs</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N06-second-degre-ii/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N06 — Second degré II : racines, signe et discriminant</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

Le second degré commence par l’étude de la fonction carré et des paraboles. La forme canonique permet de lire un extremum et de comprendre le rôle des transformations algébriques. Cette étape prépare les racines, le discriminant, le signe et les problèmes d’optimisation.

## Objectifs

- Reconnaître et exploiter une forme canonique.
- Lire le sommet et les variations d’une parabole.
- Relier expression algébrique et représentation graphique.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N05 — Second degré I : fonction carré et forme canonique](../cours/COURS_N05_SECOND_DEGRE_I.pdf)
- [TD N05 — Second degré I : fonction carré et forme canonique](../td/TD_N05_SECOND_DEGRE_I.pdf)
- [Automatismes N05 — Second degré I : fonction carré et forme canonique](../automatismes/AUTOMATISMES_N05_SECOND_DEGRE_I.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

La fonction carré est définie sur `ℝ` par `f(x)=x²`. Sa courbe est une parabole de sommet `O(0 ; 0)`, symétrique par rapport à l'axe des ordonnées. Elle est décroissante sur `]-∞ ; 0]`, puis croissante sur `[0 ; +∞[`.

Une fonction de la forme `a(x-α)²+β`, avec `a≠0`, a pour courbe une parabole de sommet `S(α ; β)` et d'axe de symétrie la droite `x=α`. Si `a>0`, `f` admet un minimum égal à `β` ; si `a<0`, `f` admet un maximum égal à `β`.

L'écriture `a(x-α)²+β` s'appelle la forme canonique. Elle est la plus efficace pour lire un sommet ou un extremum, alors que la forme développée facilite le calcul d'images et la forme factorisée la lecture des zéros.

Pour transformer `x²+bx+c` en forme canonique, on utilise l'identité `x²+2px=(x+p)²-p²` : on fait apparaître le carré qui possède le même terme en `x`, puis on ajuste la constante.

## Exemple

Mettons `x²+6x+5` sous forme canonique.

`x²+6x+5 = (x+3)² - 9 + 5 = (x+3)² - 4`

La parabole a donc pour sommet `S(-3 ; -4)`, pour axe `x=-3`, et la fonction admet un minimum égal à `-4`.

## Voir aussi

- PRÉREQUIS : [N02](N02-calcul-algebrique-equations.md) (Les transformations algébriques sont centrales.)
- PROLONGEMENT : [N06](N06-second-degre-ii.md) (La suite traite racines, signe et discriminant.)
