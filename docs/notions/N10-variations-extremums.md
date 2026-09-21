---
title: Variations et extremums
description: Cours et exercices de Première spécialité pour étudier les variations d’une fonction avec la dérivée.
---

# N10 — Variations et extremums

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N09-derivees-usuelles/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N09 — Dérivées usuelles</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N11-suites-definition/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N11 — Suites : définition et premiers raisonnements</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

L’étude des variations met la dérivée au service de la résolution de problèmes. On cherche le signe de la dérivée, on construit un tableau de variations et on identifie des extremums. Cette méthode relie calcul formel, lecture graphique et optimisation.

## Objectifs

- Étudier le signe d’une dérivée.
- Construire et exploiter un tableau de variations.
- Déterminer un maximum ou un minimum.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N10 — Variations et extremums](../cours/COURS_N10_VARIATIONS_EXTREMUMS.pdf)
- [TD N10 — Variations et extremums](../td/TD_N10_VARIATIONS_EXTREMUMS.pdf)
- [Automatismes N10 — Variations et extremums](../automatismes/AUTOMATISMES_N10_VARIATIONS_EXTREMUMS.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Soit `f` une fonction dérivable sur un intervalle `I`. Si `f′(x)>0` sur `I`, alors `f` est strictement croissante sur `I`. Si `f′(x)<0` sur `I`, alors `f` est strictement décroissante sur `I`. Si `f′(x)=0` sur `I`, alors `f` est constante sur `I`.

Pour étudier les variations de `f`, on calcule `f′(x)`, on résout `f′(x)=0` et on étudie le signe de `f′`, puis on traduit ce signe dans un tableau de variations.

`f` admet un maximum `M` sur `I` lorsque `f(x)⩽M` pour tout `x` de `I` ; elle admet un minimum `m` lorsque `f(x)⩾m` pour tout `x` de `I`. Si `f` est dérivable et admet un extremum local en un point intérieur `a`, alors `f′(a)=0` — mais cette condition seule ne suffit pas à garantir un extremum : il faut regarder le signe de `f′` de part et d'autre de `a`. Si `f′` change de signe en `a`, `f` admet un extremum local en `a`.

## Exemple

Étudions `f(x)=x³-3x+1` sur `[-3 ; 3]`. On a `f′(x)=3x²-3=3(x-1)(x+1)`, donc `f′(x)=0` pour `x=-1` ou `x=1`.

Avec `f(-3)=-17`, `f(-1)=3`, `f(1)=-1` et `f(3)=19`, le tableau de variations montre que `f` admet un maximum local égal à `3` en `x=-1`, puis un minimum local égal à `-1` en `x=1`.

## Voir aussi

- PRÉREQUIS : [N09](N09-derivees-usuelles.md) (Les dérivées usuelles alimentent l’étude.)
- PROLONGEMENT : [N20](N20-fonction-exponentielle.md) (L’exponentielle sera étudiée avec les mêmes outils.)
