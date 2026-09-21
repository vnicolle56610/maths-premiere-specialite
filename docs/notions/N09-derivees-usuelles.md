---
title: Dérivées usuelles
description: Cours et exercices de Première spécialité pour calculer les dérivées des fonctions de référence.
---

# N09 — Dérivées usuelles

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N08-nombre-derive-derivation/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N08 — Nombre dérivé et dérivation</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N10-variations-extremums/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N10 — Variations et extremums</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

Les dérivées usuelles fournissent une boîte à outils pour étudier rapidement une fonction. Les ressources consolident les formules, les combinaisons simples et les erreurs classiques. Elles préparent l’étude systématique des variations et des extremums.

## Objectifs

- Connaître les dérivées des fonctions de référence.
- Dériver une somme, un produit par une constante ou une expression simple.
- Préparer l’étude du signe de la dérivée.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N09 — Dérivées usuelles](../cours/COURS_N09_DERIVEES_USUELLES.pdf)
- [TD N09 — Dérivées usuelles](../td/TD_N09_DERIVEES_USUELLES.pdf)
- [Automatismes N09 — Dérivées usuelles](../automatismes/AUTOMATISMES_N09_DERIVEES_USUELLES.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Si `f` est dérivable en tout réel d'un intervalle `I`, la fonction qui à `x` associe `f′(x)` s'appelle la fonction dérivée de `f`, notée `f′`.

Dérivées usuelles : une constante a pour dérivée `0` ; `(x)′=1` ; `(x²)′=2x` ; `(x³)′=3x²` ; `(xⁿ)′=nxⁿ⁻¹` là où `xⁿ` est définie ; `(1/x)′=-1/x²` sur `ℝ*` ; `(√x)′=1/(2√x)` sur `]0 ; +∞[`.

Pour deux fonctions dérivables `u` et `v` et un réel `k` : `(u+v)′=u′+v′`, `(ku)′=ku′`, `(uv)′=u′v+uv′`, et si `v` ne s'annule pas, `(u/v)′=(u′v-uv′)/v²`.

Pour une fonction composée avec une fonction affine, `f(x)=g(ax+b)` a pour dérivée `f′(x)=a×g′(ax+b)`.

## Exemple

Pour `g(x)=x²(3x-1)`, on pose `u(x)=x²` et `v(x)=3x-1`, donc `u′(x)=2x` et `v′(x)=3`. Avec `(uv)′=u′v+uv′` :

`g′(x) = 2x(3x-1) + 3x² = 9x² - 2x`

## Voir aussi

- PRÉREQUIS : [N08](N08-nombre-derive-derivation.md) (Le sens de la dérivée vient du nombre dérivé.)
- PROLONGEMENT : [N10](N10-variations-extremums.md) (Les variations reposent sur le signe de la dérivée.)
