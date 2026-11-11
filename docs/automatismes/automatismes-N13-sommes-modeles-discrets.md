---
title: "Automatismes Première spécialité – Sommes et modèles discrets : exercices et QCM corrigés"
description: "24 questions d'automatismes de Première spécialité (sommes et modèles discrets), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N13 — Sommes et modèles discrets

24 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N13-sommes-modeles-discrets.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N13_SOMMES_MODELES_DISCRETS.pdf){ .md-button }
[📖 Revoir la notion](../notions/N13-sommes-modeles-discrets.md){ .md-button }
</div>

## Série A — Réactivation : suites et calculs

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Calculer rapidement des termes et de petites sommes.
</div>

<ol class="auto-questions">
<li value="1">Calculer <span class="arithmatex">\(1+2+3+4+5\)</span>.</li>
<li value="2">Calculer <span class="arithmatex">\(3+6+9+12\)</span>.</li>
<li value="3"><span class="arithmatex">\(u_n=2n+1\)</span>. Calculer <span class="arithmatex">\(u_4\)</span>.</li>
<li value="4">Suite arithmétique <span class="arithmatex">\(u_0=4\)</span>, <span class="arithmatex">\(r=3\)</span>. Calculer <span class="arithmatex">\(u_5\)</span>.</li>
<li value="5">Suite géométrique <span class="arithmatex">\(v_0=2\)</span>, <span class="arithmatex">\(q=3\)</span>. Calculer <span class="arithmatex">\(v_3\)</span>.</li>
<li value="6">Écrire <span class="arithmatex">\(2+4+8+16\)</span> avec un symbole <span class="arithmatex">\(\sum\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Une somme additionne plusieurs termes.</li><li>Chercher le premier et le dernier terme.</li><li>Compter le nombre de termes.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas confondre terme <span class="arithmatex">\(u_n\)</span> et somme de termes.</li><li>Le symbole <span class="arithmatex">\(\sum\)</span> indique les indices parcourus.</li></ul>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(1+2+3+4+5=\boxed{15}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(3+6+9+12=\boxed{30}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(u_4=2\times4+1=\boxed{9}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(u_5=\)</span><wbr><span class="arithmatex">\(4+5\times3=\)</span><wbr><span class="arithmatex">\(\boxed{19}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(v_3=\)</span><wbr><span class="arithmatex">\(2\times3^3=\)</span><wbr><span class="arithmatex">\(2\times27=\)</span><wbr><span class="arithmatex">\(\boxed{54}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(2+4+8+16=\)</span><wbr><span class="arithmatex">\(\boxed{\sum_{k=1}^{4}2^k}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Une somme de termes consécutifs se prépare en identifiant l'indice de départ et l'indice d'arrivée.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Un symbole <span class="arithmatex">\(\sum\)</span> doit toujours avoir un indice de départ et un indice d'arrivée.</div>

## Série B — Sommes arithmétiques

<p class="auto-meta">⏱ 8 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Utiliser la structure d'une somme de termes consécutifs.
</div>

<ol class="auto-questions">
<li value="1">Calculer <span class="arithmatex">\(1+2+\cdots+20\)</span>.</li>
<li value="2">Calculer <span class="arithmatex">\(5+6+\cdots+15\)</span>.</li>
<li value="3">Suite arithmétique <span class="arithmatex">\(u_0=3\)</span>, <span class="arithmatex">\(r=2\)</span>. Calculer <span class="arithmatex">\(u_0+u_1+\cdots+u_5\)</span>.</li>
<li value="4">Somme <span class="arithmatex">\(12+15+\cdots+30\)</span>. Donner le nombre de termes.</li>
<li value="5">Calculer <span class="arithmatex">\(12+15+\cdots+30\)</span>.</li>
<li value="6">Exprimer <span class="arithmatex">\(7+10+13+\cdots+34\)</span> comme somme arithmétique.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Somme arithmétique : nombre de termes <span class="arithmatex">\(\times\)</span> moyenne des extrêmes.</li><li>Vérifier que les termes sont consécutifs dans la suite.</li><li>Compter avec les rangs.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Le nombre de termes n'est pas forcément le dernier nombre.</li><li>Pour <span class="arithmatex">\(5\)</span> à <span class="arithmatex">\(15\)</span>, il y a <span class="arithmatex">\(15-5+1\)</span> termes.</li></ul>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(1+2+\cdots+20=\)</span><wbr><span class="arithmatex">\(\dfrac{20\times21}{2}=\)</span><wbr><span class="arithmatex">\(\boxed{210}\)</span>.</li>
    <li value="2">Il y a <span class="arithmatex">\(11\)</span> termes. Somme <span class="arithmatex">\(=\)</span><wbr><span class="arithmatex">\(11\times\dfrac{5+15}{2}=\)</span><wbr><span class="arithmatex">\(\boxed{110}\)</span>.</li>
    <li value="3">Les termes sont <span class="arithmatex">\(3;5;7;9;11;13\)</span>. Somme <span class="arithmatex">\(=\)</span><wbr><span class="arithmatex">\(6\times\dfrac{3+13}{2}=\)</span><wbr><span class="arithmatex">\(\boxed{48}\)</span>.</li>
    <li value="4">De <span class="arithmatex">\(12\)</span> à <span class="arithmatex">\(30\)</span> avec pas <span class="arithmatex">\(3\)</span> : <span class="arithmatex">\(12;15;18;21;24;27;30\)</span>. Donc <span class="arithmatex">\(\boxed{7}\)</span> termes.</li>
    <li value="5">Somme <span class="arithmatex">\(=\)</span><wbr><span class="arithmatex">\(7\times\dfrac{12+30}{2}=\)</span><wbr><span class="arithmatex">\(7\times21=\)</span><wbr><span class="arithmatex">\(\boxed{147}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(7+10+13+\cdots+34=\)</span><wbr><span class="arithmatex">\(\boxed{\sum_{k=0}^{9}(7+3k)}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Pour une somme arithmétique : <span class="arithmatex">\(\displaystyle S=\)</span><wbr><span class="arithmatex">\(\dfrac{\text{nombre de termes}\times(\text{premier}+\text{dernier})}{2}\)</span>.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Toujours vérifier que le dernier terme annoncé appartient bien à la suite.</div>

## Série C — Sommes géométriques et seuils

<p class="auto-meta">⏱ 8 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Calculer une somme géométrique ou repérer un seuil simple.
</div>

<ol class="auto-questions">
<li value="1">Calculer <span class="arithmatex">\(1+2+4+8+16\)</span>.</li>
<li value="2">Calculer <span class="arithmatex">\(3+6+12+24\)</span>.</li>
<li value="3">Suite géométrique <span class="arithmatex">\(u_0=5\)</span>, <span class="arithmatex">\(q=2\)</span>. Calculer <span class="arithmatex">\(u_0+u_1+u_2+u_3\)</span>.</li>
<li value="4">Une somme vaut <span class="arithmatex">\(S_n=1+2+\cdots+2^n\)</span>. Calculer <span class="arithmatex">\(S_4\)</span>.</li>
<li value="5"><span class="arithmatex">\(v_0=100\)</span>, <span class="arithmatex">\(v_{n+1}=1{,}1v_n\)</span>. À partir de quel rang dépasse-t-on <span class="arithmatex">\(120\)</span> ?</li>
<li value="6">Épargne : <span class="arithmatex">\(50\)</span> euros chaque mois pendant <span class="arithmatex">\(6\)</span> mois. Somme versée ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Ajouter les termes exacts.</li><li>Pour un seuil, avancer rang par rang.</li><li>Interpréter le résultat dans le contexte.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>La somme géométrique n'est pas le dernier terme.</li><li>Pour un seuil, la question demande souvent le premier rang.</li></ul>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(1+2+4+8+16=\boxed{31}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(3+6+12+24=\boxed{45}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(u_0=5\)</span>, <span class="arithmatex">\(u_1=10\)</span>, <span class="arithmatex">\(u_2=20\)</span>, <span class="arithmatex">\(u_3=40\)</span>. Somme <span class="arithmatex">\(=\boxed{75}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(S_4=\)</span><wbr><span class="arithmatex">\(1+2+4+8+16=\)</span><wbr><span class="arithmatex">\(\boxed{31}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(v_1=110\)</span>, <span class="arithmatex">\(v_2=121\)</span>. Le seuil <span class="arithmatex">\(120\)</span> est dépassé au rang <span class="arithmatex">\(\boxed{2}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(6\times50=\boxed{300}\)</span> euros.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Un modèle discret s'interprète terme par terme : valeur à un rang, cumul, puis seuil.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Le premier rang qui dépasse un seuil doit être vérifié par le rang précédent.</div>

## Série D — Type épreuve anticipée : QCM

<p class="auto-meta">⏱ 5 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Choisir une seule réponse. Aucune justification n'est demandée.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(1+2+\cdots+10=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(10\)</span></li><li><span class="arithmatex">\(45\)</span></li><li><span class="arithmatex">\(55\)</span></li><li><span class="arithmatex">\(100\)</span></li></ol></li>
<li value="2">Somme <span class="arithmatex">\(4+7+\cdots+22\)</span>. Nombre de termes :<ol class="auto-choix" type="A"><li><span class="arithmatex">\(6\)</span></li><li><span class="arithmatex">\(7\)</span></li><li><span class="arithmatex">\(18\)</span></li><li><span class="arithmatex">\(22\)</span></li></ol></li>
<li value="3"><span class="arithmatex">\(2+4+8+16=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(16\)</span></li><li><span class="arithmatex">\(24\)</span></li><li><span class="arithmatex">\(30\)</span></li><li><span class="arithmatex">\(32\)</span></li></ol></li>
<li value="4"><span class="arithmatex">\(\sum_{k=0}^{3}(2k+1)=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(4\)</span></li><li><span class="arithmatex">\(8\)</span></li><li><span class="arithmatex">\(12\)</span></li><li><span class="arithmatex">\(16\)</span></li></ol></li>
<li value="5"><span class="arithmatex">\(u_0=10\)</span>, <span class="arithmatex">\(u_{n+1}=u_n+5\)</span>. <span class="arithmatex">\(u_0+\cdots+u_3=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(25\)</span></li><li><span class="arithmatex">\(40\)</span></li><li><span class="arithmatex">\(70\)</span></li><li><span class="arithmatex">\(100\)</span></li></ol></li>
<li value="6"><span class="arithmatex">\(100;120;144;\ldots\)</span>. Modèle :<ol class="auto-choix" type="A"><li><span class="arithmatex">\(arithmétique\)</span></li><li><span class="arithmatex">\(géométrique\)</span></li><li><span class="arithmatex">\(constant\)</span></li><li><span class="arithmatex">\(impossible\)</span></li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Compter les termes avant de sommer.</li><li>Développer le symbole <span class="arithmatex">\(\sum\)</span> si besoin.</li><li>Repérer addition ou multiplication répétée.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Le dernier terme n'est pas la somme.</li><li>Dans un QCM, une réponse plausible peut oublier un terme.</li></ul>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse C</strong> : <span class="arithmatex">\(\dfrac{10\times11}{2}=55\)</span>.</li>
    <li value="2"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(4;7;10;13;16;19;22\)</span> : <span class="arithmatex">\(7\)</span> termes.</li>
    <li value="3"><strong class="auto-resultat">Réponse C</strong> : <span class="arithmatex">\(2+4+8+16=30\)</span>.</li>
    <li value="4"><strong class="auto-resultat">Réponse D</strong> : <span class="arithmatex">\(1+3+5+7=16\)</span>.</li>
    <li value="5"><strong class="auto-resultat">Réponse C</strong> : <span class="arithmatex">\(10+15+20+25=70\)</span>.</li>
    <li value="6"><strong class="auto-resultat">Réponse B</strong> : On multiplie par <span class="arithmatex">\(1{,}2\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Développer mentalement les premiers termes permet d'éviter la plupart des erreurs de somme.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> La somme, le terme et le seuil sont trois objets différents.</div>

---

*Ces questions reprennent le diaporama d'automatismes N13 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
