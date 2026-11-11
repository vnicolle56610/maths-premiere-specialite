---
title: "Automatismes Première spécialité – Variables aléatoires et espérance : exercices et QCM corrigés"
description: "24 questions d'automatismes de Première spécialité (variables aléatoires et espérance), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N24 — Variables aléatoires et espérance

24 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N24-variables-aleatoires-esperance.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N24_VARIABLES_ALEATOIRES_ESPERANCE.pdf){ .md-button }
[📖 Revoir la notion](../notions/N24-variables-aleatoires-esperance.md){ .md-button }
</div>

## Série A — 

<div class="auto-consigne" markdown>
**Consigne.** Lire une loi de probabilité et calculer ses premiers indicateurs.
</div>

<ol class="auto-questions">
<li value="1">Une variable aléatoire <span class="arithmatex">\(X\)</span> prend les valeurs <span class="arithmatex">\(0;1;2\)</span> avec probabilités <span class="arithmatex">\(0{,}2\)</span> ; <span class="arithmatex">\(0{,}5\)</span> ; <span class="arithmatex">\(0{,}3\)</span>. Calculer <span class="arithmatex">\(P(X\geqslant1)\)</span>.</li>
<li value="2">Calculer <span class="arithmatex">\(E(X)\)</span>.</li>
<li value="3">Calculer <span class="arithmatex">\(E(X^2)\)</span>.</li>
<li value="4">Calculer <span class="arithmatex">\(V(X)\)</span>.</li>
<li value="5">Donner une valeur approchée de <span class="arithmatex">\(\sigma(X)\)</span> au centième.</li>
<li value="6">Interpréter <span class="arithmatex">\(E(X)\)</span> en une phrase courte.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Vérifier que les probabilités totalisent <span class="arithmatex">\(1\)</span>.</li><li><span class="arithmatex">\(E(X)=\sum x_i p_i\)</span>.</li><li><span class="arithmatex">\(V(X)=E(X^2)-E(X)^2\)</span>.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas confondre <span class="arithmatex">\(E(X^2)\)</span> et <span class="arithmatex">\(E(X)^2\)</span>.</li><li>L'espérance n'est pas forcément une valeur prise par <span class="arithmatex">\(X\)</span>.</li></ul>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(P(X\geqslant1)=\)</span><wbr><span class="arithmatex">\(0{,}5+0{,}3=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}8}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(E(X)=\)</span><wbr><span class="arithmatex">\(0\times0{,}2+1\times0{,}5+2\times0{,}3=\)</span><wbr><span class="arithmatex">\(\boxed{1{,}1}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(E(X^2)=\)</span><wbr><span class="arithmatex">\(0+1^2\times0{,}5+2^2\times0{,}3=\)</span><wbr><span class="arithmatex">\(\boxed{1{,}7}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(V(X)=\)</span><wbr><span class="arithmatex">\(1{,}7-1{,}1^2=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}49}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(\sigma(X)=\)</span><wbr><span class="arithmatex">\(\sqrt{0{,}49}=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}70}\)</span>.</li>
    <li value="6">Sur un grand nombre d'expériences, la moyenne attendue est <span class="arithmatex">\(\boxed{1{,}1}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Construire deux lignes : valeurs puis probabilités. Calculer séparément <span class="arithmatex">\(E(X)\)</span>, <span class="arithmatex">\(E(X^2)\)</span>, puis <span class="arithmatex">\(V(X)\)</span>.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> La variance mesure une dispersion, elle est positive.</div>

## Série B — 

