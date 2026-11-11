---
title: "Automatismes Première spécialité – Fonction exponentielle I : exercices et QCM corrigés"
description: "24 questions d'automatismes de Première spécialité (fonction exponentielle I), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N20 — Fonction exponentielle I

24 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N20-fonction-exponentielle.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N20_EXPONENTIELLE_I.pdf){ .md-button }
[📖 Revoir la notion](../notions/N20-fonction-exponentielle.md){ .md-button }
</div>

## Série A — 

<div class="auto-consigne" markdown>
**Consigne.** Calculer rapidement. Réduire les expressions avec les propriétés de l'exponentielle.
</div>

<ol class="auto-questions">
<li value="1">Simplifier : <span class="arithmatex">\(e^3\times e^5\)</span>.</li>
<li value="2">Simplifier : <span class="arithmatex">\(\dfrac{e^7}{e^2}\)</span>.</li>
<li value="3">Simplifier : <span class="arithmatex">\((e^2)^4\)</span>.</li>
<li value="4">Écrire sans quotient : <span class="arithmatex">\(\dfrac{1}{e^{-3}}\)</span>.</li>
<li value="5">Comparer à <span class="arithmatex">\(1\)</span> : <span class="arithmatex">\(e^0\)</span>.</li>
<li value="6">Résoudre : <span class="arithmatex">\(e^x=1\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Additionner les exposants dans un produit.</li><li>Soustraire les exposants dans un quotient.</li><li>Utiliser <span class="arithmatex">\(e^0=1\)</span>.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas écrire <span class="arithmatex">\(e^a+e^b=e^{a+b}\)</span>.</li><li>La fonction exponentielle est strictement positive.</li></ul>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(e^3\times e^5=\)</span><wbr><span class="arithmatex">\(e^{3+5}=\)</span><wbr><span class="arithmatex">\(\boxed{e^8}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(\dfrac{e^7}{e^2}=\)</span><wbr><span class="arithmatex">\(e^{7-2}=\)</span><wbr><span class="arithmatex">\(\boxed{e^5}\)</span>.</li>
    <li value="3"><span class="arithmatex">\((e^2)^4=\)</span><wbr><span class="arithmatex">\(e^{2\times 4}=\)</span><wbr><span class="arithmatex">\(\boxed{e^8}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(\dfrac{1}{e^{-3}}=\)</span><wbr><span class="arithmatex">\(e^3=\)</span><wbr><span class="arithmatex">\(\boxed{e^3}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(e^0=\boxed{1}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(e^x=1=e^0\)</span>, donc <span class="arithmatex">\(\boxed{x=0}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Produit : <span class="arithmatex">\(e^a e^b=e^{a+b}\)</span>. Quotient : <span class="arithmatex">\(\dfrac{e^a}{e^b}=e^{a-b}\)</span>. Égalité : <span class="arithmatex">\(e^u=e^v\Longleftrightarrow\)</span><wbr><span class="arithmatex">\( u=v\)</span>.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Les propriétés portent sur les produits, pas sur les sommes.</div>

## Série B — 

<div class="auto-consigne" markdown>
**Consigne.** Donner la dérivée de chaque fonction sur <span class="arithmatex">\(\mathbb R\)</span>.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(f(x)=e^x+3x\)</span>.</li>
<li value="2"><span class="arithmatex">\(g(x)=5e^x-2\)</span>.</li>
<li value="3"><span class="arithmatex">\(h(x)=xe^x\)</span>.</li>
<li value="4"><span class="arithmatex">\(p(x)=(x^2+1)e^x\)</span>.</li>
<li value="5"><span class="arithmatex">\(q(x)=e^x(2x-3)\)</span>.</li>
<li value="6"><span class="arithmatex">\(r(x)=e^x-x^2\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Dérivée de <span class="arithmatex">\(e^x\)</span> : elle-même.</li><li>Pour un produit, utiliser <span class="arithmatex">\((uv)'=u'v+uv'\)</span>.</li><li>Réduire seulement si c'est lisible.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas oublier la dérivée de <span class="arithmatex">\(x\)</span> dans un produit.</li><li>Une constante seule a une dérivée nulle.</li></ul>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(f'(x)=\)</span><wbr><span class="arithmatex">\(e^x+3=\)</span><wbr><span class="arithmatex">\(\boxed{e^x+3}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(g'(x)=5e^x=\boxed{5e^x}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(h'(x)=\)</span><wbr><span class="arithmatex">\(1\cdot e^x+x e^x=\)</span><wbr><span class="arithmatex">\(\boxed{(x+1)e^x}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(p'(x)=\)</span><wbr><span class="arithmatex">\(2xe^x+(x^2+1)e^x=\)</span><wbr><span class="arithmatex">\(\boxed{(x^2+2x+1)e^x}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(q'(x)=\)</span><wbr><span class="arithmatex">\(e^x(2x-3)+2e^x=\)</span><wbr><span class="arithmatex">\(\boxed{(2x-1)e^x}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(r'(x)=\boxed{e^x-2x}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Identifier somme, produit ou constante. Factoriser par <span class="arithmatex">\(e^x\)</span> quand cela simplifie le signe.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> <span class="arithmatex">\(e^x&gt;0\)</span>, donc le signe de <span class="arithmatex">\(P(x)e^x\)</span> est celui de <span class="arithmatex">\(P(x)\)</span>.</div>

## Série C — 

<div class="auto-consigne" markdown>
**Consigne.** Utiliser le signe de <span class="arithmatex">\(e^x\)</span> pour déduire un signe ou une variation.
</div>

<ol class="auto-questions">
<li value="1">Signe de <span class="arithmatex">\(3e^x\)</span> sur <span class="arithmatex">\(\mathbb R\)</span>.</li>
<li value="2">Signe de <span class="arithmatex">\(-2e^x\)</span> sur <span class="arithmatex">\(\mathbb R\)</span>.</li>
<li value="3">Signe de <span class="arithmatex">\((x-4)e^x\)</span>.</li>
<li value="4">Variation de <span class="arithmatex">\(f(x)=e^x-5\)</span>.</li>
<li value="5">Si <span class="arithmatex">\(g'(x)=(2x-6)e^x\)</span>, donner le signe de <span class="arithmatex">\(g'(x)\)</span>.</li>
<li value="6">Si <span class="arithmatex">\(h'(x)=-(x+1)e^x\)</span>, <span class="arithmatex">\(h\)</span> est croissante sur quel intervalle ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Commencer par <span class="arithmatex">\(e^x&gt;0\)</span>.</li><li>Un facteur positif ne change pas le signe.</li><li>Traduire le signe de la dérivée en variation.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas chercher les zéros de <span class="arithmatex">\(e^x\)</span> : il n'en a pas.</li><li>Un signe négatif devant change le sens.</li></ul>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(e^x&gt;0\)</span>, donc <span class="arithmatex">\(3e^x\)</span> est <span class="arithmatex">\(\boxed{strictement positif}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(-2e^x\)</span> est <span class="arithmatex">\(\boxed{strictement négatif}\)</span>.</li>
    <li value="3">Le signe est celui de <span class="arithmatex">\(x-4\)</span> : négatif si <span class="arithmatex">\(x&lt;4\)</span>, nul en <span class="arithmatex">\(4\)</span>, positif si <span class="arithmatex">\(x&gt;4\)</span>.</li>
    <li value="4"><span class="arithmatex">\(f'(x)=e^x&gt;0\)</span>, donc <span class="arithmatex">\(f\)</span> est <span class="arithmatex">\(\boxed{strictement croissante}\)</span>.</li>
    <li value="5">Signe de <span class="arithmatex">\(2x-6\)</span> : négatif si <span class="arithmatex">\(x&lt;3\)</span>, nul en <span class="arithmatex">\(3\)</span>, positif si <span class="arithmatex">\(x&gt;3\)</span>.</li>
    <li value="6"><span class="arithmatex">\(h'(x)\geqslant0 \Longleftrightarrow\)</span><wbr><span class="arithmatex">\( -(x+1)\geqslant0 \Longleftrightarrow\)</span><wbr><span class="arithmatex">\( x\leqslant -1\)</span>. Donc <span class="arithmatex">\(\boxed{]-\infty;-1]}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Factoriser par <span class="arithmatex">\(e^x\)</span>, toujours positif. Lire le signe du facteur restant.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Un extremum peut apparaître quand la dérivée change de signe.</div>

## Série D — 

<div class="auto-consigne" markdown>
**Consigne.** Choisir la seule réponse correcte. Aucune justification demandée.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(e^2e^{-5}=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(e^{-10}\)</span></li><li><span class="arithmatex">\(e^{-3}\)</span></li><li><span class="arithmatex">\(e^7\)</span></li><li><span class="arithmatex">\(-e^3\)</span></li></ol></li>
<li value="2">La dérivée de <span class="arithmatex">\(4e^x-x\)</span> est<ol class="auto-choix" type="A"><li><span class="arithmatex">\(4e^x\)</span></li><li><span class="arithmatex">\(4e^x-1\)</span></li><li><span class="arithmatex">\(e^x-1\)</span></li><li><span class="arithmatex">\(4e^{x-1}\)</span></li></ol></li>
<li value="3"><span class="arithmatex">\(e^x&gt;0\)</span> sur <span class="arithmatex">\(\mathbb R\)</span> :<ol class="auto-choix" type="A"><li>vrai</li><li>faux</li><li>seulement si <span class="arithmatex">\(x&gt;0\)</span></li><li>seulement si <span class="arithmatex">\(x\geqslant0\)</span></li></ol></li>
<li value="4">Si <span class="arithmatex">\(f'(x)=(x-2)e^x\)</span>, <span class="arithmatex">\(f\)</span> décroît sur<ol class="auto-choix" type="A"><li><span class="arithmatex">\(]-\infty;2]\)</span></li><li><span class="arithmatex">\([2;+\infty[\)</span></li><li><span class="arithmatex">\(\mathbb R\)</span></li><li><span class="arithmatex">\(\varnothing\)</span></li></ol></li>
<li value="5"><span class="arithmatex">\(\dfrac{e^6}{e^8}=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(e^2\)</span></li><li><span class="arithmatex">\(e^{-2}\)</span></li><li><span class="arithmatex">\(e^{48}\)</span></li><li><span class="arithmatex">\(\dfrac{6}{8}\)</span></li></ol></li>
<li value="6">L'équation <span class="arithmatex">\(e^x=e^4\)</span> a pour solution<ol class="auto-choix" type="A"><li><span class="arithmatex">\(0\)</span></li><li><span class="arithmatex">\(1\)</span></li><li><span class="arithmatex">\(4\)</span></li><li><span class="arithmatex">\(e^4\)</span></li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Repérer la propriété utile avant de calculer.</li><li>Éliminer les réponses impossibles.</li><li>Toujours penser à <span class="arithmatex">\(e^x&gt;0\)</span>.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Une seule réponse correcte.</li><li>Le signe de <span class="arithmatex">\(e^x\)</span> ne dépend pas de <span class="arithmatex">\(x\)</span>.</li></ul>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse B</strong> : car <span class="arithmatex">\(e^2e^{-5}=e^{-3}\)</span>.</li>
    <li value="2"><strong class="auto-resultat">Réponse B</strong> : car <span class="arithmatex">\((4e^x-x)'=4e^x-1\)</span>.</li>
    <li value="3"><strong class="auto-resultat">Réponse A</strong> : car <span class="arithmatex">\(e^x&gt;0\)</span> pour tout réel <span class="arithmatex">\(x\)</span>.</li>
    <li value="4"><strong class="auto-resultat">Réponse A</strong> : car le signe est celui de <span class="arithmatex">\(x-2\)</span>.</li>
    <li value="5"><strong class="auto-resultat">Réponse B</strong> : car <span class="arithmatex">\(\dfrac{e^6}{e^8}=e^{-2}\)</span>.</li>
    <li value="6"><strong class="auto-resultat">Réponse C</strong> : car <span class="arithmatex">\(e^x=e^4\Longleftrightarrow\)</span><wbr><span class="arithmatex">\( x=4\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Réponses rapides : propriété puis décision. Pour une dérivée factorisée par <span class="arithmatex">\(e^x\)</span>, regarder l'autre facteur.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Ne jamais remplacer <span class="arithmatex">\(e^x\)</span> par <span class="arithmatex">\(x\)</span>.</div>

---

*Ces questions reprennent le diaporama d'automatismes N20 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
