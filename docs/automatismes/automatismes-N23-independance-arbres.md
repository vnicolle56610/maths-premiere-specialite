---
title: "Automatismes Première spécialité – Indépendance et arbres : exercices et QCM corrigés"
description: "24 questions d'automatismes de Première spécialité (indépendance et arbres), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N23 — Indépendance et arbres

24 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N23-independance-arbres.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N23_INDEPENDANCE_ARBRES.pdf){ .md-button }
[📖 Revoir la notion](../notions/N23-independance-arbres.md){ .md-button }
</div>

## Série A — 

<div class="auto-consigne" markdown>
**Consigne.** Reconnaître et utiliser rapidement l\'indépendance de deux événements.
</div>

<ol class="auto-questions">
<li value="1">Si <span class="arithmatex">\(P(A)=0{,}4\)</span>, <span class="arithmatex">\(P(B)=0{,}5\)</span> et <span class="arithmatex">\(A\)</span> et <span class="arithmatex">\(B\)</span> sont indépendants, calculer <span class="arithmatex">\(P(A\cap B)\)</span>.</li>
<li value="2">Si <span class="arithmatex">\(P(A)=0{,}6\)</span>, <span class="arithmatex">\(P(A\cap B)=0{,}18\)</span> et <span class="arithmatex">\(A\)</span> et <span class="arithmatex">\(B\)</span> sont indépendants, calculer <span class="arithmatex">\(P(B)\)</span>.</li>
<li value="3">Si <span class="arithmatex">\(P(B)=0{,}7\)</span> et <span class="arithmatex">\(A\)</span> et <span class="arithmatex">\(B\)</span> sont indépendants, donner <span class="arithmatex">\(P_A(B)\)</span>.</li>
<li value="4">Si <span class="arithmatex">\(P_A(B)=0{,}25\)</span> et <span class="arithmatex">\(P(B)=0{,}25\)</span>, que peut-on conclure pour <span class="arithmatex">\(A\)</span> et <span class="arithmatex">\(B\)</span> ?</li>
<li value="5">Deux tirs indépendants réussissent chacun avec probabilité <span class="arithmatex">\(0{,}8\)</span>. Calculer la probabilité de deux réussites.</li>
<li value="6">Deux lancers indépendants donnent pile avec probabilité <span class="arithmatex">\(0{,}5\)</span>. Calculer la probabilité d'obtenir au moins un pile.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Indépendance : <span class="arithmatex">\(P(A\cap B)=P(A)P(B)\)</span>.</li><li>Comparer <span class="arithmatex">\(P_A(B)\)</span> à <span class="arithmatex">\(P(B)\)</span>.</li><li>Pour « au moins un », penser au complément.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Indépendance ne signifie pas événements incompatibles.</li><li>Vérifier que la probabilité obtenue est entre <span class="arithmatex">\(0\)</span> et <span class="arithmatex">\(1\)</span>.</li></ul>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(P(A\cap B)=\)</span><wbr><span class="arithmatex">\(0{,}4\times0{,}5=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}2}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(0{,}18=0{,}6P(B)\)</span>, donc <span class="arithmatex">\(P(B)=\boxed{0{,}3}\)</span>.</li>
    <li value="3">Par indépendance, <span class="arithmatex">\(P_A(B)=\)</span><wbr><span class="arithmatex">\(P(B)=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}7}\)</span>.</li>
    <li value="4">Si <span class="arithmatex">\(P(A)&gt;0\)</span>, alors <span class="arithmatex">\(P_A(B)=P(B)\)</span> : <strong class="auto-resultat"><span class="arithmatex">\(A\)</span> et <span class="arithmatex">\(B\)</span> sont indépendants</strong>.</li>
    <li value="5"><span class="arithmatex">\(0{,}8\times0{,}8=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}64}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(1-P(\text{aucun pile})=\)</span><wbr><span class="arithmatex">\(1-0{,}5^2=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}75}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Traduire l'indépendance par un produit. Utiliser le complément pour éviter de lister trop de cas.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Deux événements indépendants peuvent se produire ensemble.</div>

## Série B — 

<div class="auto-consigne" markdown>
**Consigne.** Exploiter un arbre pondéré avec deux niveaux.
</div>

