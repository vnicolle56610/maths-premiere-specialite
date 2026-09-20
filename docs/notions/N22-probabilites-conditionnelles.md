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

- Lire et compléter un arbre pondéré.
- Calculer une probabilité conditionnelle.
- Utiliser les intersections d'événements dans un raisonnement.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N22 — Probabilités conditionnelles](../cours/COURS_N22_PROBABILITES_CONDITIONNELLES.pdf)
- [TD N22 — Probabilités conditionnelles](../td/TD_N22_PROBABILITES_CONDITIONNELLES.pdf)
- [Automatismes N22 — Probabilités conditionnelles](../automatismes/AUTOMATISMES_N22_PROBABILITES_CONDITIONNELLES.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

Si P(A)>0, la probabilité de B sachant A se note P<sub>A</sub>(B).

On a alors :

**P(A ∩ B) = P(A) × P<sub>A</sub>(B)**

Dans un arbre pondéré, les probabilités inscrites sur les branches de deuxième niveau sont des probabilités conditionnelles. La probabilité d'un chemin s'obtient en multipliant les probabilités inscrites sur ses branches.

## Exemple

Si P(A)=0,4 et P<sub>A</sub>(B)=0,25, alors :

**P(A ∩ B) = 0,4 × 0,25 = 0,10**

La probabilité que A et B se réalisent est donc égale à 0,10.

## Voir aussi

- PROLONGEMENT : [N23](N23-independance-arbres.md) (L’indépendance prolonge les calculs conditionnels.)
