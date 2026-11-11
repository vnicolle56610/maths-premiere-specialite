---
title: "Automatismes Première spécialité – Géométrie repérée : exercices et QCM corrigés"
description: "23 questions d'automatismes de Première spécialité (géométrie repérée), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N19 — Géométrie repérée

23 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N19-geometrie-reperee.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N19_GEOMETRIE_REPEREE.pdf){ .md-button }
[📖 Revoir la notion](../notions/N19-geometrie-reperee.md){ .md-button }
</div>

## Série A — Distances, milieux et cercles

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Utiliser les formules de base en repère orthonormé.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(A(-1;3)\)</span>, <span class="arithmatex">\(B(5;-1)\)</span>. Calculer les coordonnées du milieu <span class="arithmatex">\(I\)</span> de <span class="arithmatex">\([AB]\)</span>.</li>
<li value="2">Avec les mêmes points, calculer <span class="arithmatex">\(AB^2\)</span>.</li>
<li value="3">En déduire <span class="arithmatex">\(AB\)</span>.</li>
<li value="4">Donner le centre et le rayon du cercle <span class="arithmatex">\((x-2)^2+(y+1)^2=9\)</span>.</li>
<li value="5">Le point <span class="arithmatex">\(P(5;-1)\)</span> appartient-il à ce cercle ?</li>
<li value="6">Écrire l'équation du cercle de centre <span class="arithmatex">\(C(1;-2)\)</span> et de rayon <span class="arithmatex">\(4\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Milieu : moyenne des abscisses et des ordonnées.</li><li>Distance : <span class="arithmatex">\(AB^2=\)</span><wbr><span class="arithmatex">\((x_B-x_A)^2+(y_B-y_A)^2\)</span>.</li><li>Cercle : <span class="arithmatex">\((x-a)^2+(y-b)^2=r^2\)</span>.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Dans <span class="arithmatex">\((y+1)^2\)</span>, le centre a pour ordonnée <span class="arithmatex">\(-1\)</span>.</li><li>Le rayon est la racine du second membre.</li></ul>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(I\left(\dfrac{-1+5}{2};\dfrac{3+(-1)}{2}\right)=\)</span><wbr><span class="arithmatex">\(\boxed{(2;1)}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(AB^2=\)</span><wbr><span class="arithmatex">\((5+1)^2+(-1-3)^2=\)</span><wbr><span class="arithmatex">\(36+16=\)</span><wbr><span class="arithmatex">\(\boxed{52}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(AB=\)</span><wbr><span class="arithmatex">\(\sqrt{52}=\)</span><wbr><span class="arithmatex">\(\boxed{2\sqrt{13}}\)</span>.</li>
    <li value="4">Le centre est <span class="arithmatex">\(\boxed{(2;-1)}\)</span> et le rayon est <span class="arithmatex">\(\boxed{3}\)</span>.</li>
    <li value="5"><span class="arithmatex">\((5-2)^2+(-1+1)^2=9\)</span>, donc <span class="arithmatex">\(P\)</span> <span class="arithmatex">\(\boxed{\text{appartient}}\)</span> au cercle.</li>
    <li value="6"><span class="arithmatex">\(\boxed{(x-1)^2+(y+2)^2=16}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> En repère orthonormé, les distances et les cercles se calculent avec Pythagore.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Ne pas confondre rayon et rayon au carré dans l'équation d'un cercle.</div>

## Série B — Droites en repère

<p class="auto-meta">⏱ 8 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Reconnaître et déterminer des équations de droites.
</div>

<ol class="auto-questions">
<li value="1">Donner un vecteur directeur de la droite <span class="arithmatex">\(d:2x-3y+5=0\)</span>.</li>
<li value="2">Donner un vecteur normal de cette droite.</li>
<li value="3">Le point <span class="arithmatex">\(A(2;3)\)</span> appartient-il à <span class="arithmatex">\(d\)</span> ?</li>
<li value="4">Trouver le coefficient directeur de la droite passant par <span class="arithmatex">\(A(1;2)\)</span> et <span class="arithmatex">\(B(5;10)\)</span>.</li>
<li value="5">Donner une équation réduite de cette droite.</li>
<li value="6">Donner une équation de la droite passant par <span class="arithmatex">\(C(0;1)\)</span> et perpendiculaire à <span class="arithmatex">\(y=2x-3\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Pour <span class="arithmatex">\(ax+by+c=0\)</span>, un normal est <span class="arithmatex">\((a;b)\)</span>.</li><li>Un directeur possible est <span class="arithmatex">\((b;-a)\)</span>.</li><li>Deux droites perpendiculaires ont des coefficients directeurs de produit <span class="arithmatex">\(-1\)</span>.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Tester un point : remplacer <span class="arithmatex">\(x\)</span> et <span class="arithmatex">\(y\)</span>.</li><li>Ne pas confondre vecteur directeur et vecteur normal.</li></ul>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1">Un vecteur directeur est <span class="arithmatex">\(\boxed{(3;2)}\)</span>.</li>
    <li value="2">Un vecteur normal est <span class="arithmatex">\(\boxed{(2;-3)}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(2\times2-3\times3+5=0\)</span>, donc <span class="arithmatex">\(A\)</span> <span class="arithmatex">\(\boxed{\text{appartient}}\)</span> à <span class="arithmatex">\(d\)</span>.</li>
    <li value="4"><span class="arithmatex">\(m=\)</span><wbr><span class="arithmatex">\(\dfrac{10-2}{5-1}=\)</span><wbr><span class="arithmatex">\(\boxed{2}\)</span>.</li>
    <li value="5">La droite a pour équation <span class="arithmatex">\(y=2x+p\)</span>. Avec <span class="arithmatex">\(A\)</span>, <span class="arithmatex">\(2=2+p\)</span>, donc <span class="arithmatex">\(\boxed{y=2x}\)</span>.</li>
    <li value="6">Le coefficient directeur est <span class="arithmatex">\(-\dfrac12\)</span>. Avec <span class="arithmatex">\(C(0;1)\)</span>, une équation est <span class="arithmatex">\(\boxed{y=-\dfrac12x+1}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Choisir la forme d'équation la plus rapide : cartésienne pour normal, réduite pour pente.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Pour une perpendiculaire, le coefficient directeur n'est pas l'opposé : c'est l'opposé de l'inverse.</div>

## Série C — Configurations analytiques

<p class="auto-meta">⏱ 8 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Choisir entre calcul de droite, cercle et projection.
</div>

<ol class="auto-questions">
<li value="1">Résoudre l'intersection de <span class="arithmatex">\(d:y=x+1\)</span> et <span class="arithmatex">\(\Delta:y=-x+5\)</span>.</li>
<li value="2">Le point trouvé appartient-il au cercle <span class="arithmatex">\((x-3)^2+(y-3)^2=2\)</span> ?</li>
<li value="3"><span class="arithmatex">\(A(0;0)\)</span>, <span class="arithmatex">\(B(4;0)\)</span>, <span class="arithmatex">\(P(1;3)\)</span>. Quel est le projeté orthogonal de <span class="arithmatex">\(P\)</span> sur <span class="arithmatex">\((AB)\)</span> ?</li>
<li value="4">Calculer la distance de <span class="arithmatex">\(P\)</span> à la droite <span class="arithmatex">\((AB)\)</span>.</li>
<li value="5">La droite <span class="arithmatex">\(x=2\)</span> coupe le cercle <span class="arithmatex">\(x^2+y^2=5\)</span>. Trouver les points d'intersection.</li>
<li value="6">Donner une équation de la droite passant par <span class="arithmatex">\(M(2;-1)\)</span> et parallèle à <span class="arithmatex">\(3x-y+4=0\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Intersection : résoudre un système.</li><li>Projection : utiliser une direction perpendiculaire.</li><li>Droites parallèles : même vecteur normal dans une équation cartésienne.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Une droite verticale n'a pas d'équation <span class="arithmatex">\(y=mx+p\)</span>.</li><li>Vérifier dans l'équation du cercle.</li></ul>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(x+1=-x+5\)</span>, donc <span class="arithmatex">\(2x=4\)</span>, <span class="arithmatex">\(x=2\)</span>, puis <span class="arithmatex">\(y=3\)</span>. Intersection : <span class="arithmatex">\(\boxed{(2;3)}\)</span>.</li>
    <li value="2"><span class="arithmatex">\((2-3)^2+(3-3)^2=1\ne2\)</span>, donc le point <span class="arithmatex">\(\boxed{\text{n'appartient pas}}\)</span> au cercle.</li>
    <li value="3">La droite <span class="arithmatex">\((AB)\)</span> est l'axe des abscisses : le projeté est <span class="arithmatex">\(\boxed{(1;0)}\)</span>.</li>
    <li value="4">La distance à l'axe des abscisses vaut <span class="arithmatex">\(\boxed{3}\)</span>.</li>
    <li value="5">Si <span class="arithmatex">\(x=2\)</span>, alors <span class="arithmatex">\(4+y^2=5\)</span>, donc <span class="arithmatex">\(y=\pm1\)</span>. Points : <span class="arithmatex">\(\boxed{\text{$(2;1)$ et $(2;-1)$}}\)</span>.</li>
    <li value="6">Une droite parallèle a la forme <span class="arithmatex">\(3x-y+c=0\)</span>. Avec <span class="arithmatex">\(M\)</span> : <span class="arithmatex">\(6+1+c=0\)</span>, donc <span class="arithmatex">\(\boxed{3x-y-7=0}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Dans une configuration, identifier d'abord l'objet : droite, cercle, intersection ou projection.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Le résultat doit satisfaire toutes les équations utilisées.</div>

## Série D — QCM : Géométrie repérée

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Choisir la bonne réponse. Une seule réponse est correcte.
</div>

<ol class="auto-questions">
<li value="1">Le centre du cercle <span class="arithmatex">\((x+2)^2+(y-5)^2=16\)</span> est<ol class="auto-choix" type="A"><li><span class="arithmatex">\((2;-5)\)</span></li><li><span class="arithmatex">\((-2;5)\)</span></li><li><span class="arithmatex">\((-2;-5)\)</span></li></ol></li>
<li value="2">Un vecteur normal à <span class="arithmatex">\(4x+y-1=0\)</span> est<ol class="auto-choix" type="A"><li><span class="arithmatex">\((4;1)\)</span></li><li><span class="arithmatex">\((1;-4)\)</span></li><li><span class="arithmatex">\((4;-1)\)</span></li></ol></li>
<li value="3">La droite <span class="arithmatex">\(x=3\)</span> est<ol class="auto-choix" type="A"><li>horizontale</li><li>verticale</li><li>oblique</li></ol></li>
<li value="4">Le milieu de <span class="arithmatex">\(A(2;-1)\)</span> et <span class="arithmatex">\(B(6;5)\)</span> est<ol class="auto-choix" type="A"><li><span class="arithmatex">\((4;2)\)</span></li><li><span class="arithmatex">\((8;4)\)</span></li><li><span class="arithmatex">\((2;3)\)</span></li></ol></li>
<li value="5">Si deux droites de coefficients directeurs <span class="arithmatex">\(2\)</span> et <span class="arithmatex">\(-\dfrac12\)</span> se coupent, elles sont<ol class="auto-choix" type="A"><li>parallèles</li><li>perpendiculaires</li><li>confondues</li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Lire les signes dans l'équation du cercle.</li><li>Pour <span class="arithmatex">\(ax+by+c=0\)</span>, le normal est <span class="arithmatex">\((a;b)\)</span>.</li><li>Produit des pentes <span class="arithmatex">\(-1\)</span> : perpendicularité.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li><span class="arithmatex">\(x=3\)</span> impose l'abscisse, pas l'ordonnée.</li><li>Le milieu utilise deux moyennes.</li></ul>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\((x+2)^2=(x-(-2))^2\)</span> et <span class="arithmatex">\((y-5)^2\)</span>. Réponse .</li>
    <li value="2"><strong class="auto-resultat">Réponse A</strong> : Pour <span class="arithmatex">\(ax+by+c=0\)</span>, un normal est <span class="arithmatex">\((a;b)\)</span>. Réponse .</li>
    <li value="3"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(x=3\)</span> est une droite verticale. Réponse .</li>
    <li value="4"><strong class="auto-resultat">Réponse A</strong> : <span class="arithmatex">\(\left(\dfrac{2+6}{2};\dfrac{-1+5}{2}\right)=\)</span><wbr><span class="arithmatex">\((4;2)\)</span>. Réponse .</li>
    <li value="5"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(2\times\left(-\dfrac12\right)=\)</span><wbr><span class="arithmatex">\(-1\)</span>. Réponse .</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Les questions courtes de repérage exigent surtout une lecture très précise des signes.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Ne pas transformer une droite verticale en équation réduite.</div>

---

*Ces questions reprennent le diaporama d'automatismes N19 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
