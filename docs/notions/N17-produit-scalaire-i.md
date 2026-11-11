---
title: Produit scalaire I
description: Cours et exercices de Première spécialité pour introduire le produit scalaire, les projections et les coordonnées.
---

# N17 — Produit scalaire I

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N16-trigonometrie/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N16 — Trigonométrie</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N18-produit-scalaire-ii/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N18 — Produit scalaire II</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

Le produit scalaire permet de calculer avec les longueurs, les angles et l’orthogonalité. Cette première partie introduit les définitions, la projection et les expressions en coordonnées. Elle donne une méthode efficace pour traiter des configurations géométriques.

## Objectifs

!!! objectifs ""

    - Calculer un produit scalaire avec une formule adaptée.
    - Utiliser projection et coordonnées.
    - Reconnaître ou prouver une orthogonalité.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N17 — Produit scalaire I](../cours/COURS_N17_PRODUIT_SCALAIRE_I.pdf)
- [TD N17 — Produit scalaire I](../td/TD_N17_PRODUIT_SCALAIRE_I.pdf)
- [Automatismes N17 — Produit scalaire I](../automatismes/AUTOMATISMES_N17_PRODUIT_SCALAIRE_I.pdf)
<!-- AUTO-DOCS:END -->

<!-- AUTOMATISMES-WEB:START -->
- ⚡ [Automatismes N17 en ligne : énoncés, corrigés et QCM interactif](../automatismes/automatismes-N17-produit-scalaire-i.md)
<!-- AUTOMATISMES-WEB:END -->

## Notions essentielles

!!! essentiel ""

    Le produit scalaire de deux vecteurs `u⃗` et `v⃗` est un nombre réel, noté `u⃗·v⃗` — pas un vecteur. Lorsque `u⃗` et `v⃗` sont non nuls : `u⃗·v⃗>0` si l'angle entre eux est aigu, `u⃗·v⃗=0` si l'angle est droit, `u⃗·v⃗<0` si l'angle est obtus.

    Avec un angle `θ` entre `0` et `π` : `u⃗·v⃗ = ‖u⃗‖ × ‖v⃗‖ × cos θ`.

    Dans un repère **orthonormé**, si `u⃗(x ; y)` et `v⃗(x′ ; y′)`, alors `u⃗·v⃗ = xx′+yy′`.

    Deux vecteurs `u⃗` et `v⃗` sont orthogonaux si et seulement si `u⃗·v⃗=0`. Deux droites de vecteurs directeurs `u⃗` et `v⃗` sont perpendiculaires si et seulement si `u⃗·v⃗=0`.

## Exemple

!!! exemple ""

    Soient `u⃗(3 ; -2)` et `v⃗(5 ; 4)`, dans un repère orthonormé :

    `u⃗·v⃗ = 3×5 + (-2)×4 = 15-8 = 7`

## Repère historique — Pourquoi tenir compte de la direction dans un calcul ?

!!! historique ""

    Hermann Grassmann, *Ausdehnungslehre*, 1844
    {: .frise data-annee="1844" }

    Au XIXe siècle, plusieurs mathématiciens développent des calculs portant sur des grandeurs orientées. En 1844, Hermann Grassmann publie son *Ausdehnungslehre*, qui organise algébriquement des objets géométriques et leurs opérations. Ses travaux constituent une étape importante de l’histoire du calcul vectoriel ; ils ne se confondent pas avec la présentation scolaire actuelle du produit scalaire.

    **Le lien avec le cours :** multiplier seulement deux longueurs ne suffit pas à tenir compte de la direction des vecteurs. Le produit scalaire introduit le cosinus de leur angle : pour deux vecteurs de normes 3 et 4, il vaut 12 s’ils ont même direction et même sens, 0 s’ils sont perpendiculaires et −12 s’ils sont de sens opposés.

    La projection permet de comprendre ces résultats : seule la composante d’un vecteur dans la direction de l’autre intervient. Dans un repère orthonormé, la formule `xx′ + yy′` traduit cette information géométrique en un calcul sur les coordonnées. Le résultat est un nombre réel, dont le signe renseigne sur l’angle.

    *Source : [MacTutor, université de St Andrews — Hermann Grassmann](https://mathshistory.st-andrews.ac.uk/Biographies/Grassmann/) (en anglais).*

## Voir aussi

- PRÉREQUIS : [N04](N04-reperages-vecteurs.md) (Les vecteurs sont le langage de base.)
- PROLONGEMENT : [N18](N18-produit-scalaire-ii.md) (La suite développe identités et problèmes.)
