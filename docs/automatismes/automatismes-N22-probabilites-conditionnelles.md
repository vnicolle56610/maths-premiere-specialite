---
title: "Automatismes Première spécialité – Probabilités conditionnelles : exercices et QCM corrigés"
description: "24 questions d'automatismes de Première spécialité (probabilités conditionnelles), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N22 — Probabilités conditionnelles

24 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N22-probabilites-conditionnelles.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N22_PROBABILITES_CONDITIONNELLES.pdf){ .md-button }
[📖 Revoir la notion](../notions/N22-probabilites-conditionnelles.md){ .md-button }
</div>

## Série A — 

<div class="auto-consigne" markdown>
**Consigne.** Traduire les notations et calculer des probabilités conditionnelles simples.
</div>

<ol class="auto-questions">
<li value="1">Lire <span class="arithmatex">\(P_A(B)\)</span> en phrase.</li>
<li value="2">Formule de <span class="arithmatex">\(P_A(B)\)</span> avec <span class="arithmatex">\(P(A)\neq0\)</span>.</li>
<li value="3">Si <span class="arithmatex">\(P(A\cap B)=0{,}18\)</span> et <span class="arithmatex">\(P(A)=0{,}6\)</span>, calculer <span class="arithmatex">\(P_A(B)\)</span>.</li>
<li value="4">Si <span class="arithmatex">\(P_A(B)=0{,}4\)</span> et <span class="arithmatex">\(P(A)=0{,}5\)</span>, calculer <span class="arithmatex">\(P(A\cap B)\)</span>.</li>
<li value="5">Si <span class="arithmatex">\(A\)</span> et <span class="arithmatex">\(B\)</span> sont incompatibles, que vaut <span class="arithmatex">\(P(A\cap B)\)</span> ?</li>
<li value="6">Si <span class="arithmatex">\(P(A)=0{,}7\)</span>, calculer <span class="arithmatex">\(P(\overline A)\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Toujours vérifier l'événement de conditionnement.</li><li><span class="arithmatex">\(P_A(B)\)</span> signifie : parmi les <span class="arithmatex">\(A\)</span>.</li><li>Utiliser le complément quand c'est plus rapide.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas confondre <span class="arithmatex">\(P_A(B)\)</span> et <span class="arithmatex">\(P_B(A)\)</span>.</li><li>Une probabilité est entre <span class="arithmatex">\(0\)</span> et <span class="arithmatex">\(1\)</span>.</li></ul>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(\boxed{\text{probabilité de }B\text{ sachant }A}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(\boxed{P_A(B)=\dfrac{P(A\cap B)}{P(A)}}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(P_A(B)=\)</span><wbr><span class="arithmatex">\(0{,}18/0{,}6=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}3}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(P(A\cap B)=\)</span><wbr><span class="arithmatex">\(0{,}4\times0{,}5=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}2}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(\boxed{P(A\cap B)=0}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(P(\overline A)=\)</span><wbr><span class="arithmatex">\(1-0{,}7=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}3}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Formule clé : <span class="arithmatex">\(P(A\cap B)=\)</span><wbr><span class="arithmatex">\(P(A) imes P_A(B)\)</span>. Complément : <span class="arithmatex">\(P(\overline A)=1-P(A)\)</span>.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> L'ordre dans <span class="arithmatex">\(P_A(B)\)</span> est essentiel.</div>

## Série B — 

<div class="auto-consigne" markdown>
**Consigne.** Compléter mentalement des branches et calculer des probabilités d'intersections.
</div>

<ol class="auto-questions">
<li value="1">Sur une branche, <span class="arithmatex">\(P(A)=0{,}35\)</span>. Que vaut <span class="arithmatex">\(P(\overline A)\)</span> ?</li>
<li value="2">Si <span class="arithmatex">\(P(A)=0{,}4\)</span> et <span class="arithmatex">\(P_A(B)=0{,}7\)</span>, calculer <span class="arithmatex">\(P(A\cap B)\)</span>.</li>
<li value="3">Si <span class="arithmatex">\(P(\overline A)=0{,}6\)</span> et <span class="arithmatex">\(P_{\overline A}(B)=\)</span><wbr><span class="arithmatex">\(0{,}25\)</span>, calculer <span class="arithmatex">\(P(\overline A\cap B)\)</span>.</li>
<li value="4">Deuxième branche après <span class="arithmatex">\(A\)</span> : <span class="arithmatex">\(P_A(B)=0{,}2\)</span>. Que vaut <span class="arithmatex">\(P_A(\overline B)\)</span> ?</li>
<li value="5">Si <span class="arithmatex">\(P(A\cap B)=0{,}12\)</span> et <span class="arithmatex">\(P(\overline A\cap B)=\)</span><wbr><span class="arithmatex">\(0{,}18\)</span>, calculer <span class="arithmatex">\(P(B)\)</span>.</li>
<li value="6">Nommer la formule utilisée à la question précédente.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Sur deux branches issues d'un même noeud, la somme vaut <span class="arithmatex">\(1\)</span>.</li><li>Pour une intersection : multiplier le long du chemin.</li><li>Pour un total : additionner les chemins qui mènent à l'événement.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Les probabilités conditionnelles dépendent du noeud de départ.</li><li>Ne pas additionner les branches d'un même chemin.</li></ul>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(P(\overline A)=\)</span><wbr><span class="arithmatex">\(1-0{,}35=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}65}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(P(A\cap B)=\)</span><wbr><span class="arithmatex">\(0{,}4\times0{,}7=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}28}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(0{,}6\times0{,}25=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}15}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(P_A(\overline B)=\)</span><wbr><span class="arithmatex">\(1-0{,}2=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}8}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(P(B)=\)</span><wbr><span class="arithmatex">\(0{,}12+0{,}18=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}30}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(\boxed{formule des probabilités totales}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Multiplier le long d'un chemin. Additionner les chemins incompatibles qui réalisent le même événement.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> L'arbre impose l'ordre des conditions.</div>

## Série C — 

<div class="auto-consigne" markdown>
**Consigne.** Lire un tableau d'effectifs et passer aux probabilités.
</div>

<ol class="auto-questions">
<li value="1">Dans une classe de <span class="arithmatex">\(30\)</span> élèves, <span class="arithmatex">\(18\)</span> sont filles. Probabilité de choisir une fille ?</li>
<li value="2">Parmi les <span class="arithmatex">\(18\)</span> filles, <span class="arithmatex">\(6\)</span> font option théâtre. Calculer <span class="arithmatex">\(P_F(T)\)</span>.</li>
<li value="3">Dans la classe, <span class="arithmatex">\(10\)</span> élèves font théâtre. Combien de garçons font théâtre ?</li>
<li value="4">Calculer <span class="arithmatex">\(P(F\cap T)\)</span> avec les données précédentes.</li>
<li value="5">Calculer <span class="arithmatex">\(P(T)\)</span>.</li>
<li value="6">Calculer <span class="arithmatex">\(P_T(F)\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Transformer un effectif en probabilité : diviser par le total.</li><li>Condition : diviser par le total de la ligne ou de la colonne concernée.</li><li>Vérifier l'univers utilisé.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Changer de dénominateur quand on conditionne.</li><li><span class="arithmatex">\(P_F(T)\)</span> et <span class="arithmatex">\(P_T(F)\)</span> peuvent être différents.</li></ul>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(P(F)=18/30=\boxed{0{,}6}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(P_F(T)=\)</span><wbr><span class="arithmatex">\(6/18=\)</span><wbr><span class="arithmatex">\(\boxed{\frac13}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(10-6=\boxed{4}\)</span> garçons font théâtre.</li>
    <li value="4"><span class="arithmatex">\(P(F\cap T)=\)</span><wbr><span class="arithmatex">\(6/30=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}2}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(P(T)=\)</span><wbr><span class="arithmatex">\(10/30=\)</span><wbr><span class="arithmatex">\(\boxed{\frac13}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(P_T(F)=\)</span><wbr><span class="arithmatex">\(6/10=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}6}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Tableau : choisir le bon total de référence. Intersection : case du tableau sur total général.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Une même case peut servir à plusieurs quotients selon la condition.</div>

## Série D — 

<div class="auto-consigne" markdown>
**Consigne.** Choisir la seule réponse correcte. Aucune justification demandée.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(P_A(B)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(\dfrac{P(A)}{P(B)}\)</span></li><li><span class="arithmatex">\(\dfrac{P(A\cap B)}{P(A)}\)</span></li><li><span class="arithmatex">\(P(A)P(B)\)</span></li><li><span class="arithmatex">\(P(A\cup B)\)</span></li></ol></li>
<li value="2">Si <span class="arithmatex">\(P(A)=0{,}4\)</span>, <span class="arithmatex">\(P_A(B)=0{,}5\)</span>, alors <span class="arithmatex">\(P(A\cap B)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(0{,}9\)</span></li><li><span class="arithmatex">\(0{,}1\)</span></li><li><span class="arithmatex">\(0{,}2\)</span></li><li><span class="arithmatex">\(0{,}45\)</span></li></ol></li>
<li value="3">Sur deux branches complémentaires <span class="arithmatex">\(B\)</span> et <span class="arithmatex">\(\overline B\)</span>, les probabilités<ol class="auto-choix" type="A"><li>s'additionnent à <span class="arithmatex">\(1\)</span></li><li>se multiplient</li><li>sont égales</li><li>valent <span class="arithmatex">\(0\)</span></li></ol></li>
<li value="4"><span class="arithmatex">\(P(A\cap B)\)</span> se lit<ol class="auto-choix" type="A"><li><span class="arithmatex">\(A\)</span> ou <span class="arithmatex">\(B\)</span></li><li><span class="arithmatex">\(A\)</span> sachant <span class="arithmatex">\(B\)</span></li><li><span class="arithmatex">\(A\)</span> et <span class="arithmatex">\(B\)</span></li><li>ni <span class="arithmatex">\(A\)</span> ni <span class="arithmatex">\(B\)</span></li></ol></li>
<li value="5">Si <span class="arithmatex">\(P(A\cap B)=0{,}08\)</span>, <span class="arithmatex">\(P(A)=0{,}2\)</span>, alors <span class="arithmatex">\(P_A(B)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(0{,}016\)</span></li><li><span class="arithmatex">\(0{,}4\)</span></li><li><span class="arithmatex">\(0{,}28\)</span></li><li><span class="arithmatex">\(2{,}5\)</span></li></ol></li>
<li value="6">Les probabilités totales servent à calculer<ol class="auto-choix" type="A"><li>une intersection</li><li>un complément</li><li>un événement par somme de cas</li><li>une moyenne</li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Repérer condition, intersection ou total.</li><li>Contrôler que le résultat est entre <span class="arithmatex">\(0\)</span> et <span class="arithmatex">\(1\)</span>.</li><li>Les QCM de probas se gagnent avec les notations.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>L'ordre de la condition change le calcul.</li><li>Une probabilité supérieure à <span class="arithmatex">\(1\)</span> est impossible.</li></ul>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(\dfrac{P(A\cap B)}{P(A)}\)</span></li>
    <li value="2"><strong class="auto-resultat">Réponse C</strong> : car <span class="arithmatex">\(0{,}4\times0{,}5=0{,}2\)</span>.</li>
    <li value="3"><strong class="auto-resultat">Réponse A</strong> : s'additionnent à <span class="arithmatex">\(1\)</span></li>
    <li value="4"><strong class="auto-resultat">Réponse C</strong> : <span class="arithmatex">\(A\)</span> et <span class="arithmatex">\(B\)</span></li>
    <li value="5"><strong class="auto-resultat">Réponse B</strong> : car <span class="arithmatex">\(0{,}08/0{,}2=0{,}4\)</span>.</li>
    <li value="6"><strong class="auto-resultat">Réponse C</strong> : un événement par somme de cas</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Formule conditionnelle puis contrôle de cohérence. Sur un arbre : multiplier les chemins, additionner les cas.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Ne pas mélanger union et intersection.</div>

---

*Ces questions reprennent le diaporama d'automatismes N22 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
