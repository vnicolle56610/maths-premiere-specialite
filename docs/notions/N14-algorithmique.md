---
title: Algorithmique
description: Cours et exercices de Première spécialité pour écrire, lire et adapter des algorithmes mathématiques.
---

# N14 — Algorithmique

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N13-sommes-modeles-discrets/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N13 — Sommes et modèles discrets</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N15-droites-equations/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N15 — Droites et équations</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

L’algorithmique rend les raisonnements exécutables étape par étape. Les exercices portent sur variables, boucles, conditions et simulations, notamment autour des suites. L’objectif est de comprendre un programme court et de l’utiliser comme outil mathématique.

## Objectifs

- Lire un algorithme simple et prévoir sa sortie.
- Utiliser variables, conditions et boucles.
- Relier un programme à une situation mathématique.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N14 — Algorithmique](../cours/COURS_N14_ALGORITHMIQUE.pdf)
- [TD N14 — Algorithmique](../td/TD_N14_ALGORITHMIQUE.pdf)
- [Automatismes N14 — Algorithmique](../automatismes/AUTOMATISMES_N14_ALGORITHMIQUE.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

En Python, l'instruction `=` ne signifie pas « est égal à » comme en mathématiques : c'est une **affectation**, qui donne une valeur à une variable. Une variable est un nom qui désigne une valeur stockée en mémoire, valeur qui peut changer au cours de l'exécution.

Une **boucle bornée** (`for`) répète un bloc d'instructions un nombre connu de fois : `range(n)` produit `n` répétitions, avec les valeurs `0, 1, …, n-1`.

Une **boucle conditionnelle** (`while`) répète un bloc tant qu'une condition reste vraie ; elle est utile pour chercher un seuil, quand on ne connaît pas à l'avance le nombre d'étapes nécessaires. La condition est testée avant chaque répétition.

Une **fonction Python**, définie avec `def`, est un bloc d'instructions nommé qui peut recevoir des paramètres et renvoyer un résultat avec `return`.

## Exemple

On considère la suite définie par `u₀=500` et `uₙ₊₁=1,12×uₙ`. Le programme suivant calcule `u₈` :

```
u = 500
for k in range(8):
    u = 1.12*u
print(u)
```

La boucle est exécutée `8` fois : on passe de `u₀` à `u₈`.

## Voir aussi

- PRÉREQUIS : [N13](N13-sommes-modeles-discrets.md) (Les modèles discrets se programment naturellement.)