<ol class="auto-questions">
<li value="1">On donne <span class="arithmatex">\(P(A)=0{,}3\)</span>, <span class="arithmatex">\(P_A(B)=0{,}6\)</span> et <span class="arithmatex">\(P_{\overline A}(B)=0{,}2\)</span>. Calculer <span class="arithmatex">\(P(A\cap B)\)</span>.</li>
<li value="2">Calculer <span class="arithmatex">\(P(\overline A\cap B)\)</span>.</li>
<li value="3">Calculer <span class="arithmatex">\(P(B)\)</span>.</li>
<li value="4">Calculer <span class="arithmatex">\(P(A\cap\overline B)\)</span>.</li>
<li value="5">Calculer <span class="arithmatex">\(P(\overline B)\)</span>.</li>
<li value="6">Calculer <span class="arithmatex">\(P_B(A)\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Sur une branche, multiplier les probabilités.</li><li>Pour <span class="arithmatex">\(P(B)\)</span>, additionner les chemins qui finissent par <span class="arithmatex">\(B\)</span>.</li><li>Une probabilité conditionnelle inverse nécessite une division.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas confondre <span class="arithmatex">\(P_A(B)\)</span> et <span class="arithmatex">\(P_B(A)\)</span>.</li><li>Un arbre pondéré doit avoir des branches complémentaires.</li></ul>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(P(A\cap B)=\)</span><wbr><span class="arithmatex">\(0{,}3\times0{,}6=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}18}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(P(\overline A\cap B)=\)</span><wbr><span class="arithmatex">\(0{,}7\times0{,}2=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}14}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(P(B)=\)</span><wbr><span class="arithmatex">\(0{,}18+0{,}14=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}32}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(P(A\cap\overline B)=\)</span><wbr><span class="arithmatex">\(0{,}3\times0{,}4=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}12}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(P(\overline B)=\)</span><wbr><span class="arithmatex">\(1-0{,}32=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}68}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(P_B(A)=\)</span><wbr><span class="arithmatex">\(\dfrac{0{,}18}{0{,}32}=\)</span><wbr><span class="arithmatex">\(\boxed{\dfrac{9}{16}}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Multiplier le long d'un chemin. Additionner les chemins incompatibles. Conditionner en divisant par la probabilité de la condition.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> La formule de Bayes est ici seulement la formule conditionnelle réorganisée.</div>

## Série C — 

<div class="auto-consigne" markdown>
**Consigne.** Travailler des épreuves répétées indépendantes.
</div>

<ol class="auto-questions">
<li value="1">Trois essais indépendants ont une probabilité de succès <span class="arithmatex">\(p=0{,}4\)</span>. Calculer la probabilité de <span class="arithmatex">\(SSS\)</span>.</li>
<li value="2">Calculer la probabilité de <span class="arithmatex">\(EEF\)</span>, où <span class="arithmatex">\(E\)</span> signifie échec et <span class="arithmatex">\(S\)</span> succès.</li>
<li value="3">Calculer la probabilité d'obtenir exactement un succès.</li>
<li value="4">Calculer la probabilité d'obtenir aucun succès.</li>
<li value="5">Calculer la probabilité d'obtenir au moins un succès.</li>
<li value="6">Combien de chemins donnent exactement deux succès en trois essais ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Chaque chemin a une probabilité obtenue par produit.</li><li>Compter les chemins ayant le même nombre de succès.</li><li>« Au moins un » se traite souvent par le complément.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Les chemins <span class="arithmatex">\(SSE\)</span>, <span class="arithmatex">\(SES\)</span>, <span class="arithmatex">\(ESS\)</span> sont différents.</li><li>L'indépendance autorise le produit des probabilités.</li></ul>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(P(SSS)=\)</span><wbr><span class="arithmatex">\(0{,}4^3=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}064}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(P(EES)=\)</span><wbr><span class="arithmatex">\(0{,}6\times0{,}6\times0{,}4=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}144}\)</span>.</li>
    <li value="3">Il y a 3 chemins : <span class="arithmatex">\(3\times0{,}4\times0{,}6^2=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}432}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(P(EEE)=\)</span><wbr><span class="arithmatex">\(0{,}6^3=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}216}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(1-P(EEE)=\)</span><wbr><span class="arithmatex">\(1-0{,}216=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}784}\)</span>.</li>
    <li value="6">Les chemins <span class="arithmatex">\(SSE\)</span>, <span class="arithmatex">\(SES\)</span>, <span class="arithmatex">\(ESS\)</span> : <span class="arithmatex">\(\boxed{3 chemins}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Produit sur un chemin ; somme sur plusieurs chemins. Pour 3 essais, on peut lister rapidement les chemins.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Ne pas oublier le coefficient de comptage.</div>

## Série D — 

<div class="auto-consigne" markdown>
**Consigne.** Choisir rapidement la bonne réponse. Une seule réponse correcte.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(A\)</span> et <span class="arithmatex">\(B\)</span> indépendants, <span class="arithmatex">\(P(A)=0{,}2\)</span>, <span class="arithmatex">\(P(B)=0{,}6\)</span>. <span class="arithmatex">\(P(A\cap B)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(0{,}8\)</span></li><li><span class="arithmatex">\(0{,}12\)</span></li><li><span class="arithmatex">\(0{,}4\)</span></li><li><span class="arithmatex">\(0{,}3\)</span></li></ol></li>
<li value="2">Si <span class="arithmatex">\(P_A(B)=P(B)\)</span>, alors<ol class="auto-choix" type="A"><li><span class="arithmatex">\(A=B\)</span></li><li><span class="arithmatex">\(A\)</span> et <span class="arithmatex">\(B\)</span> incompatibles</li><li><span class="arithmatex">\(A\)</span> et <span class="arithmatex">\(B\)</span> indépendants</li><li><span class="arithmatex">\(B=\overline A\)</span></li></ol></li>
<li value="3">Sur un arbre, la probabilité d'un chemin s'obtient par<ol class="auto-choix" type="A"><li>somme</li><li>produit</li><li>quotient</li><li>complément</li></ol></li>
<li value="4">Si deux événements sont incompatibles et de probabilités non nulles, ils sont<ol class="auto-choix" type="A"><li>indépendants</li><li>non indépendants</li><li>complémentaires</li><li>certains</li></ol></li>
<li value="5">Deux essais indépendants, <span class="arithmatex">\(p=0{,}3\)</span>. Probabilité de deux succès :<ol class="auto-choix" type="A"><li><span class="arithmatex">\(0{,}6\)</span></li><li><span class="arithmatex">\(0{,}09\)</span></li><li><span class="arithmatex">\(0{,}49\)</span></li><li><span class="arithmatex">\(0{,}21\)</span></li></ol></li>
<li value="6"><span class="arithmatex">\(P(A\cap B)=0{,}08\)</span>, <span class="arithmatex">\(P(B)=0{,}4\)</span>. <span class="arithmatex">\(P_B(A)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(0{,}32\)</span></li><li><span class="arithmatex">\(0{,}2\)</span></li><li><span class="arithmatex">\(0{,}48\)</span></li><li><span class="arithmatex">\(5\)</span></li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Identifier la formule avant de calculer.</li><li>Tester la cohérence des réponses proposées.</li><li>Un QCM se résout vite, mais pas au hasard.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Une incompatibilité non triviale empêche l'indépendance.</li><li>Une probabilité conditionnelle est un quotient.</li></ul>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(0{,}12\)</span></li>
    <li value="2"><strong class="auto-resultat">Réponse C</strong> : <span class="arithmatex">\(A\)</span> et <span class="arithmatex">\(B\)</span> indépendants</li>
    <li value="3"><strong class="auto-resultat">Réponse B</strong> : produit</li>
    <li value="4"><strong class="auto-resultat">Réponse B</strong> : car <span class="arithmatex">\(P(A\cap B)=\)</span><wbr><span class="arithmatex">\(0\neq P(A)P(B)\)</span>.</li>
    <li value="5"><strong class="auto-resultat">Réponse B</strong> : car <span class="arithmatex">\(0{,}3^2=0{,}09\)</span>.</li>
    <li value="6"><strong class="auto-resultat">Réponse B</strong> : car <span class="arithmatex">\(0{,}08/0{,}4=0{,}2\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Traduire l'énoncé en formule. Écarter les réponses impossibles ou incohérentes.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Indépendance et incompatibilité sont deux idées différentes.</div>

---

*Ces questions reprennent le diaporama d'automatismes N23 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
