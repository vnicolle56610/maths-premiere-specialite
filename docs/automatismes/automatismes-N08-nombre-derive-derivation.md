---
title: "Automatismes Première spécialité – Nombre dérivé et dérivation : exercices et QCM corrigés"
description: "24 questions d'automatismes de Première spécialité (nombre dérivé et dérivation), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N08 — Nombre dérivé et dérivation

24 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N08-nombre-derive-derivation.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N08_NOMBRE_DERIVE_DERIVATION.pdf){ .md-button }
[📖 Revoir la notion](../notions/N08-nombre-derive-derivation.md){ .md-button }
</div>

## Série A — Réactiver pentes et calculs

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Répondre rapidement. Écrire seulement les étapes utiles.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(f(x)=x^2\)</span>. Taux de variation entre <span class="arithmatex">\(1\)</span> et <span class="arithmatex">\(3\)</span>.</li>
<li value="2"><span class="arithmatex">\(g(x)=2x+5\)</span>. Taux de variation entre <span class="arithmatex">\(-2\)</span> et <span class="arithmatex">\(4\)</span>.</li>
<li value="3">Droite de pente <span class="arithmatex">\(4\)</span> passant par <span class="arithmatex">\(A(1;3)\)</span> : donner une équation.</li>
<li value="4">Développer puis réduire <span class="arithmatex">\((x+1)^2-x^2\)</span>.</li>
<li value="5">Résoudre <span class="arithmatex">\(3x-6=0\)</span>.</li>
<li value="6">Factoriser <span class="arithmatex">\(x^2-4\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Un taux de variation est un quotient.</li><li>Pour une droite, la pente est le coefficient directeur.</li><li>Surveiller les identités remarquables.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas confondre image et antécédent.</li><li>Dans une équation de droite, <span class="arithmatex">\(x\)</span> et <span class="arithmatex">\(y\)</span> sont des nombres.</li></ul>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(\dfrac{f(3)-f(1)}{3-1}=\)</span><wbr><span class="arithmatex">\(\dfrac{9-1}{2}=\)</span><wbr><span class="arithmatex">\(\boxed{4}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(\dfrac{g(4)-g(-2)}{4-(-2)}=\)</span><wbr><span class="arithmatex">\(\dfrac{13-1}{6}=\)</span><wbr><span class="arithmatex">\(\boxed{2}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(y=4x+b\)</span>. Or <span class="arithmatex">\(3=4\times1+b\)</span>, donc <span class="arithmatex">\(b=-1\)</span>. <span class="arithmatex">\(\boxed{y=4x-1}\)</span>.</li>
    <li value="4"><span class="arithmatex">\((x+1)^2-x^2=\)</span><wbr><span class="arithmatex">\(x^2+2x+1-x^2=\)</span><wbr><span class="arithmatex">\(\boxed{2x+1}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(3x-6=0 \iff\)</span><wbr><span class="arithmatex">\( 3x=6 \iff\)</span><wbr><span class="arithmatex">\( \boxed{x=2}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(x^2-4=\)</span><wbr><span class="arithmatex">\(x^2-2^2=\)</span><wbr><span class="arithmatex">\(\boxed{(x-2)(x+2)}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> La pente entre deux points est une variation verticale divisée par une variation horizontale.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Éviter l'expression « passer de l'autre côté » : on effectue la même opération sur les deux membres.</div>

## Série B — Nombre dérivé par calcul

<p class="auto-meta">⏱ 7 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Utiliser le quotient <span class="arithmatex">\(\dfrac{f(a+h)-f(a)}{h}\)</span>, avec <span class="arithmatex">\(h\neq0\)</span>.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(f(x)=x^2\)</span>. Simplifier <span class="arithmatex">\(\dfrac{f(2+h)-f(2)}{h}\)</span>.</li>
<li value="2">En déduire le nombre dérivé de <span class="arithmatex">\(f(x)=x^2\)</span> en <span class="arithmatex">\(2\)</span>.</li>
<li value="3"><span class="arithmatex">\(g(x)=x^2+3x\)</span>. Simplifier <span class="arithmatex">\(\dfrac{g(1+h)-g(1)}{h}\)</span>.</li>
<li value="4">En déduire le nombre dérivé de <span class="arithmatex">\(g\)</span> en <span class="arithmatex">\(1\)</span>.</li>
<li value="5">Pour <span class="arithmatex">\(f(x)=x^2\)</span>, donner le coefficient directeur de la tangente en <span class="arithmatex">\(2\)</span>.</li>
<li value="6">Pour <span class="arithmatex">\(f(x)=x^2\)</span>, donner l'équation réduite de la tangente en <span class="arithmatex">\(2\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Développer seulement ce qui est nécessaire.</li><li>Factoriser par <span class="arithmatex">\(h\)</span>, puis simplifier.</li><li>Le nombre dérivé est un nombre réel.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>On simplifie par <span class="arithmatex">\(h\)</span> seulement car <span class="arithmatex">\(h\neq0\)</span>.</li><li>La limite est prise quand <span class="arithmatex">\(h\)</span> se rapproche de <span class="arithmatex">\(0\)</span>.</li></ul>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(\dfrac{(2+h)^2-4}{h}=\)</span><wbr><span class="arithmatex">\(\dfrac{4+4h+h^2-4}{h}=\)</span><wbr><span class="arithmatex">\(\boxed{4+h}\)</span>.</li>
    <li value="2">Quand <span class="arithmatex">\(h\)</span> tend vers <span class="arithmatex">\(0\)</span>, <span class="arithmatex">\(4+h\)</span> tend vers <span class="arithmatex">\(\boxed{4}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(g(1+h)=\)</span><wbr><span class="arithmatex">\(1+2h+h^2+3+3h=\)</span><wbr><span class="arithmatex">\(4+5h+h^2\)</span>, donc le quotient vaut <span class="arithmatex">\(\boxed{5+h}\)</span>.</li>
    <li value="4">Quand <span class="arithmatex">\(h\)</span> tend vers <span class="arithmatex">\(0\)</span>, <span class="arithmatex">\(5+h\)</span> tend vers <span class="arithmatex">\(\boxed{5}\)</span>.</li>
    <li value="5">Le coefficient directeur de la tangente est le nombre dérivé : <span class="arithmatex">\(\boxed{4}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(y=f(2)+4(x-2)=4+4(x-2)\)</span>, donc <span class="arithmatex">\(\boxed{y=4x-4}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Le quotient mesure une pente moyenne. Le nombre dérivé est la pente limite de la tangente.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Une tangente est une droite : son équation met en relation deux nombres <span class="arithmatex">\(x\)</span> et <span class="arithmatex">\(y\)</span>.</div>

## Série C — Tangente et approximation locale

<p class="auto-meta">⏱ 7 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Passer de <span class="arithmatex">\(f(a)\)</span> et <span class="arithmatex">\(f'(a)\)</span> à une tangente ou à une approximation.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(f(x)=x^2\)</span>. Équation de la tangente en <span class="arithmatex">\(a=3\)</span>.</li>
<li value="2"><span class="arithmatex">\(f(x)=x^2-4x\)</span>. Calculer <span class="arithmatex">\(f(2)\)</span> et interpréter <span class="arithmatex">\(f'(2)=0\)</span>.</li>
<li value="3">Approximer <span class="arithmatex">\(2{,}1^2\)</span> à l'aide de la tangente à <span class="arithmatex">\(x^2\)</span> en <span class="arithmatex">\(2\)</span>.</li>
<li value="4">On sait que <span class="arithmatex">\(f(1)=3\)</span> et <span class="arithmatex">\(f'(1)=-2\)</span>. Donner l'équation de la tangente en <span class="arithmatex">\(1\)</span>.</li>
<li value="5"><span class="arithmatex">\(u(x)=\dfrac{1}{x}\)</span>. Simplifier <span class="arithmatex">\(\dfrac{u(1+h)-u(1)}{h}\)</span>.</li>
<li value="6">En déduire le nombre dérivé de <span class="arithmatex">\(u(x)=\dfrac1x\)</span> en <span class="arithmatex">\(1\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Formule : <span class="arithmatex">\(y=f(a)+f'(a)(x-a)\)</span>.</li><li>Approximation : <span class="arithmatex">\(f(a+h)\approx f(a)+h f'(a)\)</span>.</li><li>Identifier la nature du résultat demandé.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Une approximation n'est pas une égalité exacte.</li><li>Pour <span class="arithmatex">\(1/x\)</span>, garder <span class="arithmatex">\(1+h\neq0\)</span>.</li></ul>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(f(3)=9\)</span> et <span class="arithmatex">\(f'(3)=6\)</span>. <span class="arithmatex">\(y=9+6(x-3)\)</span>, donc <span class="arithmatex">\(\boxed{y=6x-9}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(f(2)=4-8=-4\)</span>. Comme <span class="arithmatex">\(f'(2)=0\)</span>, la tangente est horizontale : <span class="arithmatex">\(\boxed{y=-4}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(2{,}1^2=\)</span><wbr><span class="arithmatex">\(f(2+0{,}1)\approx4+0{,}1\times4=\)</span><wbr><span class="arithmatex">\(\boxed{4{,}4}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(y=3-2(x-1)\)</span>, donc <span class="arithmatex">\(\boxed{y=-2x+5}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(\dfrac{\frac1{1+h}-1}{h}=\)</span><wbr><span class="arithmatex">\(\dfrac{\frac{-h}{1+h}}{h}=\)</span><wbr><span class="arithmatex">\(\boxed{-\dfrac1{1+h}}\)</span>.</li>
    <li value="6">Quand <span class="arithmatex">\(h\)</span> tend vers <span class="arithmatex">\(0\)</span>, <span class="arithmatex">\(-\dfrac1{1+h}\)</span> tend vers <span class="arithmatex">\(\boxed{-1}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> À proximité de <span class="arithmatex">\(a\)</span>, la courbe est approchée par sa tangente : <span class="arithmatex">\(f(a+h)\approx f(a)+h f'(a)\)</span>.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> La pente de tangente est un nombre réel ; l'équation de tangente décrit une droite.</div>

## Série D — Type épreuve anticipée : QCM

<p class="auto-meta">⏱ 5 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Choisir une seule réponse. Aucune justification n'est demandée.
</div>

<ol class="auto-questions">
<li value="1">Tangente en <span class="arithmatex">\(a\)</span>, pente <span class="arithmatex">\(5\)</span>. <span class="arithmatex">\(f'(a)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(0\)</span></li><li><span class="arithmatex">\(1\)</span></li><li><span class="arithmatex">\(5\)</span></li><li><span class="arithmatex">\(a\)</span></li></ol></li>
<li value="2"><span class="arithmatex">\(f(1)=4\)</span>, <span class="arithmatex">\(f'(1)=-3\)</span>. Tangente :<ol class="auto-choix" type="A"><li><span class="arithmatex">\(y=-3x+7\)</span> ;</li><li><span class="arithmatex">\(y=4x-3\)</span> ;</li><li><span class="arithmatex">\(y=-3x+1\)</span> ;</li><li><span class="arithmatex">\(y=x+4\)</span>.</li></ol></li>
<li value="3">Nombre dérivé en <span class="arithmatex">\(a\)</span> : limite de<ol class="auto-choix" type="A"><li><span class="arithmatex">\(\dfrac{f(a)}a\)</span> ;</li><li><span class="arithmatex">\(\dfrac{f(a+h)-f(a)}h\)</span> ;</li><li><span class="arithmatex">\(f(a+h)\)</span> ;</li><li><span class="arithmatex">\(f(h)-f(a)\)</span>.</li></ol></li>
<li value="4">Approximation locale :<ol class="auto-choix" type="A"><li><span class="arithmatex">\(f(a+h)\approx f(a)+h f'(a)\)</span> ;</li><li><span class="arithmatex">\(f(a+h)=h f(a)\)</span> ;</li><li><span class="arithmatex">\(f'(a+h)=f(a)\)</span> ;</li><li><span class="arithmatex">\(f(a+h)\approx f'(a)\)</span>.</li></ol></li>
<li value="5">Une tangente horizontale en <span class="arithmatex">\(a\)</span> signifie :<ol class="auto-choix" type="A"><li><span class="arithmatex">\(f(a)=0\)</span></li><li><span class="arithmatex">\(f'(a)=0\)</span></li><li><span class="arithmatex">\(a=0\)</span></li><li><span class="arithmatex">\(f'(a)=1\)</span></li></ol></li>
<li value="6">Pour <span class="arithmatex">\(f(x)=x^2\)</span>, le nombre dérivé en <span class="arithmatex">\(3\)</span> vaut :<ol class="auto-choix" type="A"><li><span class="arithmatex">\(3\)</span></li><li><span class="arithmatex">\(6\)</span></li><li><span class="arithmatex">\(9\)</span></li><li><span class="arithmatex">\(12\)</span></li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Lire d'abord ce que représente la pente.</li><li>Repérer <span class="arithmatex">\(f(a)\)</span>, <span class="arithmatex">\(f'(a)\)</span> et <span class="arithmatex">\(a\)</span>.</li><li>Éliminer les réponses de mauvaise nature.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Une pente n'est pas une ordonnée.</li><li>Une tangente contient encore <span class="arithmatex">\(x\)</span> et <span class="arithmatex">\(y\)</span>.</li></ul>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse C</strong> : Le nombre <span class="arithmatex">\(f'(a)\)</span> est la pente de la tangente.</li>
    <li value="2"><strong class="auto-resultat">Réponse A</strong> : <span class="arithmatex">\(y=4-3(x-1)=-3x+7\)</span>.</li>
    <li value="3"><strong class="auto-resultat">Réponse B</strong> : C'est le quotient de variation au voisinage de <span class="arithmatex">\(a\)</span>.</li>
    <li value="4"><strong class="auto-resultat">Réponse A</strong> : C'est l'approximation affine locale.</li>
    <li value="5"><strong class="auto-resultat">Réponse B</strong> : Une droite horizontale a une pente nulle.</li>
    <li value="6"><strong class="auto-resultat">Réponse B</strong> : Pour <span class="arithmatex">\(x^2\)</span>, le nombre dérivé en <span class="arithmatex">\(3\)</span> vaut <span class="arithmatex">\(2\times3=6\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> En QCM, comparer la nature des propositions : nombre, fonction, équation ou approximation.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Ne pas confondre valeur de la fonction <span class="arithmatex">\(f(a)\)</span> et nombre dérivé <span class="arithmatex">\(f'(a)\)</span>.</div>

---

*Ces questions reprennent le diaporama d'automatismes N08 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
