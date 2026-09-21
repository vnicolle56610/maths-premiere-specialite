---
title: Taux de variation
description: Cours et exercices de Première spécialité pour calculer et interpréter un taux de variation.
---

# N07 — Taux de variation

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N06-second-degre-ii/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N06 — Second degré II : racines, signe et discriminant</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N08-nombre-derive-derivation/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N08 — Nombre dérivé et dérivation</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

Le taux de variation mesure une évolution moyenne entre deux valeurs. Il relie les fonctions aux pentes de sécantes et prépare naturellement la notion de nombre dérivé. Les exercices alternent calculs, graphiques et interprétations dans des situations variées.

## Objectifs

- Calculer un taux de variation sur un intervalle.
- Interpréter graphiquement une pente de sécante.
- Préparer le passage au nombre dérivé.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N07 — Taux de variation](../cours/COURS_N07_TAUX_DE_VARIATION.pdf)
- [TD N07 — Taux de variation](../td/TD_N07_TAUX_DE_VARIATION.pdf)
- [Automatismes N07 — Taux de variation](../automatismes/AUTOMATISMES_N07_TAUX_DE_VARIATION.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Entre deux réels distincts `a` et `b`, l'accroissement de la variable est `b-a`, et l'accroissement de l'image est `f(b)-f(a)`. Le taux de variation de `f` entre `a` et `b` est le quotient `τf(a;b) = (f(b)-f(a)) / (b-a)` : il mesure l'accroissement moyen de `f(x)` par unité d'accroissement de `x`.

Ce taux est le coefficient directeur de la droite sécante passant par `A(a ; f(a))` et `B(b ; f(b))`. Un taux positif indique que l'image augmente en moyenne entre `a` et `b` ; un taux négatif indique qu'elle diminue.

Pour une fonction affine, le taux de variation entre deux réels distincts est toujours le même : la pente est constante. Pour une fonction non affine, le taux dépend en général de l'intervalle choisi.

L'écriture `(f(a+h)-f(a)) / h`, avec `h≠0`, permet de rapprocher progressivement le second point du premier : elle prépare la notion de nombre dérivé, étudiée par la suite.

## Exemple

Pour `f(x)=x²`, entre `1` et `3`, on a `f(1)=1` et `f(3)=9`.

`τf(1;3) = (9-1) / (3-1) = 4`

En moyenne, lorsque `x` augmente de `1`, l'image augmente de `4` sur cet intervalle.

## Voir aussi

- PRÉREQUIS : [N03](N03-fonctions-lectures-variations.md) (Les lectures de fonctions donnent le cadre.)
- PROLONGEMENT : [N08](N08-nombre-derive-derivation.md) (Le nombre dérivé est une limite de taux de variation.)
