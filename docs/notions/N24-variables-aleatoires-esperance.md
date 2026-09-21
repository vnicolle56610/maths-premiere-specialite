---
title: Variables aléatoires et espérance
description: Cours et exercices de Première spécialité pour définir une variable aléatoire, sa loi et son espérance.
---

# N24 — Variables aléatoires et espérance

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N23-independance-arbres/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N23 — Indépendance et arbres</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N25-syntheses-automatismes/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N25 — Synthèses et automatismes</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

Les variables aléatoires transforment une expérience en valeurs numériques. Cette notion installe la loi de probabilité, l’espérance et l’interprétation d’un gain moyen. Elle sert à modéliser des jeux, décisions et situations aléatoires simples.

## Objectifs

- Définir une variable aléatoire et sa loi.
- Calculer et interpréter une espérance.
- Résoudre un problème de décision avec un modèle probabiliste.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N24 — Variables aléatoires et espérance](../cours/COURS_N24_VARIABLES_ALEATOIRES_ESPERANCE.pdf)
- [TD N24 — Variables aléatoires et espérance](../td/TD_N24_VARIABLES_ALEATOIRES_ESPERANCE.pdf)
- [Automatismes N24 — Variables aléatoires et espérance](../automatismes/AUTOMATISMES_N24_VARIABLES_ALEATOIRES_ESPERANCE.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Une **variable aléatoire réelle** `X` est une fonction qui associe un nombre réel à chaque issue d'une expérience aléatoire. Si `X` prend les valeurs `x₁,...,xₙ` avec les probabilités `p₁,...,pₙ`, sa **loi de probabilité** vérifie `p₁+p₂+...+pₙ=1`.

L'**espérance** de `X` est `E(X) = x₁p₁+x₂p₂+...+xₙpₙ`. Ce n'est pas forcément une valeur prise par `X` : elle s'interprète comme une moyenne à long terme, jamais comme un résultat garanti pour une seule expérience. Pour tous réels `a` et `b` : `E(aX+b) = a×E(X)+b`.

La **variance** de `X` est `V(X) = Σ pᵢ(xᵢ-E(X))²`, et son **écart-type** est `σ(X)=√V(X)`. La formule de König-Huygens donne `V(X) = E(X²) - (E(X))²`, plus pratique en calcul. Une variance n'est jamais négative.

Lorsqu'on répète l'expérience un grand nombre de fois, la moyenne observée sur l'échantillon se rapproche de `E(X)`, sans jamais lui être exactement égale sur un échantillon fini.

## Exemple

Une variable aléatoire `X` prend les valeurs `-1`, `1` et `4` avec les probabilités `0,5`, `0,3` et `0,2`.

`E(X) = (-1)×0,5 + 1×0,3 + 4×0,2 = -0,5+0,3+0,8 = 0,6`

En moyenne, sur un grand nombre de répétitions, `X` vaut `0,6`.

## Voir aussi

- PRÉREQUIS : [N22](N22-probabilites-conditionnelles.md) (Les probabilités de base alimentent la loi.)
