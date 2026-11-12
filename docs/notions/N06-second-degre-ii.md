---
title: "Second degré II : racines, signe et discriminant"
description: Cours et exercices de Première spécialité pour résoudre des équations et inéquations du second degré.
---

# N06 — Second degré II : racines, signe et discriminant

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N05-second-degre-i/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N05 — Second degré I : fonction carré et forme canonique</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N07-taux-de-variation/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N07 — Taux de variation</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

Cette notion complète l’étude du second degré avec les racines, le discriminant, la factorisation et le signe. Les exercices conduisent à résoudre des équations, des inéquations et des problèmes. Le second degré devient alors un outil de modélisation et de décision.

## Objectifs

!!! objectifs ""

    - Calculer un discriminant et interpréter les racines.
    - Dresser et utiliser un tableau de signe.
    - Résoudre des inéquations et problèmes du second degré.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N06 — Second degré (partie 1) : formes, racines, signe et discriminant (Partie 1 Formes Racines Signe Discriminant)](../cours/COURS_N06_PARTIE_1_FORMES_RACINES_SIGNE_DISCRIMINANT.pdf)
- [Cours N06 — Second degré (partie 2) : inéquations, optimisation et problèmes (Partie 2 Inequations Optimisation Problemes)](../cours/COURS_N06_PARTIE_2_INEQUATIONS_OPTIMISATION_PROBLEMES.pdf)
- [TD N06 — Second degré (partie 1) : formes, racines, signe et discriminant (Partie 1 Formes Racines Signe Discriminant)](../td/TD_N06_PARTIE_1_FORMES_RACINES_SIGNE_DISCRIMINANT.pdf)
- [TD N06 — Second degré (partie 2) : inéquations, optimisation et problèmes (Partie 2 Inequations Optimisation Problemes)](../td/TD_N06_PARTIE_2_INEQUATIONS_OPTIMISATION_PROBLEMES.pdf)
<!-- AUTO-DOCS:END -->

<!-- AUTOMATISMES-WEB:START -->
- ⚡ [Automatismes N06 en ligne — Second degré II (partie 1) : énoncés, corrigés et QCM interactif](../automatismes/automatismes-N06-second-degre-racines-signe-discriminant.md)
- ⚡ [Automatismes N06 en ligne — Second degré II (partie 2) : énoncés, corrigés et QCM interactif](../automatismes/automatismes-N06-second-degre-inequations-optimisation.md)
<!-- AUTOMATISMES-WEB:END -->

<!-- PARCOURS-GUIDE:START -->
### Parcours guidé (partie 1)

Des fiches pour reprendre la notion en autonomie : à la maison, après une absence ou avant une évaluation. Chaque bloc commence par un **exemple résolu**. Les réponses sont imprimées **à l'envers** dans les cadres « Je vérifie » : répondre d'abord, retourner la feuille ensuite.

- 📝 [Fiche 1 — Trois formes, des racines](../parcours-guide/PARCOURS_GUIDE_N06_PARTIE_1_FICHE_1.pdf) : forme canonique et signe de α, racine ou image, racines sur une forme factorisée, choix de la forme.
- 📝 [Fiche 2 — Résoudre sans discriminant](../parcours-guide/PARCOURS_GUIDE_N06_PARTIE_1_FICHE_2.pdf) : facteur commun, x² = k, forme canonique, racine évidente et produit des racines.
- 📝 [Fiche 3 — Discriminant, factorisation, signe](../parcours-guide/PARCOURS_GUIDE_N06_PARTIE_1_FICHE_3.pdf) : calculer Δ, résoudre et vérifier, factoriser sans oublier a, tableau de signes.

À la maison, ignorer les cases « STOP ». Faire le ticket de sortie seul, à la fin, puis l'apporter au cours suivant pour le faire vérifier.
<!-- PARCOURS-GUIDE:END -->

<!-- AUTO-EVAL:START -->
- 🎯 Évaluée au DS1 du lundi 23 novembre : [devoir blanc en ligne le lundi 16 novembre](../preparer-evaluation/index.md#ds1-2026-2027)
<!-- AUTO-EVAL:END -->

## Notions essentielles

!!! essentiel ""

    Pour `P(x)=ax²+bx+c`, avec `a≠0`, un réel `r` est une racine de `P` lorsque `P(r)=0`. Le discriminant `Δ=b²-4ac` donne le nombre de racines réelles :

    - si `Δ>0`, deux racines distinctes `x₁` et `x₂` ;
    - si `Δ=0`, une racine double `x₀=-b/2a` ;
    - si `Δ<0`, aucune racine réelle.

    Avec deux racines `x₁<x₂`, le trinôme est du signe de `a` à l'extérieur des racines et du signe opposé entre elles. Avec une racine double, il garde le signe de `a` et s'annule seulement en `x₀`. Sans racine réelle, il garde le signe de `a` sur `ℝ`.

    Pour résoudre une inéquation du second degré, on ramène tout dans un membre, on détermine les racines ou une factorisation, puis on dresse le tableau de signes avant de conclure. Une racine appartient à l'ensemble des solutions pour `⩽` ou `⩾`, mais pas pour `<` ou `>`.

## Exemple

!!! exemple ""

    Résolvons `2x² - 5x - 3 = 0`. Ici `a=2`, `b=-5`, `c=-3`.

    `Δ = (-5)² - 4×2×(-3) = 49`

    Comme `Δ>0`, l'équation possède deux solutions :

    `x₁ = (5-7)/4 = -0,5` et `x₂ = (5+7)/4 = 3`

    Donc `S = {-0,5 ; 3}`.

## Repère historique — Une équation peut-elle avoir deux solutions ?

!!! historique ""

    Al-Khwarizmi, Bagdad, IXe siècle
    {: .frise data-annee="820" data-etiquette="v. 820" }

    Dans son traité d’algèbre du IXe siècle, Al-Khwarizmi étudie un problème que nous écrivons `x² + 21 = 10x`. Sa méthode fait apparaître deux réponses positives : 3 et 7. Il distingue aussi les situations où une équation de ce type n’a pas de solution et celle où les deux réponses se rejoignent. Il expose ces cas avec des mots, sans notre notation du discriminant.

    **Le lien avec le cours :** en écriture actuelle, l’équation devient `x² − 10x + 21 = 0`, et son discriminant vaut `100 − 84 = 16`. La forme canonique donne `(x − 5)² = 4`, d’où les deux solutions 3 et 7.

    Si l’on remplace 21 par 25, on obtient une seule racine, 5 ; avec 26, aucune racine réelle. Le discriminant rassemble ces trois situations dans une même règle. Il indique le nombre de racines réelles ; pour déterminer le signe du trinôme, il faut aussi tenir compte du coefficient de `x²`.

    *Source : [MacTutor, université de St Andrews — Al-Khwarizmi and quadratic equations](https://mathshistory.st-andrews.ac.uk/Extras/Al-Khwarizmi_quadratics/) (en anglais).*

## Voir aussi

- PRÉREQUIS : [N05](N05-second-degre-i.md) (La forme canonique éclaire la parabole.)
- PROLONGEMENT : [N10](N10-variations-extremums.md) (Les extremums seront repris avec les dérivées.)
