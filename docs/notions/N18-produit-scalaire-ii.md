---
title: Produit scalaire II
description: Cours et exercices de Première spécialité pour utiliser identités, théorème d’Al-Kashi et lieux de points.
---

# N18 — Produit scalaire II

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N17-produit-scalaire-i/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N17 — Produit scalaire I</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N19-geometrie-reperee/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N19 — Géométrie repérée</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

Cette seconde partie du produit scalaire développe les identités utiles et les applications aux problèmes. Les ressources mobilisent Al-Kashi, les calculs de longueurs, les angles et certains lieux de points. On apprend à choisir une formule selon la configuration.

## Objectifs

- Utiliser les identités du produit scalaire.
- Appliquer le théorème d’Al-Kashi.
- Résoudre des problèmes de géométrie avec un choix de formule.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N18 — Produit scalaire II](../cours/COURS_N18_PRODUIT_SCALAIRE_II.pdf)
- [TD N18 — Produit scalaire II](../td/TD_N18_PRODUIT_SCALAIRE_II.pdf)
- [Automatismes N18 — Produit scalaire II](../automatismes/AUTOMATISMES_N18_PRODUIT_SCALAIRE_II.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Pour tous vecteurs `u⃗` et `v⃗` : `‖u⃗+v⃗‖² = ‖u⃗‖² + 2×u⃗·v⃗ + ‖v⃗‖²` et `‖u⃗-v⃗‖² = ‖u⃗‖² - 2×u⃗·v⃗ + ‖v⃗‖²`.

Dans un triangle `ABC`, avec `a=BC`, `b=AC`, `c=AB`, la **formule d'Al-Kashi** généralise Pythagore : `BC² = AB² + AC² - 2×AB×AC×cos(Â)`. Elle permet aussi de calculer un angle à partir des trois longueurs : `cos(Â) = (AB²+AC²-BC²) / (2×AB×AC)`.

Pour deux points distincts `A` et `B`, l'ensemble des points `M` tels que `MA⃗·MB⃗=0` est le cercle de diamètre `[AB]` (`A` et `B` inclus) : cela revient à dire que le triangle `AMB` est rectangle en `M`.

## Exemple

Dans un triangle `ABC` avec `AB=6`, `AC=5` et `Â=60°` :

`BC² = 6² + 5² - 2×6×5×cos 60° = 36+25-60×0,5 = 31`, donc `BC = √31`.

## Voir aussi

- PRÉREQUIS : [N17](N17-produit-scalaire-i.md) (Les définitions du produit scalaire sont nécessaires.)
- PROLONGEMENT : [N19](N19-geometrie-reperee.md) (La géométrie repérée combine ces outils.)
