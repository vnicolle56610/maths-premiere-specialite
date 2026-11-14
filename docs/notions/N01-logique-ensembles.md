---
title: Logique, ensembles et intervalles
description: Cours et exercices de Première spécialité pour consolider logique, ensembles, intervalles et raisonnements de début d’année.
---

# N01 — Logique, ensembles et intervalles

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--next" href="../N02-calcul-algebrique-equations/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N02 — Calcul algébrique et équations</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

Les premières notations structurent tout le travail de spécialité mathématiques. Cette notion consolide les ensembles, les intervalles, les implications et la rédaction courte. Elle sert de base pour écrire clairement les calculs, les résolutions d’équations et les raisonnements sur les fonctions.

## Objectifs

!!! objectifs ""

    - Utiliser correctement les notations d’ensembles et d’intervalles.
    - Traduire une phrase mathématique en écriture symbolique.
    - Rédiger un raisonnement court et lisible.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N01 — Logique, ensembles et intervalles](../cours/COURS_N01_LOGIQUE_ENSEMBLES.pdf)
- [TD N01 — Logique, ensembles et intervalles](../td/TD_N01_LOGIQUE_ENSEMBLES.pdf)
- [Corrigé TD N01](../corriges/CORRIGE_TD_N01_LOGIQUE_ENSEMBLES.pdf)
<!-- AUTO-DOCS:END -->

<!-- AUTOMATISMES-WEB:START -->
- ⚡ [Automatismes N01 en ligne : énoncés, corrigés et QCM interactif](../automatismes/automatismes-N01-logique-ensembles.md)
<!-- AUTOMATISMES-WEB:END -->

<!-- PARCOURS-GUIDE:START -->
### Parcours guidé

Des fiches pour reprendre la notion en autonomie : à la maison, après une absence ou avant une évaluation. Chaque bloc commence par un **exemple résolu**. Les réponses sont imprimées **à l'envers** dans les cadres « Je vérifie » : répondre d'abord, retourner la feuille ensuite.

- 📝 [Fiche 1 — Nombres et ensembles](../parcours-guide/PARCOURS_GUIDE_N01_FICHE_1.pdf) · ✔️ [corrigé](../parcours-guide/PARCOURS_GUIDE_N01_FICHE_1_CORRIGE.pdf) : classer un nombre dans N, Z, D, Q ou R, utiliser « appartient » et « est inclus » avec des ensembles finis, reconnaître une assertion, une phrase ouverte ou une écriture qui n'a pas de sens.
- 📝 [Fiche 2 — Les intervalles](../parcours-guide/PARCOURS_GUIDE_N01_FICHE_2.pdf) · ✔️ [corrigé](../parcours-guide/PARCOURS_GUIDE_N01_FICHE_2_CORRIGE.pdf) : passer d'une phrase à une inégalité puis à un intervalle, représenter et lire un intervalle sur une droite graduée, écrire « ou » avec une réunion, trouver l'intersection, la réunion et la différence de deux intervalles.
- 📝 [Fiche 3 — Vrai ou faux ?](../parcours-guide/PARCOURS_GUIDE_N01_FICHE_3.pdf) · ✔️ [corrigé](../parcours-guide/PARCOURS_GUIDE_N01_FICHE_3_CORRIGE.pdf) : dire si une phrase « pour tout » ou « il existe » est vraie, donner un contre-exemple, écrire la négation d'une phrase quantifiée, étudier une implication, écrire sa réciproque et sa contraposée.
- 📝 [Fiche passerelle — Traduire une situation](../parcours-guide/PARCOURS_GUIDE_N01_FICHE_4.pdf) · ✔️ [corrigé](../parcours-guide/PARCOURS_GUIDE_N01_FICHE_4_CORRIGE.pdf) : fiche passerelle : traduire des conditions par des intervalles, utiliser l'intersection et la réunion dans une situation, compter avec un diagramme à deux ensembles, puis un exercice sans modèle avant le retour au TD.

À la maison, ignorer les cases « STOP ». Faire le ticket de sortie seul, à la fin, puis l'apporter au cours suivant pour le faire vérifier. Ne lire le corrigé qu'après avoir cherché.
<!-- PARCOURS-GUIDE:END -->

<!-- AUTO-EVAL:START -->
- 🎯 Évaluée au DS1 du lundi 23 novembre : [voir le devoir blanc](../preparer-evaluation/index.md#ds1-2026-2027)
<!-- AUTO-EVAL:END -->

## Notions essentielles

!!! essentiel ""

    Une assertion est une phrase mathématique vraie ou fausse. Une phrase ouverte dépend d'une variable : elle devient une assertion lorsqu'une valeur est fixée.

    Une implication `P ⇒ Q` signifie que chaque fois que `P` est vraie, `Q` est vraie. Sa réciproque `Q ⇒ P` est une affirmation différente, à étudier séparément.

    Pour réfuter une implication, un seul contre-exemple suffit : il faut trouver une situation où l'hypothèse est vraie et la conclusion fausse.

    La contraposée de `P ⇒ Q` est `non Q ⇒ non P`. Elle a la même valeur de vérité que l'implication de départ.

    L'appartenance `x ∈ E` relie un élément à un ensemble ; l'inclusion `A ⊂ B` relie deux ensembles. Les opérations `A ∩ B`, `A ∪ B` et `A \ B` se lisent souvent efficacement sur une représentation d'intervalles.

## Exemple

!!! exemple ""

    Soient `A=[-3 ; 2]` et `B=]0 ; 5[`.

    La partie commune aux deux intervalles est `A ∩ B = ]0 ; 2]`.

    La réunion des deux intervalles est `A ∪ B = [-3 ; 5[`.

    La partie de `A` qui n'appartient pas à `B` est `A \ B = [-3 ; 0]`.

## Repère historique — Peut-on calculer avec des raisonnements ?

!!! historique ""

    George Boole, Angleterre puis Irlande, 1847–1854
    {: .frise data-annee="1847" data-fin="1854" }

    Au XIXe siècle, George Boole cherche à appliquer les méthodes de l’algèbre à la logique. Dans deux ouvrages parus en 1847 et en 1854, il développe un langage symbolique pour analyser des raisonnements. L’idée est de rendre explicites les règles qui permettent de passer de certaines affirmations à une conclusion.

    Cette démarche éclaire le rôle des notations du chapitre : elles permettent de distinguer des phrases qui se ressemblent, mais qui n’affirment pas la même chose. Avec les notations actuelles, « appartenir à A **et** à B » décrit l’intersection `A ∩ B`, tandis que « appartenir à A **ou** à B » décrit la réunion `A ∪ B`, en acceptant l’appartenance aux deux ensembles.

    **Le lien avec le cours :** traduire une phrase avec précision permet de contrôler un raisonnement. L’écriture symbolique accompagne l’explication ; elle exige de connaître le sens de chaque opération.

    *Source : [Stanford Encyclopedia of Philosophy — George Boole](https://plato.stanford.edu/entries/boole/) (en anglais).*