<div class="auto-consigne" markdown>
**Consigne.** Compléter une loi puis calculer espérance et variance.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(X\)</span> prend les valeurs <span class="arithmatex">\(-1;0;3\)</span> avec probabilités <span class="arithmatex">\(0{,}25\)</span> ; <span class="arithmatex">\(p\)</span> ; <span class="arithmatex">\(0{,}35\)</span>. Calculer <span class="arithmatex">\(p\)</span>.</li>
<li value="2">Calculer <span class="arithmatex">\(P(X&gt;0)\)</span>.</li>
<li value="3">Calculer <span class="arithmatex">\(E(X)\)</span>.</li>
<li value="4">Calculer <span class="arithmatex">\(E(X^2)\)</span>.</li>
<li value="5">Calculer <span class="arithmatex">\(V(X)\)</span>.</li>
<li value="6">Donner une valeur approchée de l'écart type au centième.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>La somme des probabilités vaut <span class="arithmatex">\(1\)</span>.</li><li>Les valeurs négatives comptent dans l'espérance.</li><li>Les carrés sont toujours positifs dans <span class="arithmatex">\(E(X^2)\)</span>.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas supprimer le signe moins de la valeur <span class="arithmatex">\(-1\)</span>.</li><li>Ne pas arrondir trop tôt.</li></ul>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(p=\)</span><wbr><span class="arithmatex">\(1-0{,}25-0{,}35=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}40}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(P(X&gt;0)=\)</span><wbr><span class="arithmatex">\(P(X=\)</span><wbr><span class="arithmatex">\(3)=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}35}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(E(X)=\)</span><wbr><span class="arithmatex">\(-1\times0{,}25+3\times0{,}35=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}80}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(E(X^2)=\)</span><wbr><span class="arithmatex">\(1\times0{,}25+9\times0{,}35=\)</span><wbr><span class="arithmatex">\(\boxed{3{,}40}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(V(X)=\)</span><wbr><span class="arithmatex">\(3{,}40-0{,}80^2=\)</span><wbr><span class="arithmatex">\(\boxed{2{,}76}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(\sigma(X)=\)</span><wbr><span class="arithmatex">\(\sqrt{2{,}76}\approx\boxed{1{,}66}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Compléter la loi avant tout calcul. Appliquer <span class="arithmatex">\(V(X)=E(X^2)-E(X)^2\)</span>.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Une espérance peut être positive même si une valeur est négative.</div>

## Série C — 

<div class="auto-consigne" markdown>
**Consigne.** Modéliser rapidement un gain algébrique par une variable aléatoire.
</div>

<ol class="auto-questions">
<li value="1">Un jeu coûte <span class="arithmatex">\(2\)</span> euros. Avec probabilité <span class="arithmatex">\(0{,}2\)</span>, on gagne <span class="arithmatex">\(10\)</span> euros, sinon on ne gagne rien. Donner les valeurs du gain algébrique <span class="arithmatex">\(G\)</span>.</li>
<li value="2">Donner la loi de <span class="arithmatex">\(G\)</span>.</li>
<li value="3">Calculer <span class="arithmatex">\(E(G)\)</span>.</li>
<li value="4">Le jeu est-il favorable au joueur ?</li>
<li value="5">Calculer <span class="arithmatex">\(P(G&gt;0)\)</span>.</li>
<li value="6">On double la mise gagnante : le gain brut devient <span class="arithmatex">\(20\)</span> euros. Donner la nouvelle espérance.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Gain algébrique = gain reçu moins coût payé.</li><li>Un jeu favorable a une espérance positive.</li><li>Garder le signe du gain négatif.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas confondre gain brut et gain algébrique.</li><li>Une probabilité faible peut être compensée par un gain élevé.</li></ul>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(G=8\)</span> en cas de gain brut <span class="arithmatex">\(10\)</span>, et <span class="arithmatex">\(G=-2\)</span> sinon : <strong class="auto-resultat"><span class="arithmatex">\(8\)</span> et <span class="arithmatex">\(-2\)</span></strong>.</li>
    <li value="2"><span class="arithmatex">\(P(G=8)=0{,}2\)</span> et <span class="arithmatex">\(P(G=-2)=0{,}8\)</span>.</li>
    <li value="3"><span class="arithmatex">\(E(G)=\)</span><wbr><span class="arithmatex">\(8\times0{,}2+(-2)\times0{,}8=\)</span><wbr><span class="arithmatex">\(\boxed{0}\)</span>.</li>
    <li value="4">L'espérance est nulle : <span class="arithmatex">\(\boxed{jeu équilibré}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(P(G&gt;0)=\)</span><wbr><span class="arithmatex">\(P(G=\)</span><wbr><span class="arithmatex">\(8)=\)</span><wbr><span class="arithmatex">\(\boxed{0{,}2}\)</span>.</li>
    <li value="6">Nouvelle espérance : <span class="arithmatex">\(18\times0{,}2+(-2)\times0{,}8=\)</span><wbr><span class="arithmatex">\(\boxed{2}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Identifier d'abord les valeurs possibles du gain algébrique. Calculer l'espérance pour juger le jeu.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Un jeu peut être souvent perdant mais favorable en moyenne.</div>

## Série D — 

<div class="auto-consigne" markdown>
**Consigne.** Choisir rapidement la bonne réponse. Une seule réponse correcte.
</div>

<ol class="auto-questions">
<li value="1">Une loi de probabilité doit avoir une somme de probabilités égale à<ol class="auto-choix" type="A"><li><span class="arithmatex">\(0\)</span></li><li><span class="arithmatex">\(1\)</span></li><li><span class="arithmatex">\(100\)</span></li><li><span class="arithmatex">\(E(X)\)</span></li></ol></li>
<li value="2">Si <span class="arithmatex">\(X\)</span> vaut <span class="arithmatex">\(2\)</span> avec probabilité <span class="arithmatex">\(0{,}3\)</span> et <span class="arithmatex">\(5\)</span> avec probabilité <span class="arithmatex">\(0{,}7\)</span>, <span class="arithmatex">\(E(X)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(3{,}5\)</span></li><li><span class="arithmatex">\(4{,}1\)</span></li><li><span class="arithmatex">\(7\)</span></li><li><span class="arithmatex">\(0{,}21\)</span></li></ol></li>
<li value="3">La formule de la variance est<ol class="auto-choix" type="A"><li><span class="arithmatex">\(E(X^2)-E(X)^2\)</span></li><li><span class="arithmatex">\(E(X)^2-E(X^2)\)</span></li><li><span class="arithmatex">\(E(X^2)\)</span></li><li><span class="arithmatex">\(\sqrt{E(X)}\)</span></li></ol></li>
<li value="4">Un jeu est favorable au joueur si<ol class="auto-choix" type="A"><li><span class="arithmatex">\(E(G)&lt;0\)</span></li><li><span class="arithmatex">\(E(G)=0\)</span></li><li><span class="arithmatex">\(E(G)&gt;0\)</span></li><li><span class="arithmatex">\(P(G&gt;0)=1\)</span></li></ol></li>
<li value="5">L'écart type est<ol class="auto-choix" type="A"><li>la variance</li><li>la racine carrée de la variance</li><li>l'espérance</li><li>une probabilité</li></ol></li>
<li value="6">Si <span class="arithmatex">\(V(X)=0\)</span>, alors <span class="arithmatex">\(X\)</span> est<ol class="auto-choix" type="A"><li>toujours dispersée</li><li>constante presque sûrement</li><li>négative</li><li>impossible</li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Un QCM de variables aléatoires teste surtout les formules.</li><li>Identifier la grandeur : probabilité, espérance ou dispersion.</li><li>Contrôler l'unité : variance et écart type ne sont pas identiques.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>L'espérance peut ne pas être une valeur possible.</li><li>La variance ne peut pas être négative.</li></ul>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(1\)</span></li>
    <li value="2"><strong class="auto-resultat">Réponse B</strong> : car <span class="arithmatex">\(2\times0{,}3+5\times0{,}7=\)</span><wbr><span class="arithmatex">\(4{,}1\)</span>.</li>
    <li value="3"><strong class="auto-resultat">Réponse A</strong> : <span class="arithmatex">\(E(X^2)-E(X)^2\)</span></li>
    <li value="4"><strong class="auto-resultat">Réponse C</strong> : <span class="arithmatex">\(E(G)&gt;0\)</span></li>
    <li value="5"><strong class="auto-resultat">Réponse B</strong> : la racine carrée de la variance</li>
    <li value="6"><strong class="auto-resultat">Réponse B</strong> : constante presque sûrement</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Mémoriser la chaîne : loi <span class="arithmatex">\(\to\)</span> espérance <span class="arithmatex">\(\to\)</span> variance <span class="arithmatex">\(\to\)</span> écart type. Écarter toute variance négative.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Une espérance ne dit pas toute la dispersion.</div>

---

*Ces questions reprennent le diaporama d'automatismes N24 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
