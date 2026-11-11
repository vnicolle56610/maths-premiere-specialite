---
title: "Automatismes Première spécialité – Produit scalaire I : exercices et QCM corrigés"
description: "23 questions d'automatismes de Première spécialité (produit scalaire I), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N17 — Produit scalaire I

23 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N17-produit-scalaire-i.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N17_PRODUIT_SCALAIRE_I.pdf){ .md-button }
[📖 Revoir la notion](../notions/N17-produit-scalaire-i.md){ .md-button }
</div>

## Série A — Produit scalaire en coordonnées

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Calculer rapidement des produits scalaires et reconnaître l'orthogonalité.
</div>

<ol class="auto-questions">
<li value="1">Soit <span class="arithmatex">\(\vec u\left(\begin{smallmatrix}3\\4\end{smallmatrix}\right)\)</span> et <span class="arithmatex">\(\vec v\left(\begin{smallmatrix}2\\-1\end{smallmatrix}\right)\)</span>. Calculer <span class="arithmatex">\(\vec u\cdot\vec v\)</span>.</li>
<li value="2">Soit <span class="arithmatex">\(\vec a\left(\begin{smallmatrix}-5\\2\end{smallmatrix}\right)\)</span> et <span class="arithmatex">\(\vec b\left(\begin{smallmatrix}1\\3\end{smallmatrix}\right)\)</span>. Calculer <span class="arithmatex">\(\vec a\cdot\vec b\)</span>.</li>
<li value="3">Soit <span class="arithmatex">\(\vec r\left(\begin{smallmatrix}6\\-2\end{smallmatrix}\right)\)</span> et <span class="arithmatex">\(\vec s\left(\begin{smallmatrix}1\\3\end{smallmatrix}\right)\)</span>. Les vecteurs sont-ils orthogonaux ?</li>
<li value="4">Soit <span class="arithmatex">\(\vec m\left(\begin{smallmatrix}4\\3\end{smallmatrix}\right)\)</span>. Calculer <span class="arithmatex">\(\vec m\cdot\vec m\)</span>.</li>
<li value="5">En déduire <span class="arithmatex">\(\|\vec m\|\)</span>.</li>
<li value="6">Trouver <span class="arithmatex">\(x\)</span> pour que <span class="arithmatex">\(\vec p\left(\begin{smallmatrix}2\\x\end{smallmatrix}\right)\)</span> et <span class="arithmatex">\(\vec q\left(\begin{smallmatrix}3\\-4\end{smallmatrix}\right)\)</span> soient orthogonaux.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Si <span class="arithmatex">\(\vec u\left(\begin{smallmatrix}x\\y\end{smallmatrix}\right)\)</span> et <span class="arithmatex">\(\vec v\left(\begin{smallmatrix}x'\\y'\end{smallmatrix}\right)\)</span>, alors <span class="arithmatex">\(\vec u\cdot\vec v=\)</span><wbr><span class="arithmatex">\(xx'+yy'\)</span>.</li><li><span class="arithmatex">\(\vec u\cdot\vec u=\)</span><wbr><span class="arithmatex">\(\|\vec u\|^2\)</span>.</li><li>Orthogonalité : produit scalaire nul.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas multiplier seulement les abscisses.</li><li><span class="arithmatex">\(\|\vec u\|^2\)</span> n'est pas toujours <span class="arithmatex">\(\|\vec u\|\)</span>.</li></ul>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(\vec u\cdot\vec v=\)</span><wbr><span class="arithmatex">\(3\times2+4\times(-1)=\)</span><wbr><span class="arithmatex">\(\boxed{2}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(\vec a\cdot\vec b=\)</span><wbr><span class="arithmatex">\((-5)\times1+2\times3=\)</span><wbr><span class="arithmatex">\(\boxed{1}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(\vec r\cdot\vec s=\)</span><wbr><span class="arithmatex">\(6\times1+(-2)\times3=\)</span><wbr><span class="arithmatex">\(0\)</span>, donc ils sont <span class="arithmatex">\(\boxed{\text{orthogonaux}}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(\vec m\cdot\vec m=\)</span><wbr><span class="arithmatex">\(4^2+3^2=\)</span><wbr><span class="arithmatex">\(\boxed{25}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(\|\vec m\|=\)</span><wbr><span class="arithmatex">\(\sqrt{25}=\)</span><wbr><span class="arithmatex">\(\boxed{5}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(2\times3+x\times(-4)=0\)</span>, donc <span class="arithmatex">\(6-4x=0\)</span>, d'où <span class="arithmatex">\(\boxed{x=\dfrac32}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Calculer d'abord le produit scalaire, puis interpréter : nul, positif, négatif ou carré d'une norme.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Dans une condition d'orthogonalité, l'inconnue est dans une équation produit scalaire <span class="arithmatex">\(=0\)</span>.</div>

## Série B — Normes, angles et projection

<p class="auto-meta">⏱ 7 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Utiliser la formule <span class="arithmatex">\(\vec u\cdot\vec v=\)</span><wbr><span class="arithmatex">\(\|\vec u\|\,\|\vec v\|\cos\theta\)</span>.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(\|\vec u\|=3\)</span>, <span class="arithmatex">\(\|\vec v\|=4\)</span>, <span class="arithmatex">\(\theta=60^\circ\)</span>. Calculer <span class="arithmatex">\(\vec u\cdot\vec v\)</span>.</li>
<li value="2"><span class="arithmatex">\(\|\vec a\|=5\)</span>, <span class="arithmatex">\(\|\vec b\|=2\)</span>, <span class="arithmatex">\(\theta=90^\circ\)</span>. Calculer <span class="arithmatex">\(\vec a\cdot\vec b\)</span>.</li>
<li value="3"><span class="arithmatex">\(\|\vec r\|=2\)</span>, <span class="arithmatex">\(\|\vec s\|=3\)</span>, <span class="arithmatex">\(\theta=180^\circ\)</span>. Calculer <span class="arithmatex">\(\vec r\cdot\vec s\)</span>.</li>
<li value="4">Si <span class="arithmatex">\(\vec u\cdot\vec v=6\)</span>, <span class="arithmatex">\(\|\vec u\|=3\)</span>, <span class="arithmatex">\(\|\vec v\|=4\)</span>, calculer <span class="arithmatex">\(\cos\theta\)</span>.</li>
<li value="5">Si <span class="arithmatex">\(\vec u\cdot\vec v&lt;0\)</span>, l'angle est-il aigu ou obtus ?</li>
<li value="6">Si <span class="arithmatex">\(AB=8\)</span> et la projection de <span class="arithmatex">\(\overrightarrow{AC}\)</span> sur <span class="arithmatex">\((AB)\)</span> vaut <span class="arithmatex">\(3\)</span>, calculer <span class="arithmatex">\(\overrightarrow{AB}\cdot\overrightarrow{AC}\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li><span class="arithmatex">\(\cos 60^\circ=\dfrac12\)</span>, <span class="arithmatex">\(\cos90^\circ=0\)</span>, <span class="arithmatex">\(\cos180^\circ=-1\)</span>.</li><li>Le signe du produit scalaire renseigne sur l'angle.</li><li>Projection : longueur orientée sur la direction donnée.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Une projection peut être négative.</li><li>Orthogonal ne signifie pas parallèle.</li></ul>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(\vec u\cdot\vec v=\)</span><wbr><span class="arithmatex">\(3\times4\times\dfrac12=\)</span><wbr><span class="arithmatex">\(\boxed{6}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(\vec a\cdot\vec b=\)</span><wbr><span class="arithmatex">\(5\times2\times0=\)</span><wbr><span class="arithmatex">\(\boxed{0}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(\vec r\cdot\vec s=\)</span><wbr><span class="arithmatex">\(2\times3\times(-1)=\)</span><wbr><span class="arithmatex">\(\boxed{-6}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(\cos\theta=\)</span><wbr><span class="arithmatex">\(\dfrac{6}{3\times4}=\)</span><wbr><span class="arithmatex">\(\boxed{\dfrac12}\)</span>.</li>
    <li value="5">Si <span class="arithmatex">\(\vec u\cdot\vec v&lt;0\)</span>, alors <span class="arithmatex">\(\cos\theta&lt;0\)</span> : l'angle est <span class="arithmatex">\(\boxed{\text{obtus}}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(\overrightarrow{AB}\cdot\overrightarrow{AC}=\)</span><wbr><span class="arithmatex">\(AB\times 3=\)</span><wbr><span class="arithmatex">\(\boxed{24}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> La formule avec le cosinus permet de passer d'une information géométrique à un calcul.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Le signe du cosinus suit le signe du produit scalaire si les deux normes sont non nulles.</div>

## Série C — Points et orthogonalité

<p class="auto-meta">⏱ 8 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Passer des points aux vecteurs, puis calculer le produit scalaire.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(A(1;2)\)</span>, <span class="arithmatex">\(B(4;3)\)</span>. Donner les coordonnées de <span class="arithmatex">\(\overrightarrow{AB}\)</span>.</li>
<li value="2"><span class="arithmatex">\(A(1;2)\)</span>, <span class="arithmatex">\(C(2;-1)\)</span>. Donner les coordonnées de <span class="arithmatex">\(\overrightarrow{AC}\)</span>.</li>
<li value="3">Calculer <span class="arithmatex">\(\overrightarrow{AB}\cdot\overrightarrow{AC}\)</span>.</li>
<li value="4">Que peut-on dire des droites <span class="arithmatex">\((AB)\)</span> et <span class="arithmatex">\((AC)\)</span> ?</li>
<li value="5"><span class="arithmatex">\(D(5;1)\)</span>, <span class="arithmatex">\(E(2;7)\)</span>. Calculer <span class="arithmatex">\(\overrightarrow{DE}\cdot\overrightarrow{DE}\)</span>.</li>
<li value="6">En déduire la longueur <span class="arithmatex">\(DE\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li><span class="arithmatex">\(\overrightarrow{AB}\left(\begin{smallmatrix}x_B-x_A\\y_B-y_A\end{smallmatrix}\right)\)</span>.</li><li>Un angle droit se prouve par un produit scalaire nul.</li><li>Une longueur se déduit du carré de la norme.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Respecter l'ordre dans <span class="arithmatex">\(\overrightarrow{AB}\)</span>.</li><li>Une longueur est positive.</li></ul>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(\overrightarrow{AB}\left(\begin{smallmatrix}4-1\\3-2\end{smallmatrix}\right)=\)</span><wbr><span class="arithmatex">\(\boxed{\left(\begin{smallmatrix}3\\1\end{smallmatrix}\right)}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(\overrightarrow{AC}\left(\begin{smallmatrix}2-1\\-1-2\end{smallmatrix}\right)=\)</span><wbr><span class="arithmatex">\(\boxed{\left(\begin{smallmatrix}1\\-3\end{smallmatrix}\right)}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(\overrightarrow{AB}\cdot\overrightarrow{AC}=\)</span><wbr><span class="arithmatex">\(3\times1+1\times(-3)=\)</span><wbr><span class="arithmatex">\(\boxed{0}\)</span>.</li>
    <li value="4">Le produit scalaire est nul, donc <span class="arithmatex">\((AB)\)</span> et <span class="arithmatex">\((AC)\)</span> sont <span class="arithmatex">\(\boxed{\text{perpendiculaires}}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(\overrightarrow{DE}\left(\begin{smallmatrix}-3\\6\end{smallmatrix}\right)\)</span>, donc <span class="arithmatex">\(\overrightarrow{DE}\cdot\overrightarrow{DE}=\)</span><wbr><span class="arithmatex">\((-3)^2+6^2=\)</span><wbr><span class="arithmatex">\(\boxed{45}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(DE=\)</span><wbr><span class="arithmatex">\(\sqrt{45}=\)</span><wbr><span class="arithmatex">\(\boxed{3\sqrt5}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> En repère, une preuve géométrique peut devenir un calcul de coordonnées puis de produit scalaire.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Ne pas conclure à une perpendicularité avec deux vecteurs seulement proportionnels.</div>

## Série D — QCM : Produit scalaire I

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Choisir la bonne réponse. Une seule réponse est correcte.
</div>

<ol class="auto-questions">
<li value="1">Si <span class="arithmatex">\(\vec u\left(\begin{smallmatrix}1\\-2\end{smallmatrix}\right)\)</span> et <span class="arithmatex">\(\vec v\left(\begin{smallmatrix}4\\2\end{smallmatrix}\right)\)</span>, alors <span class="arithmatex">\(\vec u\cdot\vec v=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(8\)</span></li><li><span class="arithmatex">\(0\)</span></li><li><span class="arithmatex">\(-8\)</span></li></ol></li>
<li value="2">Si <span class="arithmatex">\(\vec u\cdot\vec v=0\)</span>, alors les vecteurs sont<ol class="auto-choix" type="A"><li>égaux</li><li>orthogonaux</li><li>colinéaires</li></ol></li>
<li value="3"><span class="arithmatex">\(\vec u\cdot\vec u\)</span> est égal à<ol class="auto-choix" type="A"><li><span class="arithmatex">\(\|\vec u\|\)</span></li><li><span class="arithmatex">\(2\|\vec u\|\)</span></li><li><span class="arithmatex">\(\|\vec u\|^2\)</span></li></ol></li>
<li value="4">Un produit scalaire négatif correspond à un angle<ol class="auto-choix" type="A"><li>aigu</li><li>droit</li><li>obtus</li></ol></li>
<li value="5">Si <span class="arithmatex">\(\|\vec u\|=6\)</span>, <span class="arithmatex">\(\|\vec v\|=2\)</span>, <span class="arithmatex">\(\theta=60^\circ\)</span>, alors <span class="arithmatex">\(\vec u\cdot\vec v=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(6\)</span></li><li><span class="arithmatex">\(12\)</span></li><li><span class="arithmatex">\(3\)</span></li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Calculer avant de choisir.</li><li>Repérer les mots-clés : nul, négatif, carré de la norme.</li><li>Vérifier les signes.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Orthogonal et colinéaire sont deux idées différentes.</li><li><span class="arithmatex">\(\vec u\cdot\vec u\)</span> n'est pas un produit de coordonnées quelconque.</li></ul>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(1\times4+(-2)\times2=0\)</span>. Réponse .</li>
    <li value="2"><strong class="auto-resultat">Réponse B</strong> : Un produit scalaire nul caractérise l'orthogonalité. Réponse .</li>
    <li value="3"><strong class="auto-resultat">Réponse C</strong> : <span class="arithmatex">\(\vec u\cdot\vec u=\)</span><wbr><span class="arithmatex">\(\|\vec u\|^2\)</span>. Réponse .</li>
    <li value="4"><strong class="auto-resultat">Réponse C</strong> : Un produit scalaire négatif donne un cosinus négatif. Réponse .</li>
    <li value="5"><strong class="auto-resultat">Réponse A</strong> : <span class="arithmatex">\(6\times2\times\dfrac12=6\)</span>. Réponse .</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Dans un QCM, une formule simple suffit souvent à éliminer deux réponses.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Ne pas répondre au seul souvenir : faire le calcul éclair.</div>

---

*Ces questions reprennent le diaporama d'automatismes N17 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
