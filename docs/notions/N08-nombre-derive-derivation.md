---
title: Nombre dérivé et dérivation
description: Cours et exercices de Première spécialité pour introduire nombre dérivé, tangente et dérivation.
---

# N08 — Nombre dérivé et dérivation

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N07-taux-de-variation/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N07 — Taux de variation</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N09-derivees-usuelles/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N09 — Dérivées usuelles</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

La dérivation permet de décrire une variation instantanée. Cette notion introduit le nombre dérivé, la tangente et les premières règles de calcul. Elle donne les outils qui serviront à étudier les variations, les extremums et les modèles fonctionnels.

## Objectifs

- Calculer ou lire un nombre dérivé.
- Relier nombre dérivé et tangente à une courbe.
- Utiliser les premières règles de dérivation.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N08 — Nombre dérivé et dérivation](../cours/COURS_N08_NOMBRE_DERIVE_DERIVATION.pdf)
- [TD N08 — Nombre dérivé et dérivation](../td/TD_N08_NOMBRE_DERIVE_DERIVATION.pdf)
- [Automatismes N08 — Nombre dérivé et dérivation](../automatismes/AUTOMATISMES_N08_NOMBRE_DERIVE_DERIVATION.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Pour `h≠0`, le taux de variation de `f` entre `a` et `a+h` est `(f(a+h)-f(a)) / h`. Si ce quotient se rapproche d'un même nombre réel lorsque `h` se rapproche de `0`, on dit que `f` est dérivable en `a`, et ce nombre est le nombre dérivé de `f` en `a`, noté `f′(a)`.

Graphiquement, `f′(a)` est le coefficient directeur de la tangente à la courbe au point d'abscisse `a`. Cette tangente a pour équation `y = f′(a)(x-a) + f(a)`.

Le nombre dérivé peut ne pas exister : si les taux ne se stabilisent pas autour d'une même valeur lorsque `h` se rapproche de `0` (angle, pointe, pente verticale), la fonction n'est pas dérivable en ce point.

## Exemple

Pour `f(x)=x²`, calculons le nombre dérivé en `2`. On a `f(2)=4` et `f(2+h)=4+4h+h²`, donc pour `h≠0` :

`(f(2+h)-f(2)) / h = (4h+h²) / h = 4+h`

Lorsque `h` se rapproche de `0`, `4+h` se rapproche de `4`. Donc `f′(2)=4`, et la tangente au point d'abscisse `2` a pour équation `y = 4(x-2)+4`, soit `y = 4x-4`.

## Voir aussi

- PRÉREQUIS : [N07](N07-taux-de-variation.md) (Le taux de variation prépare la dérivée.)
- PROLONGEMENT : [N09](N09-derivees-usuelles.md) (Les dérivées usuelles accélèrent les calculs.)
