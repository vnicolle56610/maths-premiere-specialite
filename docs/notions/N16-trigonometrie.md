---
title: Trigonométrie
description: Cours et exercices de Première spécialité pour utiliser sinus, cosinus, angles et cercle trigonométrique.
---

# N16 — Trigonométrie

<!-- NOTION-NAV:START -->
<nav class="notion-nav" aria-label="Navigation entre notions">
<a class="notion-nav__btn notion-nav__btn--prev" href="../N15-droites-equations/"><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M16 6v12L6 12z" fill="currentColor"/></svg></span><span class="notion-nav__text"><small>Notion précédente</small><span class="notion-nav__title">N15 — Droites et équations</span></span></a>
<a class="notion-nav__btn notion-nav__btn--next" href="../N17-produit-scalaire-i/"><span class="notion-nav__text"><small>Notion suivante</small><span class="notion-nav__title">N17 — Produit scalaire I</span></span><span class="notion-nav__icon"><svg viewBox="0 0 24 24" width="15" height="15" aria-hidden="true"><path d="M8 6v12l10-6z" fill="currentColor"/></svg></span></a>
</nav>
<!-- NOTION-NAV:END -->

La trigonométrie étend les outils de mesure des angles. On travaille le cercle trigonométrique, les valeurs remarquables, les relations entre sinus et cosinus et les premières équations trigonométriques. Ces repères seront utiles en géométrie et dans les modèles périodiques.

## Objectifs

!!! objectifs ""

    - Placer et lire des angles sur le cercle trigonométrique.
    - Utiliser les valeurs remarquables de sinus et cosinus.
    - Résoudre des questions simples avec les relations trigonométriques.

## Documents

<!-- AUTO-DOCS:START -->
- [Cours N16 — Trigonométrie](../cours/COURS_N16_TRIGONOMETRIE.pdf)
- [TD N16 — Trigonométrie](../td/TD_N16_TRIGONOMETRIE.pdf)
- [Automatismes N16 — Trigonométrie](../automatismes/AUTOMATISMES_N16_TRIGONOMETRIE.pdf)
<!-- AUTO-DOCS:END -->

## Notions essentielles

!!! essentiel ""

    Le cercle trigonométrique est le cercle de centre `O`, de rayon `1`, orienté dans le sens inverse des aiguilles d'une montre. Un tour complet correspond à `2π` radians, donc `360° = 2π` rad.

    En enroulant la droite numérique autour du cercle à partir du point `I`, on associe à chaque réel `x` un point `Mₓ`. Deux réels qui diffèrent d'un multiple de `2π` correspondent au même point.

    Le cosinus et le sinus de `x` sont les coordonnées de `Mₓ` : `Mₓ(cos x ; sin x)`. Pour tout réel `x`, `cos²x + sin²x = 1`, avec `-1⩽cos x⩽1` et `-1⩽sin x⩽1`.

    Cosinus et sinus sont `2π`-périodiques. La fonction cosinus est paire (`cos(-x)=cos x`) et la fonction sinus est impaire (`sin(-x)=-sin x`). On a aussi `cos(π-x)=-cos x` et `sin(π-x)=sin x`.

## Exemple

!!! exemple ""

    Déterminons `cos(5π/6)`. On écrit `5π/6 = π - π/6`, donc :

    `cos(5π/6) = -cos(π/6) = -√3/2`

## Repère historique — Pourquoi les astronomes calculaient-ils des cordes ?

!!! historique ""

    Ptolémée, *Almageste*, Alexandrie, IIe siècle
    {: .frise data-annee="150" data-etiquette="IIe s." }

    Au IIe siècle de notre ère, Ptolémée présente dans l’*Almageste* des tables de cordes destinées aux calculs astronomiques. Une corde est le segment qui relie deux points d’un cercle. Ses tables associent à un angle au centre une longueur de corde, pour un cercle de rayon 60. Elles permettent de passer des angles aux longueurs sans refaire chaque construction géométrique.

    **Le lien avec le cours :** avec les notations actuelles, une corde qui intercepte un angle au centre `α`, pour `0 ≤ α ≤ π`, a pour longueur `2R × sin(α/2)` dans un cercle de rayon `R`. Cette relation se retrouve en partageant le triangle isocèle formé par les deux rayons en deux triangles rectangles.

    Le cercle trigonométrique du cours choisit un rayon égal à 1 et définit cosinus et sinus comme des coordonnées. Il prolonge le lien entre angles et longueurs, avec un cadre adapté aux angles orientés et à la périodicité. Il se distingue donc des tables anciennes de cordes.

    *Source : [Heinz Klaus Strick — Claudius Ptolemy, texte hébergé par l’université de St Andrews](https://mathshistory.st-andrews.ac.uk/Strick/ptolemy.pdf) (PDF en anglais).*

## Voir aussi

- PRÉREQUIS : [N04](N04-reperages-vecteurs.md) (Le repérage aide à lire le cercle trigonométrique.)
