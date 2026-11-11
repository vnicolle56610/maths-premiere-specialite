---
title: "Automatismes Première spécialité – Suites : définition et premiers raisonnements : exercices et QCM corrigés"
description: "24 questions d'automatismes de Première spécialité (suites : définition et premiers raisonnements), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N11 — Suites : définition et premiers raisonnements

24 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N11-suites-definition.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N11_SUITES_DEFINITION.pdf){ .md-button }
[📖 Revoir la notion](../notions/N11-suites-definition.md){ .md-button }
</div>

## Série A — Réactivation : expressions et rangs

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Calculer les premiers termes et identifier le rang demandé.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(u_n=2n+3\)</span>. Calculer <span class="arithmatex">\(u_0\)</span>.</li>
<li value="2">Pour la même suite, calculer <span class="arithmatex">\(u_5\)</span>.</li>
<li value="3"><span class="arithmatex">\(v_n=n^2-1\)</span>. Calculer <span class="arithmatex">\(v_3\)</span>.</li>
<li value="4"><span class="arithmatex">\(w_0=4\)</span> et <span class="arithmatex">\(w_{n+1}=w_n+5\)</span>. Calculer <span class="arithmatex">\(w_1\)</span>.</li>
<li value="5">Pour la même suite, calculer <span class="arithmatex">\(w_2\)</span>.</li>
<li value="6">Dans <span class="arithmatex">\(a_n=7-2n\)</span>, quel est le rang de <span class="arithmatex">\(a_4\)</span> ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Le rang est l'indice.</li><li>Remplacer <span class="arithmatex">\(n\)</span> par la valeur demandée.</li><li>Avec une récurrence, avancer terme après terme.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas confondre <span class="arithmatex">\(u_5\)</span> et le 5e terme si la suite commence à <span class="arithmatex">\(0\)</span>.</li><li>Une formule avec <span class="arithmatex">\(u_{n+1}\)</span> donne le terme suivant.</li></ul>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(u_0=2\times0+3=\boxed{3}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(u_5=\)</span><wbr><span class="arithmatex">\(2\times5+3=\)</span><wbr><span class="arithmatex">\(\boxed{13}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(v_3=3^2-1=9-1=\boxed{8}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(w_1=w_0+5=4+5=\boxed{9}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(w_2=w_1+5=9+5=\boxed{14}\)</span>.</li>
    <li value="6">Dans <span class="arithmatex">\(a_4\)</span>, le rang est <span class="arithmatex">\(\boxed{4}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Une suite est une liste indexée. Une formule explicite calcule directement ; une récurrence avance pas à pas.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Toujours vérifier le premier rang : <span class="arithmatex">\(0\)</span> ou <span class="arithmatex">\(1\)</span>.</div>

## Série B — Formule explicite ou récurrence

<p class="auto-meta">⏱ 8 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Dire si la suite est définie explicitement ou par récurrence, puis calculer.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(u_n=5n-2\)</span>. Type de définition ?</li>
<li value="2"><span class="arithmatex">\(v_0=1\)</span>, <span class="arithmatex">\(v_{n+1}=3v_n\)</span>. Type de définition ?</li>
<li value="3"><span class="arithmatex">\(a_n=10-4n\)</span>. Calculer <span class="arithmatex">\(a_2\)</span>.</li>
<li value="4"><span class="arithmatex">\(b_0=2\)</span>, <span class="arithmatex">\(b_{n+1}=b_n^2+1\)</span>. Calculer <span class="arithmatex">\(b_1\)</span>.</li>
<li value="5">Pour la même suite, calculer <span class="arithmatex">\(b_2\)</span>.</li>
<li value="6"><span class="arithmatex">\(c_n=2^n+1\)</span>. Calculer <span class="arithmatex">\(c_3\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Explicite : <span class="arithmatex">\(u_n\)</span> dépend directement de <span class="arithmatex">\(n\)</span>.</li><li>Récurrence : <span class="arithmatex">\(u_{n+1}\)</span> dépend d'un terme précédent.</li><li>Écrire les termes dans l'ordre.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Une formule comme <span class="arithmatex">\(u_{n+1}\)</span> n'est pas une formule de <span class="arithmatex">\(u_n\)</span>.</li><li>Ne pas sauter un terme dans une définition par récurrence.</li></ul>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(u_n=5n-2\)</span> : <span class="arithmatex">\(\boxed{\text{formule explicite}}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(v_{n+1}=3v_n\)</span> avec <span class="arithmatex">\(v_0=1\)</span> : <span class="arithmatex">\(\boxed{\text{récurrence}}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(a_2=\)</span><wbr><span class="arithmatex">\(10-4\times2=\)</span><wbr><span class="arithmatex">\(10-8=\)</span><wbr><span class="arithmatex">\(\boxed{2}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(b_1=\)</span><wbr><span class="arithmatex">\(b_0^2+1=\)</span><wbr><span class="arithmatex">\(2^2+1=\)</span><wbr><span class="arithmatex">\(\boxed{5}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(b_2=\)</span><wbr><span class="arithmatex">\(b_1^2+1=\)</span><wbr><span class="arithmatex">\(5^2+1=\)</span><wbr><span class="arithmatex">\(\boxed{26}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(c_3=2^3+1=8+1=\boxed{9}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Pour une récurrence, créer une petite chaîne : <span class="arithmatex">\(b_0\rightarrow b_1\rightarrow b_2\)</span>.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Le terme initial est indispensable pour démarrer une suite récurrente.</div>

## Série C — Représenter une suite

<p class="auto-meta">⏱ 8 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Passer d'un tableau ou d'une description à des termes de suite.
</div>

<ol class="auto-questions">
<li value="1">Une suite commence par <span class="arithmatex">\(3;7;11;15\)</span>. Donner <span class="arithmatex">\(u_0\)</span> et <span class="arithmatex">\(u_1\)</span>.</li>
<li value="2">Dans la même suite, conjecturer <span class="arithmatex">\(u_4\)</span>.</li>
<li value="3">Un motif a <span class="arithmatex">\(4\)</span> carrés au rang <span class="arithmatex">\(0\)</span>, puis on ajoute <span class="arithmatex">\(3\)</span> carrés. Donner <span class="arithmatex">\(u_2\)</span>.</li>
<li value="4">Une population vaut <span class="arithmatex">\(200\)</span>, puis augmente de <span class="arithmatex">\(20\)</span> chaque mois. Donner <span class="arithmatex">\(p_3\)</span> si <span class="arithmatex">\(p_0=200\)</span>.</li>
<li value="5">Une valeur est multipliée par <span class="arithmatex">\(2\)</span> à chaque étape, avec <span class="arithmatex">\(q_0=5\)</span>. Donner <span class="arithmatex">\(q_3\)</span>.</li>
<li value="6">Suite donnée par <span class="arithmatex">\(r_{n+1}=r_n-4\)</span>, <span class="arithmatex">\(r_0=18\)</span>. Donner <span class="arithmatex">\(r_3\)</span>.</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Associer rang et position dans la liste.</li><li>Traduire « ajouter » ou « multiplier ».</li><li>Une conjecture se vérifie ensuite.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas oublier que <span class="arithmatex">\(u_0\)</span> est le premier terme si le rang initial est <span class="arithmatex">\(0\)</span>.</li><li>Un modèle n'est fiable que dans son contexte.</li></ul>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1">Si la suite commence au rang <span class="arithmatex">\(0\)</span>, <span class="arithmatex">\(u_0=\boxed{3}\)</span> et <span class="arithmatex">\(u_1=\boxed{7}\)</span>.</li>
    <li value="2">On ajoute <span class="arithmatex">\(4\)</span> à chaque rang, donc <span class="arithmatex">\(u_4=15+4=\boxed{19}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(u_0=4\)</span>, <span class="arithmatex">\(u_1=7\)</span>, <span class="arithmatex">\(u_2=10\)</span>. Donc <span class="arithmatex">\(\boxed{u_2=10}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(p_3=\)</span><wbr><span class="arithmatex">\(200+3\times20=\)</span><wbr><span class="arithmatex">\(\boxed{260}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(q_1=10\)</span>, <span class="arithmatex">\(q_2=20\)</span>, <span class="arithmatex">\(q_3=\boxed{40}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(r_1=14\)</span>, <span class="arithmatex">\(r_2=10\)</span>, <span class="arithmatex">\(r_3=\boxed{6}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Une représentation peut être une liste, un tableau, un nuage de points ou une règle de calcul.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Le rang <span class="arithmatex">\(3\)</span> demande trois évolutions à partir du rang <span class="arithmatex">\(0\)</span>.</div>

## Série D — Type épreuve anticipée : QCM

<p class="auto-meta">⏱ 5 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Choisir une seule réponse. Aucune justification n'est demandée.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(u_n=3n+1\)</span>. <span class="arithmatex">\(u_4=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(7\)</span></li><li><span class="arithmatex">\(10\)</span></li><li><span class="arithmatex">\(13\)</span></li><li><span class="arithmatex">\(15\)</span></li></ol></li>
<li value="2"><span class="arithmatex">\(u_0=2\)</span>, <span class="arithmatex">\(u_{n+1}=u_n+3\)</span>. <span class="arithmatex">\(u_2=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(5\)</span></li><li><span class="arithmatex">\(6\)</span></li><li><span class="arithmatex">\(8\)</span></li><li><span class="arithmatex">\(11\)</span></li></ol></li>
<li value="3"><span class="arithmatex">\(v_n=2^n\)</span>. <span class="arithmatex">\(v_0=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(0\)</span></li><li><span class="arithmatex">\(1\)</span></li><li><span class="arithmatex">\(2\)</span></li><li><span class="arithmatex">\(4\)</span></li></ol></li>
<li value="4">La définition <span class="arithmatex">\(w_{n+1}=4w_n-1\)</span> est :<ol class="auto-choix" type="A"><li><span class="arithmatex">\(explicite\)</span></li><li><span class="arithmatex">\(récurrente\)</span></li><li><span class="arithmatex">\(graphique\)</span></li><li><span class="arithmatex">\(constante\)</span></li></ol></li>
<li value="5">Dans <span class="arithmatex">\(a_7\)</span>, le rang est :<ol class="auto-choix" type="A"><li><span class="arithmatex">\(a\)</span></li><li><span class="arithmatex">\(0\)</span></li><li><span class="arithmatex">\(7\)</span></li><li><span class="arithmatex">\(8\)</span></li></ol></li>
<li value="6"><span class="arithmatex">\(b_1=5\)</span>, <span class="arithmatex">\(b_{n+1}=b_n-2\)</span>. <span class="arithmatex">\(b_3=\)</span><ol class="auto-choix" type="A"><li><span class="arithmatex">\(1\)</span></li><li><span class="arithmatex">\(3\)</span></li><li><span class="arithmatex">\(5\)</span></li><li><span class="arithmatex">\(7\)</span></li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Vérifier le premier rang.</li><li>Pour un QCM, tester vite la formule.</li><li>Éliminer les réponses impossibles.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li><span class="arithmatex">\(2^0=1\)</span>.</li><li><span class="arithmatex">\(u_{n+1}\)</span> désigne le terme suivant, pas le terme <span class="arithmatex">\(n+1\)</span> déjà connu.</li></ul>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse C</strong> : <span class="arithmatex">\(u_4=3\times4+1=13\)</span>.</li>
    <li value="2"><strong class="auto-resultat">Réponse C</strong> : <span class="arithmatex">\(u_1=5\)</span>, <span class="arithmatex">\(u_2=8\)</span>.</li>
    <li value="3"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(2^0=1\)</span>.</li>
    <li value="4"><strong class="auto-resultat">Réponse B</strong> : Elle utilise le terme précédent.</li>
    <li value="5"><strong class="auto-resultat">Réponse C</strong> : L'indice <span class="arithmatex">\(7\)</span> est le rang.</li>
    <li value="6"><strong class="auto-resultat">Réponse A</strong> : <span class="arithmatex">\(b_2=3\)</span>, <span class="arithmatex">\(b_3=1\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Lire d'abord le type de définition : directe ou pas à pas.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Les suites commencent souvent au rang <span class="arithmatex">\(0\)</span>, ce qui change le comptage.</div>

---

*Ces questions reprennent le diaporama d'automatismes N11 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
