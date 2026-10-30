---
title: Indépendance et arbres
description: Cours et exercices de Première spécialité pour reconnaître l’indépendance et exploiter des arbres de probabilités.
---

# N23 — Indépendance et arbres

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N22-probabilites-conditionnelles/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N22 — Probabilités conditionnelles</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N24-variables-aleatoires-esperance/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N24 — Variables aléatoires et espérance</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

L’indépendance donne un critère pour simplifier certains calculs de probabilités. On apprend à la reconnaître, à la tester et à l’utiliser dans des arbres ou des tableaux. Les situations demandent de rester attentif au sens des événements.

## Objectifs

- Tester l’indépendance de deux événements.
- Utiliser un arbre de probabilités de façon structurée.
- Interpréter les résultats dans le contexte.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N23 — Indépendance et arbres](../cours/COURS_N23_INDEPENDANCE_ARBRES.pdf)
- [TD N23 — Indépendance et arbres](../td/TD_N23_INDEPENDANCE_ARBRES.pdf)
- [Automatismes N23 — Indépendance et arbres](../automatismes/AUTOMATISMES_N23_INDEPENDANCE_ARBRES.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Deux événements `A` et `B` (avec `P(A)>0`) sont **indépendants** lorsque `P_A(B)=P(B)` : savoir que `A` est réalisé ne change pas la probabilité de `B`. Critère pratique : `A` et `B` sont indépendants si et seulement si `P(A∩B) = P(A)×P(B)`.

Deux événements indépendants ne sont pas incompatibles : ce sont deux notions différentes. Si `A` et `B` sont indépendants, alors `A` et `B̄` le sont aussi (de même pour `Ā` et `B`, `Ā` et `B̄`).

Une succession d'épreuves est **indépendante** lorsque le résultat de l'une ne modifie pas le modèle probabiliste des suivantes : dans l'arbre, les sous-arbres d'une même épreuve sont identiques. Avec remise, l'indépendance est souvent un modèle adapté ; sans remise, généralement pas.

Dans une répétition indépendante de `n` épreuves de Bernoulli de paramètre `p`, un chemin avec `k` succès a pour probabilité `p^k×(1-p)^(n-k)`, et `P(au moins un succès) = 1-(1-p)^n`.

## Exemple

Si `P(A)=0,4`, `P(B)=0,3` et `P(A∩B)=0,12` :

`P(A)×P(B) = 0,4×0,3 = 0,12 = P(A∩B)`, donc `A` et `B` sont indépendants.

## Repère historique — Pourquoi répéter un lancer change-t-il les chances de gagner ?

Dans leurs échanges de 1654, Pascal et Fermat abordent des problèmes de jeux de hasard, dont celui de l’apparition d’un double six avec deux dés. Pour comprendre ces situations, il faut tenir compte de toutes les issues possibles et de la répétition des épreuves, plutôt que multiplier directement une probabilité par un nombre de tentatives.

**Le lien avec le cours :** dans un modèle actuel avec deux dés équilibrés et indépendants, la probabilité d’un double six à un lancer est `1/36`. Pour `n` lancers indépendants, la probabilité de n’obtenir aucun double six vaut `(35/36)^n`. Celle d’en obtenir au moins un vaut donc `1 − (35/36)^n`.

Cette formule combine le passage à l’événement contraire et l’indépendance. Les branches correspondant à l’échec gardent la même probabilité à chaque étape. L’indépendance signifie que les résultats passés ne modifient pas les probabilités du lancer suivant ; une longue série d’échecs ne rend donc pas le prochain double six plus probable.

*Source : [Bibliothèque de l’ETH Zurich — From games of chance to probability theory](https://library.ethz.ch/en/collections-and-archives/platforms/virtual-exhibitions/Its-all-math-and-games/game-types/from-games-of-chance-to-probability-theory.html) (en anglais).*

## Voir aussi

- PRÉREQUIS : [N22](N22-probabilites-conditionnelles.md) (Les probabilités conditionnelles donnent les formules.)
