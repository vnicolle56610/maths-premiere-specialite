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

!!! objectifs ""

    - Connaître les dérivées des fonctions de référence.
    - Dériver une somme, un produit par une constante ou une expression simple.
    - Préparer l’étude du signe de la dérivée.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N09 — Dérivées usuelles](../cours/COURS_N09_DERIVEES_USUELLES.pdf)
- [TD N09 — Dérivées usuelles](../td/TD_N09_DERIVEES_USUELLES.pdf)
<!-- AUTO-DOCS:END -->

<!-- AUTOMATISMES-WEB:START -->
- ⚡ [Automatismes N09 en ligne : énoncés, corrigés et QCM interactif](../automatismes/automatismes-N09-derivees-usuelles.md)
<!-- AUTOMATISMES-WEB:END -->

## Notions essentielles

!!! essentiel ""

    Si `f` est dérivable en tout réel d'un intervalle `I`, la fonction qui à `x` associe `f′(x)` s'appelle la fonction dérivée de `f`, notée `f′`.

    Dérivées usuelles : une constante a pour dérivée `0` ; `(x)′=1` ; `(x²)′=2x` ; `(x³)′=3x²` ; `(xⁿ)′=nxⁿ⁻¹` là où `xⁿ` est définie ; `(1/x)′=-1/x²` sur `ℝ*` ; `(√x)′=1/(2√x)` sur `]0 ; +∞[`.

    Pour deux fonctions dérivables `u` et `v` et un réel `k` : `(u+v)′=u′+v′`, `(ku)′=ku′`, `(uv)′=u′v+uv′`, et si `v` ne s'annule pas, `(u/v)′=(u′v-uv′)/v²`.

    Pour une fonction composée avec une fonction affine, `f(x)=g(ax+b)` a pour dérivée `f′(x)=a×g′(ax+b)`.

## Exemple

!!! exemple ""

    Pour `g(x)=x²(3x-1)`, on pose `u(x)=x²` et `v(x)=3x-1`, donc `u′(x)=2x` et `v′(x)=3`. Avec `(uv)′=u′v+uv′` :

    `g′(x) = 2x(3x-1) + 3x² = 9x² - 2x`

## Repère historique — Comment la dérivation est-elle devenue un calcul ?

!!! historique ""

    Gottfried Wilhelm Leibniz, *Acta Eruditorum*, 1684
    {: .frise data-annee="1684" }

    En 1684, Gottfried Wilhelm Leibniz publie dans les *Acta Eruditorum* un article exposant son calcul différentiel. Il y présente notamment des règles pour les puissances, les produits et les quotients, avec la notation `d` des différentielles. Ces règles permettent d’organiser les calculs et de traiter de nombreuses expressions à partir de quelques opérations.

    Ce langage historique ne correspond pas encore à notre définition de la dérivée par une limite. Il contribue cependant à faire de la recherche des tangentes une méthode de calcul réutilisable.

    **Le lien avec le cours :** les formules usuelles évitent de reprendre un taux de variation pour chaque nouvelle expression. En notation actuelle, pour `g(x) = x²(3x − 1)`, la règle du produit donne `g′(x) = 2x(3x − 1) + 3x²`. On peut vérifier le résultat en développant d’abord `g(x) = 3x³ − x²`, puis en dérivant terme à terme : les deux chemins conduisent à `9x² − 2x`.

    *Source : [MacTutor, université de St Andrews — Gottfried Wilhelm von Leibniz](https://mathshistory.st-andrews.ac.uk/Biographies/Leibniz/) (en anglais).*

## Voir aussi

- PRÉREQUIS : [N08](N08-nombre-derive-derivation.md) (Le sens de la dérivée vient du nombre dérivé.)
- PROLONGEMENT : [N10](N10-variations-extremums.md) (Les variations reposent sur le signe de la dérivée.)
