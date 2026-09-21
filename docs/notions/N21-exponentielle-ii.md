---
title: "Exponentielle II : modèles"
description: Cours et exercices de Première spécialité pour utiliser l’exponentielle dans des modèles et équations.
---

# N21 — Exponentielle II : modèles

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N20-fonction-exponentielle/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N20 — Fonction exponentielle I</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N22-probabilites-conditionnelles/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N22 — Probabilités conditionnelles</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

Cette notion prolonge l’exponentielle dans les modèles d’évolution. Les ressources travaillent les équations, les inéquations simples, les variations et l’interprétation de situations concrètes. L’objectif est de relier calcul, graphique et modélisation.

## Objectifs

- Résoudre des équations simples avec l’exponentielle.
- Étudier des variations impliquant l’exponentielle.
- Interpréter un modèle exponentiel.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N21 — Exponentielle II : modèles](../cours/COURS_N21_EXPONENTIELLE_II.pdf)
- [TD N21 — Exponentielle II : modèles](../td/TD_N21_EXPONENTIELLE_II.pdf)
- [Automatismes N21 — Exponentielle II : modèles](../automatismes/AUTOMATISMES_N21_EXPONENTIELLE_II_MODELES.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Un **modèle discret** d'évolution exponentielle s'écrit `u_n=C×q^n`, où `C` est la valeur initiale et `q>0` le coefficient multiplicateur à chaque étape. Une hausse de `t %` par étape correspond à `q=1+t/100` ; une baisse à `q=1-t/100`.

Un **modèle continu** est une fonction `f(t)=C×e^(kt)`, avec `C>0`. Si `k>0`, `f` est croissante ; si `k<0`, `f` est décroissante. On a toujours `f′(t) = k×f(t)` : la vitesse d'évolution est proportionnelle à la quantité présente.

Si `q>0` et si `k` vérifie `e^k=q`, alors pour tout entier `n`, `q^n=e^(kn)` : la suite `u_n=C×q^n` s'écrit aussi `u_n=C×e^(kn)`, ce qui relie modèle discret et modèle continu.

Pour chercher un seuil, on calcule les termes ou valeurs successives jusqu'à dépasser (ou atteindre) le seuil fixé — en distinguant bien une condition stricte d'une condition large.

## Exemple

Une population de bactéries est modélisée par `N(t)=500×e^(0,18t)`, `t` en heures.

On a `N(0)=500`, et `N′(t)=0,18×N(t)` : la vitesse instantanée d'évolution est proportionnelle à la population présente.

## Voir aussi

- PRÉREQUIS : [N20](N20-fonction-exponentielle.md) (Les propriétés de base sont indispensables.)
