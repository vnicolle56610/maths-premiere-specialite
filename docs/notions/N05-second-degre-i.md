---
title: "Second degré I : fonction carré et forme canonique"
description: Cours et exercices de Première spécialité sur la fonction carré, les paraboles et la forme canonique.
---

# N05 — Second degré I : fonction carré et forme canonique

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N04-reperages-vecteurs/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N04 — Repérage et vecteurs</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N06-second-degre-ii/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N06 — Second degré II : racines, signe et discriminant</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

Le second degré commence par l’étude de la fonction carré et des paraboles. La forme canonique permet de lire un extremum et de comprendre le rôle des transformations algébriques. Cette étape prépare les racines, le discriminant, le signe et les problèmes d’optimisation.

## Objectifs

!!! objectifs ""

    - Reconnaître et exploiter une forme canonique.
    - Lire le sommet et les variations d’une parabole.
    - Relier expression algébrique et représentation graphique.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N05 — Second degré I : fonction carré et forme canonique](../cours/COURS_N05_SECOND_DEGRE_I.pdf)
- [TD N05 — Second degré I : fonction carré et forme canonique](../td/TD_N05_SECOND_DEGRE_I.pdf)
- [Corrigé TD N05](../corriges/CORRIGE_TD_N05_SECOND_DEGRE_I.pdf)
<!-- AUTO-DOCS:END -->

<!-- AUTOMATISMES-WEB:START -->
- ⚡ [Automatismes N05 en ligne : énoncés, corrigés et QCM interactif](../automatismes/automatismes-N05-second-degre-forme-canonique.md)
<!-- AUTOMATISMES-WEB:END -->

<!-- PARCOURS-GUIDE:START -->
### Parcours guidé

Des fiches pour reprendre la notion en autonomie : à la maison, après une absence ou avant une évaluation. Chaque bloc commence par un **exemple résolu**. Les réponses sont imprimées **à l'envers** dans les cadres « Je vérifie » : répondre d'abord, retourner la feuille ensuite.

**Pour réviser** : pour chaque bloc, tenter d'abord la dernière question sans aide. Si elle est réussie, passer au bloc suivant ; sinon, lire l'exemple résolu et faire tout le bloc. Terminer par les exercices du TD indiqués à côté des questions.

