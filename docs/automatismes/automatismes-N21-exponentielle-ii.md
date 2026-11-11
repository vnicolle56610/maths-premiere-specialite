---
title: "Automatismes Première spécialité – Exponentielle II : modèles : exercices et QCM corrigés"
description: "24 questions d'automatismes de Première spécialité (exponentielle II : modèles), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N21 — Exponentielle II : modèles

24 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N21-exponentielle-ii.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N21_EXPONENTIELLE_II_MODELES.pdf){ .md-button }
[📖 Revoir la notion](../notions/N21-exponentielle-ii.md){ .md-button }
</div>

## Série A — 

<div class="auto-consigne" markdown>
**Consigne.** Reconnaître le modèle et calculer un terme ou une valeur.
</div>

<ol class="auto-questions">
<li value="1">Suite géométrique : <span class="arithmatex">\(u_0=8\)</span>, <span class="arithmatex">\(u_{n+1}=1{,}2u_n\)</span>. Calculer <span class="arithmatex">\(u_2\)</span>.</li>
<li value="2">Modèle continu : <span class="arithmatex">\(f(t)=8e^{0{,}2t}\)</span>. Calculer <span class="arithmatex">\(f(0)\)</span>.</li>
<li value="3">Dans <span class="arithmatex">\(N(t)=50e^{-0{,}1t}\)</span>, le signe de <span class="arithmatex">\(-0{,}1\)</span> indique quoi ?</li>
<li value="4">Dans <span class="arithmatex">\(u_n=12\times 0{,}85^n\)</span>, le modèle est-il croissant ou décroissant ?</li>
<li value="5">Calculer <span class="arithmatex">\(e^0\)</span>.</li>
<li value="6">Simplifier <span class="arithmatex">\(e^{0{,}3t}e^{0{,}7t}\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Comparer le facteur <span class="arithmatex">\(q\)</span> à <span class="arithmatex">\(1\)</span>.</li><li>Dans <span class="arithmatex">\(e^{kt}\)</span>, le signe de <span class="arithmatex">\(k\)</span> donne le sens.</li><li>Au rang ou temps <span class="arithmatex">\(0\)</span>, on lit la valeur initiale.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas confondre <span class="arithmatex">\(q^n\)</span> et <span class="arithmatex">\(e^{kn}\)</span>.</li><li>Un coefficient négatif dans l'exposant donne une décroissance.</li></ul>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(u_1=9{,}6\)</span>, puis <span class="arithmatex">\(u_2=11{,}52\)</span>. <span class="arithmatex">\(\boxed{u_2=11{,}52}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(f(0)=8e^0=\boxed{8}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(-0{,}1&lt;0\)</span> : le modèle est <span class="arithmatex">\(\boxed{décroissant}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(0{,}85&lt;1\)</span>, donc <span class="arithmatex">\(\boxed{décroissant}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(\boxed{e^0=1}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(e^{0{,}3t}e^{0{,}7t}=\)</span><wbr><span class="arithmatex">\(e^t=\)</span><wbr><span class="arithmatex">\(\boxed{e^t}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Discret : suite géométrique <span class="arithmatex">\(u_n=u_0q^n\)</span>. Continu : exponentielle <span class="arithmatex">\(f(t)=Ce^{kt}\)</span>.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Comparer les paramètres, pas seulement les valeurs numériques.</div>

## Série B — 

<div class="auto-consigne" markdown>
**Consigne.** Passer d'une phrase à un coefficient multiplicateur ou à un modèle.
</div>

<ol class="auto-questions">
<li value="1">Augmenter de <span class="arithmatex">\(12\%\)</span> correspond à multiplier par ?</li>
<li value="2">Diminuer de <span class="arithmatex">\(7\%\)</span> correspond à multiplier par ?</li>
<li value="3">Un capital <span class="arithmatex">\(C_0=500\)</span> croît de <span class="arithmatex">\(4\%\)</span> par période. Donner <span class="arithmatex">\(C_n\)</span>.</li>
<li value="4">Une quantité vaut <span class="arithmatex">\(120e^{0{,}03t}\)</span>. Donner la valeur initiale.</li>
<li value="5">Pour <span class="arithmatex">\(f(t)=300e^{-0{,}04t}\)</span>, calculer <span class="arithmatex">\(f'(t)\)</span>.</li>
<li value="6">Le modèle <span class="arithmatex">\(f(t)=Ae^{kt}\)</span> est constant si quelle valeur de <span class="arithmatex">\(k\)</span> ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li><span class="arithmatex">\(p\%\)</span> d'augmentation : <span class="arithmatex">\(1+\frac{p}{100}\)</span>.</li><li>Diminution : <span class="arithmatex">\(1-\frac{p}{100}\)</span>.</li><li>La dérivée de <span class="arithmatex">\(Ae^{kt}\)</span> est <span class="arithmatex">\(Ak e^{kt}\)</span>.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Un taux négatif n'est pas un coefficient multiplicateur négatif.</li><li>La valeur initiale se lit en <span class="arithmatex">\(t=0\)</span>.</li></ul>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(1+0{,}12=\boxed{1{,}12}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(1-0{,}07=\boxed{0{,}93}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(\boxed{C_n=500\times1{,}04^n}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(120e^0=\boxed{120}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(f'(t)=\)</span><wbr><span class="arithmatex">\(300(-0{,}04)e^{-0{,}04t}=\)</span><wbr><span class="arithmatex">\(\boxed{-12e^{-0{,}04t}}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(\boxed{k=0}\)</span>, car <span class="arithmatex">\(e^{0t}=1\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Identifier valeur initiale et facteur ou taux. Dériver <span class="arithmatex">\(e^{kt}\)</span> : multiplier par <span class="arithmatex">\(k\)</span>.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Le modèle discret utilise une puissance <span class="arithmatex">\(n\)</span>, le continu une exponentielle en <span class="arithmatex">\(t\)</span>.</div>

## Série C — 

<div class="auto-consigne" markdown>
**Consigne.** Lire ou compléter mentalement des étapes d'algorithme de seuil.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(u_0=100\)</span>, <span class="arithmatex">\(u_{n+1}=0{,}8u_n\)</span>. Calculer <span class="arithmatex">\(u_1,u_2\)</span>.</li>
<li value="2">Avec <span class="arithmatex">\(u_0=100\)</span>, <span class="arithmatex">\(u_{n+1}=0{,}8u_n\)</span>, le seuil <span class="arithmatex">\(u_n&lt;50\)</span> est-il atteint pour <span class="arithmatex">\(n=2\)</span> ?</li>
<li value="3">Dans une boucle <code>while u &lt; 1000</code>, le test continue tant que ?</li>
<li value="4">Pour une croissance de <span class="arithmatex">\(15\%\)</span>, écrire la mise à jour de <span class="arithmatex">\(u\)</span>.</li>
<li value="5">Pour une décroissance de <span class="arithmatex">\(6\%\)</span>, écrire la mise à jour de <span class="arithmatex">\(u\)</span>.</li>
<li value="6">Si <span class="arithmatex">\(f(t)=40e^{0{,}05t}\)</span>, <span class="arithmatex">\(f\)</span> est-elle croissante ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Mettre à jour <span class="arithmatex">\(u\)</span>, puis augmenter le compteur.</li><li>Lire strictement le symbole du seuil.</li><li>Croissance si <span class="arithmatex">\(k&gt;0\)</span>.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas inverser la condition d'arrêt.</li><li>Un seuil peut être dépassé entre deux rangs entiers.</li></ul>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(u_1=80\)</span>, <span class="arithmatex">\(u_2=64\)</span>. <span class="arithmatex">\(\boxed{80;64}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(u_2=64&gt;50\)</span>, donc <span class="arithmatex">\(\boxed{non}\)</span>.</li>
    <li value="3">La boucle continue tant que <span class="arithmatex">\(\boxed{u&lt;1000}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(\boxed{\texttt{u = 1.15*u}}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(\boxed{\texttt{u = 0.94*u}}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(0{,}05&gt;0\)</span>, donc <span class="arithmatex">\(\boxed{oui}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Un algorithme de seuil répète : mise à jour, compteur, test. Pour <span class="arithmatex">\(Ae^{kt}\)</span>, le signe de <span class="arithmatex">\(k\)</span> donne le sens.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Ne pas confondre rang <span class="arithmatex">\(n\)</span> et valeur <span class="arithmatex">\(u_n\)</span>.</div>

## Série D — 

<div class="auto-consigne" markdown>
**Consigne.** Choisir la seule réponse correcte. Calculatrice interdite.
</div>

<ol class="auto-questions">
<li value="1">Une baisse de <span class="arithmatex">\(20\%\)</span> :<ol class="auto-choix" type="A"><li><span class="arithmatex">\(1{,}2\)</span></li><li><span class="arithmatex">\(0{,}8\)</span></li><li><span class="arithmatex">\(-0{,}2\)</span></li><li><span class="arithmatex">\(20\)</span></li></ol></li>
<li value="2"><span class="arithmatex">\(f(t)=7e^{-0{,}3t}\)</span> est<ol class="auto-choix" type="A"><li>croissante</li><li>décroissante</li><li>constante</li><li>négative</li></ol></li>
<li value="3">Valeur initiale de <span class="arithmatex">\(N(t)=25e^{0{,}4t}\)</span> :<ol class="auto-choix" type="A"><li><span class="arithmatex">\(0{,}4\)</span></li><li><span class="arithmatex">\(e\)</span></li><li><span class="arithmatex">\(25\)</span></li><li><span class="arithmatex">\(25e\)</span></li></ol></li>
<li value="4"><span class="arithmatex">\(u_n=6\times1{,}1^n\)</span> :<ol class="auto-choix" type="A"><li>discret</li><li>continu</li><li>affine</li><li>constant</li></ol></li>
<li value="5"><span class="arithmatex">\((e^{2t})'=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(e^{2t}\)</span></li><li><span class="arithmatex">\(2e^{2t}\)</span></li><li><span class="arithmatex">\(te^{2t}\)</span></li><li><span class="arithmatex">\(2t\)</span></li></ol></li>
<li value="6">Croissance continue :<ol class="auto-choix" type="A"><li><span class="arithmatex">\(u_n=u_0q^n\)</span></li><li><span class="arithmatex">\(f(t)=Ce^{kt}\)</span></li><li><span class="arithmatex">\(f(x)=ax+b\)</span></li><li><span class="arithmatex">\(u_{n+1}=u_n+r\)</span></li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Chercher le type de modèle.</li><li>Regarder le signe du paramètre.</li><li>Répondre sans justification longue.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Une seule bonne réponse.</li><li>Le mot continu renvoie au temps réel <span class="arithmatex">\(t\)</span>.</li></ul>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse B</strong> : coefficient <span class="arithmatex">\(0{,}8\)</span>.</li>
    <li value="2"><strong class="auto-resultat">Réponse B</strong> : car <span class="arithmatex">\(-0{,}3&lt;0\)</span>.</li>
    <li value="3"><strong class="auto-resultat">Réponse C</strong> : car <span class="arithmatex">\(N(0)=25\)</span>.</li>
    <li value="4"><strong class="auto-resultat">Réponse A</strong> : rang entier <span class="arithmatex">\(n\)</span>.</li>
    <li value="5"><strong class="auto-resultat">Réponse B</strong> : dérivée de <span class="arithmatex">\(e^{2t}\)</span>.</li>
    <li value="6"><strong class="auto-resultat">Réponse B</strong> : modèle exponentiel continu.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Identifier discret/continu avant de calculer. Le coefficient multiplicateur est toujours positif.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Ne pas confondre taux et coefficient multiplicateur.</div>

---

*Ces questions reprennent le diaporama d'automatismes N21 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
