---
title: Fonction exponentielle I
description: Cours et exercices de Première spécialité pour découvrir la fonction exponentielle et ses premières propriétés.
---

# N20 — Fonction exponentielle I

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N19-geometrie-reperee/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N19 — Géométrie repérée</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N21-exponentielle-ii/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N21 — Exponentielle II : modèles</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

La fonction exponentielle modélise des évolutions où le taux de variation garde une structure particulière. Cette première approche installe la définition, les propriétés algébriques et les premières lectures graphiques. Elle sera prolongée par des modèles plus complets.

## Objectifs

- Connaître les premières propriétés de l’exponentielle.
- Calculer avec les règles algébriques de l’exponentielle.
- Lire et interpréter sa courbe.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N20 — Fonction exponentielle I](../cours/COURS_N20_FONCTION_EXPONENTIELLE.pdf)
- [TD N20 — Fonction exponentielle I](../td/TD_N20_FONCTION_EXPONENTIELLE.pdf)
- [Automatismes N20 — Fonction exponentielle I](../automatismes/AUTOMATISMES_N20_EXPONENTIELLE_I.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Il existe une unique fonction `f` dérivable sur `ℝ` telle que `f′=f` et `f(0)=1` : c'est la fonction **exponentielle**, notée `exp`. On note `e=exp(1)≈2,718`, et pour tout réel `x`, `exp(x)=e^x`.

Pour tous réels `x` et `y` : `e^(x+y) = e^x × e^y`, et `e^x × e^(-x) = 1`.

Pour tout réel `x`, `e^x>0`. Comme `exp′=exp`, la fonction exponentielle est **strictement croissante** sur `ℝ`.

Pour tout réel `a`, la fonction `t↦e^(at)` est dérivable sur `ℝ` et `(e^(at))′ = a×e^(at)`.

## Exemple

Simplifions `e^(2x+1) / e^(x-3)` pour tout réel `x` :

`e^(2x+1) / e^(x-3) = e^((2x+1)-(x-3)) = e^(x+4)`

## Voir aussi

- PRÉREQUIS : [N10](N10-variations-extremums.md) (Les variations donnent le cadre d’étude.)
- PROLONGEMENT : [N21](N21-exponentielle-ii.md) (La suite exploite les modèles exponentiels.)
