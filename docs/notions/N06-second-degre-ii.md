---
title: "Second degré II : racines, signe et discriminant"
description: Cours et exercices de Première spécialité pour résoudre des équations et inéquations du second degré.
---

# N06 — Second degré II : racines, signe et discriminant

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N05-second-degre-i/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N05 — Second degré I : fonction carré et forme canonique</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N07-taux-de-variation/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N07 — Taux de variation</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

Cette notion complète l’étude du second degré avec les racines, le discriminant, la factorisation et le signe. Les exercices conduisent à résoudre des équations, des inéquations et des problèmes. Le second degré devient alors un outil de modélisation et de décision.

## Objectifs

- Calculer un discriminant et interpréter les racines.
- Dresser et utiliser un tableau de signe.
- Résoudre des inéquations et problèmes du second degré.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N06 — Second degré (partie 1) : formes, racines, signe et discriminant (Partie 1 Formes Racines Signe Discriminant)](../cours/COURS_N06_PARTIE_1_FORMES_RACINES_SIGNE_DISCRIMINANT.pdf)
- [Cours N06 — Second degré (partie 2) : inéquations, optimisation et problèmes (Partie 2 Inequations Optimisation Problemes)](../cours/COURS_N06_PARTIE_2_INEQUATIONS_OPTIMISATION_PROBLEMES.pdf)
- [TD N06 — Second degré (partie 1) : formes, racines, signe et discriminant (Partie 1 Formes Racines Signe Discriminant)](../td/TD_N06_PARTIE_1_FORMES_RACINES_SIGNE_DISCRIMINANT.pdf)
- [TD N06 — Second degré (partie 2) : inéquations, optimisation et problèmes (Partie 2 Inequations Optimisation Problemes)](../td/TD_N06_PARTIE_2_INEQUATIONS_OPTIMISATION_PROBLEMES.pdf)
- [Automatismes N06 — Second degré (partie 1) : formes, racines, signe et discriminant (Partie 1 Formes Racines Signe Discriminant)](../automatismes/AUTOMATISMES_N06_PARTIE_1_FORMES_RACINES_SIGNE_DISCRIMINANT.pdf)
- [Automatismes N06 — Second degré (partie 2) : inéquations, optimisation et problèmes (Partie 2 Inequations Optimisation Problemes)](../automatismes/AUTOMATISMES_N06_PARTIE_2_INEQUATIONS_OPTIMISATION_PROBLEMES.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Pour `P(x)=ax²+bx+c`, avec `a≠0`, un réel `r` est une racine de `P` lorsque `P(r)=0`. Le discriminant `Δ=b²-4ac` donne le nombre de racines réelles :

- si `Δ>0`, deux racines distinctes `x₁` et `x₂` ;
- si `Δ=0`, une racine double `x₀=-b/2a` ;
- si `Δ<0`, aucune racine réelle.

Avec deux racines `x₁<x₂`, le trinôme est du signe de `a` à l'extérieur des racines et du signe opposé entre elles. Avec une racine double, il garde le signe de `a` et s'annule seulement en `x₀`. Sans racine réelle, il garde le signe de `a` sur `ℝ`.

Pour résoudre une inéquation du second degré, on ramène tout dans un membre, on détermine les racines ou une factorisation, puis on dresse le tableau de signes avant de conclure. Une racine appartient à l'ensemble des solutions pour `⩽` ou `⩾`, mais pas pour `<` ou `>`.

## Exemple

Résolvons `2x² - 5x - 3 = 0`. Ici `a=2`, `b=-5`, `c=-3`.

`Δ = (-5)² - 4×2×(-3) = 49`

Comme `Δ>0`, l'équation possède deux solutions :

`x₁ = (5-7)/4 = -0,5` et `x₂ = (5+7)/4 = 3`

Donc `S = {-0,5 ; 3}`.

## Voir aussi

- PRÉREQUIS : [N05](N05-second-degre-i.md) (La forme canonique éclaire la parabole.)
- PROLONGEMENT : [N10](N10-variations-extremums.md) (Les extremums seront repris avec les dérivées.)
