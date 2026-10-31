---
title: Droites et équations
description: Cours et exercices de Première spécialité pour déterminer et exploiter des équations de droites.
---

# N15 — Droites et équations

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N14-algorithmique/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N14 — Algorithmique</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N16-trigonometrie/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N16 — Trigonométrie</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

Les équations de droites relient géométrie, calcul et fonctions affines. Cette notion travaille coefficients directeurs, vecteurs directeurs, intersections et appartenance à une droite. Elle prolonge le repérage avant la trigonométrie et le produit scalaire.

## Objectifs

!!! objectifs ""

    - Déterminer une équation de droite.
    - Utiliser coefficient directeur et vecteur directeur.
    - Calculer une intersection ou tester une appartenance.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N15 — Droites et équations](../cours/COURS_N15_DROITES_ET_EQUATIONS.pdf)
- [TD N15 — Droites et équations](../td/TD_N15_DROITES_ET_EQUATIONS.pdf)
- [Automatismes N15 — Droites et équations](../automatismes/AUTOMATISMES_N15_DROITES_ET_EQUATIONS.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

!!! essentiel ""

    Un vecteur non nul `u⃗` est un **vecteur directeur** d'une droite `d` lorsqu'il a la même direction que `d`. Si `A` et `B` sont deux points distincts de `d`, alors `AB⃗` est un vecteur directeur de `d`. Un point `M(x ; y)` appartient à la droite passant par `A(xA ; yA)` de vecteur directeur `u⃗(p ; q)` lorsque `p(y-yA) - q(x-xA) = 0`.

    Une **équation cartésienne** de droite est une équation de la forme `ax+by+c=0`, avec `(a ; b)≠(0 ; 0)` : un point appartient à la droite lorsque ses coordonnées vérifient cette équation.

    Si `d` a pour équation `ax+by+c=0`, un vecteur directeur de `d` est `(-b ; a)`, et un **vecteur normal** (perpendiculaire à `d`) est `(a ; b)`.

    Deux droites sont parallèles lorsque leurs vecteurs directeurs (ou leurs vecteurs normaux) sont colinéaires : pour `d:ax+by+c=0` et `d′:a′x+b′y+c′=0`, cela revient à `ab′-a′b=0`.

## Exemple

!!! exemple ""

    On considère `d : 2x - 3y + 4 = 0`.

    Pour `A(1 ; 2)` : `2×1 - 3×2 + 4 = 0`, donc `A∈d`.

    Pour `B(4 ; 3)` : `2×4 - 3×3 + 4 = 3`, donc `B∉d`.

## Repère historique — Comment une équation peut-elle décrire une droite ?

!!! historique ""

    Pierre de Fermat, Toulouse, XVIIe siècle
    {: .frise data-annee="1636" data-etiquette="v. 1636" }

    Au XVIIe siècle, Pierre de Fermat étudie les lieux géométriques : les ensembles de points qui satisfont une même condition. Dans son travail sur la géométrie analytique, il relie des équations à deux inconnues à des droites ou à des courbes. Son dispositif utilise un axe et des longueurs variables ; il diffère du repère à deux axes fixes utilisé aujourd’hui.

    **Le lien avec le cours :** en notation actuelle, l’équation `2x − 3y + 4 = 0` décrit tous les points dont les coordonnées vérifient cette relation. Elle peut se réécrire `y = (2/3)x + 4/3`, ce qui fait apparaître le coefficient directeur et l’ordonnée à l’origine.

    Ces deux écritures décrivent la même droite. La forme cartésienne permet aussi de traiter les droites verticales, comme `x = 2`, qui ne possèdent pas d’équation de la forme `y = mx + p`. Une équation est ainsi un outil pour caractériser un ensemble de points et calculer ses intersections avec d’autres figures.

    *Source : [Dictionary of Scientific Biography — Pierre de Fermat, texte hébergé par l’université de St Andrews](https://mathshistory.st-andrews.ac.uk/DSB/Fermat.pdf) (PDF en anglais).*

## Voir aussi

- PRÉREQUIS : [N04](N04-reperages-vecteurs.md) (Le repérage fournit les coordonnées et vecteurs.)
- PROLONGEMENT : [N17](N17-produit-scalaire-i.md) (Le produit scalaire enrichit la géométrie repérée.)
