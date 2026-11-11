---
title: Probabilités conditionnelles
description: Cours et exercices de Première spécialité pour calculer avec des probabilités conditionnelles et des arbres pondérés.
---

# N22 — Probabilités conditionnelles

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N21-exponentielle-ii/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N21 — Exponentielle II : modèles</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N23-independance-arbres/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N23 — Indépendance et arbres</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

Les probabilités conditionnelles permettent de calculer une probabilité en tenant compte d'une information déjà connue. On cherche par exemple la probabilité qu'un événement B se réalise sachant qu'un événement A est déjà réalisé. Les arbres pondérés permettent de représenter simplement ce type de situation.

## Objectifs

!!! objectifs ""

    - Lire et compléter un arbre pondéré.
    - Calculer une probabilité conditionnelle.
    - Utiliser les intersections d'événements dans un raisonnement.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N22 — Probabilités conditionnelles](../cours/COURS_N22_PROBABILITES_CONDITIONNELLES.pdf)
- [TD N22 — Probabilités conditionnelles](../td/TD_N22_PROBABILITES_CONDITIONNELLES.pdf)
- [Automatismes N22 — Probabilités conditionnelles](../automatismes/AUTOMATISMES_N22_PROBABILITES_CONDITIONNELLES.pdf)
<!-- AUTO-DOCS:END -->

<!-- AUTOMATISMES-WEB:START -->
- ⚡ [Automatismes N22 en ligne : énoncés, corrigés et QCM interactif](../automatismes/automatismes-N22-probabilites-conditionnelles.md)
<!-- AUTOMATISMES-WEB:END -->

## Notions essentielles

!!! essentiel ""

    Si P(A)>0, la probabilité de B sachant A se note P<sub>A</sub>(B).

    On a alors :

    **P(A ∩ B) = P(A) × P<sub>A</sub>(B)**

    Dans un arbre pondéré, les probabilités inscrites sur les branches de deuxième niveau sont des probabilités conditionnelles. La probabilité d'un chemin s'obtient en multipliant les probabilités inscrites sur ses branches.

## Exemple

!!! exemple ""

    Si P(A)=0,4 et P<sub>A</sub>(B)=0,25, alors :

    **P(A ∩ B) = 0,4 × 0,25 = 0,10**

    La probabilité que A et B se réalisent est donc égale à 0,10.

## Repère historique — Comment une information modifie-t-elle une probabilité ?

!!! historique ""

    Thomas Bayes, mémoire publié par Richard Price, 1763
    {: .frise data-annee="1763" }

    Au XVIIIe siècle, Thomas Bayes étudie comment tirer une information probabiliste d’observations. Son mémoire, communiqué après sa mort par Richard Price en 1763, devient un jalon de l’histoire de l’inférence probabiliste. Les probabilités conditionnelles du cours fournissent un langage actuel pour distinguer une probabilité initiale d’une probabilité calculée lorsqu’une information est connue.

    **Le lien avec le cours :** prenons un exemple moderne. Une boîte contient trois jetons rouges et deux bleus, tous indiscernables au toucher. On en tire deux sans remise. Notons `A` l’événement « le premier jeton est rouge » et `B` l’événement « le second est rouge ». On a `P(A) = 3/5` et `P_A(B) = 2/4`, car après un premier rouge, il reste deux rouges parmi quatre jetons.

    La probabilité d’obtenir deux rouges vaut donc `(3/5) × (2/4) = 3/10`. L’arbre pondéré organise ces informations successives. Cet exemple illustre le conditionnement, sans reproduire le problème historique de Bayes.

    *Source : [Université de Cambridge — Bayes’ probability, Statistics 1B Interludes](https://www.statslab.cam.ac.uk/Dept/People/djsteaching/interlude-6-bayesian.pdf) (PDF en anglais).*

## Voir aussi

- PROLONGEMENT : [N23](N23-independance-arbres.md) (L’indépendance prolonge les calculs conditionnels.)
