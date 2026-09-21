---
title: Géométrie repérée
description: Cours et exercices de Première spécialité pour résoudre des problèmes dans un repère avec droites, cercles et distances.
---

# N19 — Géométrie repérée

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N18-produit-scalaire-ii/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N18 — Produit scalaire II</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N20-fonction-exponentielle/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N20 — Fonction exponentielle I</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

La géométrie repérée rassemble les outils de coordonnées, droites, distances et produit scalaire. Les exercices demandent de choisir une représentation, de calculer avec précision et de conclure géométriquement. Cette synthèse prépare les problèmes mêlant plusieurs méthodes.

## Objectifs

- Modéliser une configuration dans un repère.
- Calculer distances, milieux, droites ou orthogonalités.
- Rédiger une conclusion géométrique à partir de calculs.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N19 — Géométrie repérée](../cours/COURS_N19_GEOMETRIE_REPEREE.pdf)
- [TD N19 — Géométrie repérée](../td/TD_N19_GEOMETRIE_REPEREE.pdf)
- [Automatismes N19 — Géométrie repérée](../automatismes/AUTOMATISMES_N19_GEOMETRIE_REPEREE.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Dans un repère orthonormé, si une droite `d` a pour équation `ax+by+c=0`, alors `n⃗(a ; b)` est un vecteur normal à `d`, et un point `M(x ; y)` appartient à `d` si et seulement si `ax+by+c=0`.

Le **projeté orthogonal** de `M` sur `d` est le point `H∈d` tel que `(MH)⊥d` — c'est aussi le point de `d` le plus proche de `M`.

Le cercle de centre `Ω(a ; b)` et de rayon `r>0` a pour équation `(x-a)²+(y-b)²=r²`. Une équation de la forme `x²+y²+αx+βy+γ=0` se ramène à cette forme en complétant les carrés ; l'ensemble n'est un cercle que si le carré du rayon obtenu est strictement positif.

Pour étudier une configuration dans un repère : identifier les objets (points, droites, cercles), choisir l'outil adapté (vecteurs, produit scalaire, équations, projection), effectuer les calculs, puis conclure géométriquement.

## Exemple

Le cercle de centre `Ω(3 ; -2)` et de rayon `4` a pour équation `(x-3)²+(y+2)²=16`.

Le point `A(7 ; -2)` appartient à ce cercle, car `(7-3)² + (-2+2)² = 16`.

## Voir aussi

- PRÉREQUIS : [N15](N15-droites-equations.md) (Les équations de droites sont fréquemment utilisées.)
- PRÉREQUIS : [N18](N18-produit-scalaire-ii.md) (Le produit scalaire complète les outils.)
