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

!!! objectifs ""

    - Connaître les premières propriétés de l’exponentielle.
    - Calculer avec les règles algébriques de l’exponentielle.
    - Lire et interpréter sa courbe.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N20 — Fonction exponentielle I](../cours/COURS_N20_FONCTION_EXPONENTIELLE.pdf)
- [TD N20 — Fonction exponentielle I](../td/TD_N20_FONCTION_EXPONENTIELLE.pdf)
- [Automatismes N20 — Fonction exponentielle I](../automatismes/AUTOMATISMES_N20_EXPONENTIELLE_I.pdf)
<!-- AUTO-DOCS:END -->

<!-- AUTOMATISMES-WEB:START -->
- ⚡ [Automatismes N20 en ligne : énoncés, corrigés et QCM interactif](../automatismes/automatismes-N20-fonction-exponentielle.md)
<!-- AUTOMATISMES-WEB:END -->

## Notions essentielles

!!! essentiel ""

    Il existe une unique fonction `f` dérivable sur `ℝ` telle que `f′=f` et `f(0)=1` : c'est la fonction **exponentielle**, notée `exp`. On note `e=exp(1)≈2,718`, et pour tout réel `x`, `exp(x)=e^x`.

    Pour tous réels `x` et `y` : `e^(x+y) = e^x × e^y`, et `e^x × e^(-x) = 1`.

    Pour tout réel `x`, `e^x>0`. Comme `exp′=exp`, la fonction exponentielle est **strictement croissante** sur `ℝ`.

    Pour tout réel `a`, la fonction `t↦e^(at)` est dérivable sur `ℝ` et `(e^(at))′ = a×e^(at)`.

## Exemple

!!! exemple ""

    Simplifions `e^(2x+1) / e^(x-3)` pour tout réel `x` :

    `e^(2x+1) / e^(x-3) = e^((2x+1)-(x-3)) = e^(x+4)`

## Repère historique — D’où vient la notation e ?

!!! historique ""

    Leonhard Euler, *Introductio in analysin infinitorum*, 1748
    {: .frise data-annee="1748" }

    Au XVIIIe siècle, Leonhard Euler joue un rôle majeur dans l’étude de l’exponentielle et dans la diffusion de la notation `e`. Dans son *Introductio in analysin infinitorum* de 1748, il développe les propriétés de ce nombre et en donne une approximation précise. Ce travail prolonge des recherches antérieures sur les logarithmes et les calculs exponentiels : l’histoire de la notion ne se réduit pas au choix d’une lettre.

    **Le lien avec le cours :** `e` désigne un nombre particulier, environ égal à 2,718, tandis que `exp` désigne une fonction. L’écriture `e^x` permet d’exprimer ses propriétés sous une forme proche des règles sur les puissances : `e^(x+y) = e^x × e^y`.

    Dans le cadre du cours, l’exponentielle est caractérisée par `exp′ = exp` et `exp(0) = 1`. On peut ainsi relier ses propriétés algébriques à la dérivation, en distinguant le nombre `e = exp(1)` de la fonction entière.

    *Source : [MacTutor, université de St Andrews — The number e](https://mathshistory.st-andrews.ac.uk/HistTopics/e/) (en anglais).*

## Voir aussi

- PRÉREQUIS : [N10](N10-variations-extremums.md) (Les variations donnent le cadre d’étude.)
- PROLONGEMENT : [N21](N21-exponentielle-ii.md) (La suite exploite les modèles exponentiels.)