- 📝 [Fiche 1 — La fonction carré](../parcours-guide/PARCOURS_GUIDE_N05_FICHE_1.pdf) · ✔️ [corrigé](../parcours-guide/PARCOURS_GUIDE_N05_FICHE_1_CORRIGE.pdf) : calculer des carrés sans erreur de signe, tableau de valeurs et symétrie, images et antécédents sur la courbe, variations et minimum de la fonction carré.
- 📝 [Fiche 2 — Lire une forme canonique](../parcours-guide/PARCOURS_GUIDE_N05_FICHE_2.pdf) · ✔️ [corrigé](../parcours-guide/PARCOURS_GUIDE_N05_FICHE_2_CORRIGE.pdf) : lire a, alpha et beta sans erreur de signe, sommet et axe, minimum ou maximum et tableau de variations, lecture d'une parabole tracée, symétrie par rapport à l'axe.
- 📝 [Fiche 3 — Obtenir la forme canonique](../parcours-guide/PARCOURS_GUIDE_N05_FICHE_3.pdf) · ✔️ [corrigé](../parcours-guide/PARCOURS_GUIDE_N05_FICHE_3_CORRIGE.pdf) : faire apparaître un carré, écrire x² + bx + c sous forme canonique et contrôler en développant, utiliser alpha = -b/(2a) et beta = f(alpha) ; pour aller plus loin : montrer qu'une expression est toujours positive.
- 📝 [Fiche passerelle — De la courbe à l'expression](../parcours-guide/PARCOURS_GUIDE_N05_FICHE_4.pdf) · ✔️ [corrigé](../parcours-guide/PARCOURS_GUIDE_N05_FICHE_4_CORRIGE.pdf) : fiche passerelle : trouver a avec le sommet et un point, lire une parabole puis écrire son expression, puis une arche sans modèle où l'on choisit soi-même entre lire, calculer et utiliser la symétrie, avant le retour au TD.

À la maison, ignorer les cases « STOP ». Faire le ticket de sortie seul, à la fin, puis l'apporter au cours suivant pour le faire vérifier. Ne lire le corrigé qu'après avoir cherché.
<!-- PARCOURS-GUIDE:END -->

<!-- AUTO-EVAL:START -->
- 🎯 Pour réviser : [devoir blanc du mini-test 2 du lundi 9 novembre 2026](../preparer-evaluation/index.md#mt2-2026-2027)
- 🎯 Évaluée au DS1 du lundi 23 novembre : [voir le devoir blanc](../preparer-evaluation/index.md#ds1-2026-2027)
<!-- AUTO-EVAL:END -->

## Notions essentielles

!!! essentiel ""

    La fonction carré est définie sur `ℝ` par `f(x)=x²`. Sa courbe est une parabole de sommet `O(0 ; 0)`, symétrique par rapport à l'axe des ordonnées. Elle est décroissante sur `]-∞ ; 0]`, puis croissante sur `[0 ; +∞[`.

    Une fonction de la forme `a(x-α)²+β`, avec `a≠0`, a pour courbe une parabole de sommet `S(α ; β)` et d'axe de symétrie la droite `x=α`. Si `a>0`, `f` admet un minimum égal à `β` ; si `a<0`, `f` admet un maximum égal à `β`.

    L'écriture `a(x-α)²+β` s'appelle la forme canonique. Elle est la plus efficace pour lire un sommet ou un extremum, alors que la forme développée facilite le calcul d'images et la forme factorisée la lecture des zéros.

    Pour transformer `x²+bx+c` en forme canonique, on utilise l'identité `x²+2px=(x+p)²-p²` : on fait apparaître le carré qui possède le même terme en `x`, puis on ajuste la constante.

## Exemple

!!! exemple ""

    Mettons `x²+6x+5` sous forme canonique.

    `x²+6x+5 = (x+3)² - 9 + 5 = (x+3)² - 4`

    La parabole a donc pour sommet `S(-3 ; -4)`, pour axe `x=-3`, et la fonction admet un minimum égal à `-4`.

## Repère historique — Pourquoi dit-on « compléter le carré » ?

!!! historique ""

    Al-Khwarizmi, Bagdad, IXe siècle
    {: .frise data-annee="820" data-etiquette="v. 820" }

    Au IXe siècle, Al-Khwarizmi accompagne ses méthodes de résolution d’équations par des justifications géométriques. L’un de ses exemples correspond, dans notre notation, à `x² + 10x = 39`. Pour une longueur positive `x`, on peut représenter `x²` par l’aire d’un carré et `10x` par celles de deux rectangles de côtés `x` et 5.

    En plaçant ces rectangles sur deux côtés adjacents du carré, il manque un petit carré de côté 5 pour former un grand carré de côté `x + 5`. Ajouter son aire, 25, conduit à `(x + 5)² = 64`. L’expression « compléter le carré » prend ici un sens concret.

    **Le lien avec le cours :** la forme canonique reprend algébriquement cette idée. Par exemple, `x² + 6x + 5 = (x + 3)² − 4`. L’identité est aujourd’hui valable pour tout réel `x`, au-delà de l’interprétation initiale en longueurs positives, et permet de lire le minimum de la fonction.

    *Source : [American Mathematical Society — Completing the Square, par Tony Phillips](https://mathvoices.ams.org/featurecolumn/2020/11/01/fc-2020-10-2/) (en anglais).*

## Voir aussi

- PRÉREQUIS : [N02](N02-calcul-algebrique-equations.md) (Les transformations algébriques sont centrales.)
- PROLONGEMENT : [N06](N06-second-degre-ii.md) (La suite traite racines, signe et discriminant.)
