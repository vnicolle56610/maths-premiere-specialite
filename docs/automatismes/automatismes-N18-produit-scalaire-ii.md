---
title: "Automatismes Première spécialité – Produit scalaire II : exercices et QCM corrigés"
description: "23 questions d'automatismes de Première spécialité (produit scalaire II), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N18 — Produit scalaire II

23 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N18-produit-scalaire-ii.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N18_PRODUIT_SCALAIRE_II.pdf){ .md-button }
[📖 Revoir la notion](../notions/N18-produit-scalaire-ii.md){ .md-button }
</div>

## Série A — Identités avec le produit scalaire

<p class="auto-meta">⏱ 7 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Développer et utiliser les identités vectorielles.
</div>

<ol class="auto-questions">
<li value="1">Développer <span class="arithmatex">\(\|\vec u+\vec v\|^2\)</span>.</li>
<li value="2">Développer <span class="arithmatex">\(\|\vec u-\vec v\|^2\)</span>.</li>
<li value="3">Si <span class="arithmatex">\(\|\vec u\|=3\)</span>, <span class="arithmatex">\(\|\vec v\|=5\)</span>, <span class="arithmatex">\(\vec u\cdot\vec v=4\)</span>, calculer <span class="arithmatex">\(\|\vec u+\vec v\|^2\)</span>.</li>
<li value="4">Avec les mêmes données, calculer <span class="arithmatex">\(\|\vec u-\vec v\|^2\)</span>.</li>
<li value="5">Si <span class="arithmatex">\(\|\vec u+\vec v\|^2=50\)</span>, <span class="arithmatex">\(\|\vec u\|=4\)</span>, <span class="arithmatex">\(\|\vec v\|=5\)</span>, calculer <span class="arithmatex">\(\vec u\cdot\vec v\)</span>.</li>
<li value="6">Simplifier <span class="arithmatex">\((\vec u+\vec v)\cdot(\vec u-\vec v)\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Une norme au carré est un produit scalaire avec soi-même.</li><li>Développer comme avec <span class="arithmatex">\((a+b)^2\)</span>, mais avec des vecteurs.</li><li><span class="arithmatex">\(\vec u\cdot\vec v=\)</span><wbr><span class="arithmatex">\(\vec v\cdot\vec u\)</span>.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas oublier le terme <span class="arithmatex">\(2\vec u\cdot\vec v\)</span>.</li><li>Le signe change dans <span class="arithmatex">\(\|\vec u-\vec v\|^2\)</span>.</li></ul>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(\|\vec u+\vec v\|^2=\)</span><wbr><span class="arithmatex">\(\boxed{\|\vec u\|^2+2\vec u\cdot\vec v+\|\vec v\|^2}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(\|\vec u-\vec v\|^2=\)</span><wbr><span class="arithmatex">\(\boxed{\|\vec u\|^2-2\vec u\cdot\vec v+\|\vec v\|^2}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(\|\vec u+\vec v\|^2=\)</span><wbr><span class="arithmatex">\(9+2\times4+25=\)</span><wbr><span class="arithmatex">\(\boxed{42}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(\|\vec u-\vec v\|^2=\)</span><wbr><span class="arithmatex">\(9-2\times4+25=\)</span><wbr><span class="arithmatex">\(\boxed{26}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(50=\)</span><wbr><span class="arithmatex">\(16+2\vec u\cdot\vec v+25\)</span>, donc <span class="arithmatex">\(2\vec u\cdot\vec v=9\)</span> et <span class="arithmatex">\(\boxed{\vec u\cdot\vec v=\dfrac92}\)</span>.</li>
    <li value="6"><span class="arithmatex">\((\vec u+\vec v)\cdot(\vec u-\vec v)=\)</span><wbr><span class="arithmatex">\(\boxed{\|\vec u\|^2-\|\vec v\|^2}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Transformer une norme au carré en produit scalaire permet de développer proprement.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Les identités vectorielles ressemblent aux identités remarquables, mais le produit est le produit scalaire.</div>

## Série B — Théorème d'Al-Kashi

<p class="auto-meta">⏱ 8 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Relier longueurs et angles dans un triangle quelconque.
</div>

<ol class="auto-questions">
<li value="1">Dans <span class="arithmatex">\(ABC\)</span>, <span class="arithmatex">\(AB=5\)</span>, <span class="arithmatex">\(AC=7\)</span> et <span class="arithmatex">\(\widehat{BAC}=60^\circ\)</span>. Calculer <span class="arithmatex">\(BC^2\)</span>.</li>
<li value="2">En déduire <span class="arithmatex">\(BC\)</span>.</li>
<li value="3">Dans <span class="arithmatex">\(ABC\)</span>, <span class="arithmatex">\(AB=5\)</span>, <span class="arithmatex">\(AC=6\)</span>, <span class="arithmatex">\(BC=7\)</span>. Calculer <span class="arithmatex">\(\cos(\widehat{BAC})\)</span>.</li>
<li value="4">Dans <span class="arithmatex">\(ABC\)</span>, <span class="arithmatex">\(AB=4\)</span>, <span class="arithmatex">\(AC=3\)</span>, <span class="arithmatex">\(BC=5\)</span>. Que vaut <span class="arithmatex">\(\widehat{BAC}\)</span> ?</li>
<li value="5">Si <span class="arithmatex">\(AB^2+AC^2-BC^2&lt;0\)</span>, l'angle <span class="arithmatex">\(\widehat{BAC}\)</span> est-il aigu ou obtus ?</li>
<li value="6">Écrire la formule d'Al-Kashi pour <span class="arithmatex">\(BC^2\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Côté opposé à l'angle : <span class="arithmatex">\(BC\)</span> est opposé à <span class="arithmatex">\(\widehat{BAC}\)</span>.</li><li><span class="arithmatex">\(\cos60^\circ=\dfrac12\)</span>.</li><li>Pour trouver un angle, isoler le cosinus.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas confondre le côté opposé et les côtés adjacents.</li><li>Al-Kashi généralise Pythagore.</li></ul>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(BC^2=\)</span><wbr><span class="arithmatex">\(5^2+7^2-2\times5\times7\times\dfrac12=\)</span><wbr><span class="arithmatex">\(25+49-35=\)</span><wbr><span class="arithmatex">\(\boxed{39}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(BC=\boxed{\sqrt{39}}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(7^2=\)</span><wbr><span class="arithmatex">\(5^2+6^2-2\times5\times6\cos A\)</span>, donc <span class="arithmatex">\(\cos A=\)</span><wbr><span class="arithmatex">\(\dfrac{25+36-49}{60}=\)</span><wbr><span class="arithmatex">\(\boxed{\dfrac15}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(5^2=4^2+3^2\)</span>, donc le triangle est rectangle en <span class="arithmatex">\(A\)</span>, ainsi <span class="arithmatex">\(\boxed{\widehat{BAC}=90^\circ}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(\cos A=\)</span><wbr><span class="arithmatex">\(\dfrac{AB^2+AC^2-BC^2}{2AB\times AC}&lt;0\)</span>, donc l'angle est <span class="arithmatex">\(\boxed{\text{obtus}}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(\boxed{BC^2=AB^2+AC^2-2AB\times AC\cos(\widehat{BAC})}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Identifier le côté opposé à l'angle avant d'écrire la formule évite presque toutes les erreurs.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Le cosinus peut être négatif : cela indique un angle obtus.</div>

## Série C — Lieux géométriques

<p class="auto-meta">⏱ 8 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Reconnaître un lieu à partir d'une condition de produit scalaire.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(A(0;0)\)</span>, <span class="arithmatex">\(B(4;0)\)</span>, <span class="arithmatex">\(M(x;y)\)</span>. Donner <span class="arithmatex">\(\overrightarrow{MA}\)</span>.</li>
<li value="2">Donner <span class="arithmatex">\(\overrightarrow{MB}\)</span>.</li>
<li value="3">Écrire <span class="arithmatex">\(\overrightarrow{MA}\cdot\overrightarrow{MB}=\)</span><wbr><span class="arithmatex">\(0\)</span> en fonction de <span class="arithmatex">\(x\)</span> et <span class="arithmatex">\(y\)</span>.</li>
<li value="4">Transformer <span class="arithmatex">\(x^2+y^2-4x=0\)</span> sous forme canonique.</li>
<li value="5">Quel est le lieu des points <span class="arithmatex">\(M\)</span> tels que <span class="arithmatex">\(\overrightarrow{MA}\cdot\overrightarrow{MB}=\)</span><wbr><span class="arithmatex">\(0\)</span> ?</li>
<li value="6">Écrire l'équation du lieu <span class="arithmatex">\(\overrightarrow{AM}\cdot\overrightarrow{AB}=\)</span><wbr><span class="arithmatex">\(8\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li><span class="arithmatex">\(\overrightarrow{MA}=A-M\)</span> et <span class="arithmatex">\(\overrightarrow{MB}=B-M\)</span>.</li><li><span class="arithmatex">\(\overrightarrow{MA}\cdot\overrightarrow{MB}=\)</span><wbr><span class="arithmatex">\(0\)</span> traduit un angle droit.</li><li>Compléter le carré pour reconnaître un cercle.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Attention à l'ordre des vecteurs.</li><li>Une équation peut représenter une droite ou un cercle.</li></ul>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(\overrightarrow{MA}\left(\begin{smallmatrix}0-x\\0-y\end{smallmatrix}\right)=\)</span><wbr><span class="arithmatex">\(\boxed{\left(\begin{smallmatrix}-x\\-y\end{smallmatrix}\right)}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(\overrightarrow{MB}\left(\begin{smallmatrix}4-x\\-y\end{smallmatrix}\right)=\)</span><wbr><span class="arithmatex">\(\boxed{\left(\begin{smallmatrix}4-x\\-y\end{smallmatrix}\right)}\)</span>.</li>
    <li value="3"><span class="arithmatex">\((-x)(4-x)+(-y)(-y)=0\)</span>, donc <span class="arithmatex">\(\boxed{x^2+y^2-4x=0}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(x^2-4x+y^2=0\)</span>, donc <span class="arithmatex">\(\boxed{(x-2)^2+y^2=4}\)</span>.</li>
    <li value="5">C'est le <span class="arithmatex">\(\boxed{\text{cercle de diamètre $[AB]$}}\)</span>, de centre <span class="arithmatex">\((2;0)\)</span> et de rayon <span class="arithmatex">\(2\)</span>.</li>
    <li value="6"><span class="arithmatex">\(\overrightarrow{AM}\left(\begin{smallmatrix}x\\y\end{smallmatrix}\right)\)</span>, <span class="arithmatex">\(\overrightarrow{AB}\left(\begin{smallmatrix}4\\0\end{smallmatrix}\right)\)</span>, donc <span class="arithmatex">\(4x=8\)</span>, soit <span class="arithmatex">\(\boxed{x=2}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Un produit scalaire nul donne souvent un angle droit ; le lieu associé peut être un cercle.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> L'équation <span class="arithmatex">\((x-a)^2+(y-b)^2=r^2\)</span> se lit centre <span class="arithmatex">\((a;b)\)</span>, rayon <span class="arithmatex">\(r\)</span>.</div>

## Série D — QCM : Produit scalaire II

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Choisir la bonne réponse. Une seule réponse est correcte.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(\|\vec u-\vec v\|^2=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(\|\vec u\|^2+\|\vec v\|^2\)</span></li><li><span class="arithmatex">\(\|\vec u\|^2-2\vec u\cdot\vec v+\|\vec v\|^2\)</span></li><li><span class="arithmatex">\(\|\vec u\|-\|\vec v\|\)</span></li></ol></li>
<li value="2">Dans Al-Kashi, si l'angle est droit, on retrouve<ol class="auto-choix" type="A"><li>Thalès</li><li>Pythagore</li><li>la médiane</li></ol></li>
<li value="3">Le lieu <span class="arithmatex">\(\overrightarrow{MA}\cdot\overrightarrow{MB}=\)</span><wbr><span class="arithmatex">\(0\)</span> est<ol class="auto-choix" type="A"><li>une droite</li><li>un cercle de diamètre <span class="arithmatex">\([AB]\)</span></li><li>une parabole</li></ol></li>
<li value="4">Si <span class="arithmatex">\(\cos A&lt;0\)</span>, alors <span class="arithmatex">\(A\)</span> est<ol class="auto-choix" type="A"><li>aigu</li><li>droit</li><li>obtus</li></ol></li>
<li value="5"><span class="arithmatex">\((\vec u+\vec v)\cdot(\vec u-\vec v)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(\|\vec u\|^2-\|\vec v\|^2\)</span></li><li><span class="arithmatex">\(2\vec u\cdot\vec v\)</span></li><li><span class="arithmatex">\(0\)</span></li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Revenir aux identités de base.</li><li>Relier les lieux aux angles droits.</li><li>Le signe du cosinus donne la nature de l'angle.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Un carré de norme se développe, une norme non.</li><li>Ne pas confondre cercle de diamètre et cercle de centre <span class="arithmatex">\(A\)</span>.</li></ul>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse B</strong> : C'est l'identité de la différence. Réponse .</li>
    <li value="2"><strong class="auto-resultat">Réponse B</strong> : Avec un angle droit, <span class="arithmatex">\(\cos90^\circ=0\)</span>. Réponse .</li>
    <li value="3"><strong class="auto-resultat">Réponse B</strong> : L'angle <span class="arithmatex">\(\widehat{AMB}\)</span> est droit. Réponse .</li>
    <li value="4"><strong class="auto-resultat">Réponse C</strong> : Un cosinus négatif correspond à un angle obtus. Réponse .</li>
    <li value="5"><strong class="auto-resultat">Réponse A</strong> : Les termes croisés s'annulent. Réponse .</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Les QCM de géométrie se traitent mieux en identifiant la figure mentale associée.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> La réponse juste doit être compatible avec les dimensions : longueur, carré de longueur ou nombre.</div>

---

*Ces questions reprennent le diaporama d'automatismes N18 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
