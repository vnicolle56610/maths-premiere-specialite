---
title: "Automatismes Première spécialité – Algorithmique : exercices et QCM corrigés"
description: "24 questions d'automatismes de Première spécialité (algorithmique), sans calculatrice, en 4 séries chronométrées, avec corrigés détaillés et QCM interactif."
---

# Automatismes N14 — Algorithmique

24 questions **sans calculatrice**, réparties en 4 séries courtes à faire en quelques minutes. Chercher d'abord seul, puis ouvrir le corrigé.

<div class="auto-actions" markdown>
[⚡ Faire le QCM interactif](qcm-N14-algorithmique.md){ .md-button .md-button--primary }
[📄 Diaporama PDF à projeter](AUTOMATISMES_N14_ALGORITHMIQUE.pdf){ .md-button }
[📖 Revoir la notion](../notions/N14-algorithmique.md){ .md-button }
</div>

## Série A — Tracer des affectations

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Compléter mentalement les valeurs obtenues après les instructions.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(\texttt{x=4 ; x=x+3}\)</span>. Quelle est la valeur finale de <span class="arithmatex">\(x\)</span> ?</li>
<li value="2"><span class="arithmatex">\(\texttt{a=2 ; b=5 ; a=a+b}\)</span>. Quelle est la valeur finale de <span class="arithmatex">\(a\)</span> ?</li>
<li value="3"><span class="arithmatex">\(\texttt{u=3}\)</span>, puis deux fois <span class="arithmatex">\(\texttt{u=2*u+1}\)</span>. Valeur finale ?</li>
<li value="4"><span class="arithmatex">\(\texttt{s=0}\)</span>, puis on ajoute <span class="arithmatex">\(2\)</span> ; <span class="arithmatex">\(4\)</span> ; <span class="arithmatex">\(6\)</span>. Valeur finale de <span class="arithmatex">\(s\)</span> ?</li>
<li value="5">Dans la liste <span class="arithmatex">\(\texttt{L=[4,7,10]}\)</span>, que vaut <span class="arithmatex">\(\texttt{L[0]}\)</span> ?</li>
<li value="6">Quelles valeurs prend <span class="arithmatex">\(k\)</span> dans <span class="arithmatex">\(\texttt{range(4)}\)</span> ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Une affectation remplace l'ancienne valeur.</li><li>Dans une liste Python, le premier indice est <span class="arithmatex">\(0\)</span>.</li><li><span class="arithmatex">\(\texttt{range(n)}\)</span> s'arrête avant <span class="arithmatex">\(n\)</span>.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Lire les instructions dans l'ordre.</li><li>Ne pas confondre égalité mathématique et affectation informatique.</li></ul>

??? success "Corrigé de la série A"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(x\)</span> vaut d'abord <span class="arithmatex">\(4\)</span>, puis <span class="arithmatex">\(4+3\)</span>, donc <span class="arithmatex">\(\boxed{7}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(a\)</span> devient <span class="arithmatex">\(2+5\)</span>, donc <span class="arithmatex">\(\boxed{7}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(3\rightarrow 7\rightarrow 15\)</span>, donc la valeur finale est <span class="arithmatex">\(\boxed{15}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(s=0+2+4+6=\boxed{12}\)</span>.</li>
    <li value="5"><span class="arithmatex">\(\texttt{L[0]}\)</span> désigne le premier élément : <span class="arithmatex">\(\boxed{4}\)</span>.</li>
    <li value="6"><span class="arithmatex">\(\texttt{range(4)}\)</span> donne <span class="arithmatex">\(\boxed{0;1;2;3}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Faire une trace d'exécution : une ligne par instruction, une colonne par variable.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Le symbole <span class="arithmatex">\(=\)</span> en Python signifie « reçoit la valeur ».</div>

## Série B — Boucles et répétitions

<p class="auto-meta">⏱ 8 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Déterminer le résultat obtenu après une boucle courte.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(u=5\)</span>. On répète trois fois : <span class="arithmatex">\(u\leftarrow u+4\)</span>. Valeur finale ?</li>
<li value="2"><span class="arithmatex">\(v=80\)</span>. On répète deux fois : <span class="arithmatex">\(v\leftarrow 0{,}75v\)</span>. Valeur finale ?</li>
<li value="3"><span class="arithmatex">\(s=0\)</span>. Pour <span class="arithmatex">\(k=1;2;3;4\)</span>, on fait <span class="arithmatex">\(s\leftarrow s+k\)</span>. Valeur finale ?</li>
<li value="4"><span class="arithmatex">\(u=3\)</span>. On répète <span class="arithmatex">\(u\leftarrow 2u\)</span> jusqu'à obtenir <span class="arithmatex">\(u\geq 20\)</span>. Combien d'itérations ?</li>
<li value="5">Après la question 4, quelle est la valeur finale de <span class="arithmatex">\(u\)</span> ?</li>
<li value="6">Dans une boucle de seuil, que représente le compteur <span class="arithmatex">\(n\)</span> ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Repérer ce qui est répété.</li><li>Mettre à jour le compteur après chaque tour.</li><li>Pour un seuil, s'arrêter dès que la condition est vérifiée.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas faire un tour de trop.</li><li>Le test du seuil se fait sur la valeur courante.</li></ul>

??? success "Corrigé de la série B"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(5\rightarrow 9\rightarrow 13\rightarrow 17\)</span>, donc <span class="arithmatex">\(\boxed{17}\)</span>.</li>
    <li value="2"><span class="arithmatex">\(80\rightarrow 60\rightarrow 45\)</span>, donc <span class="arithmatex">\(\boxed{45}\)</span>.</li>
    <li value="3"><span class="arithmatex">\(s=1+2+3+4=\boxed{10}\)</span>.</li>
    <li value="4"><span class="arithmatex">\(3\rightarrow 6\rightarrow 12\rightarrow 24\)</span>. Il faut <span class="arithmatex">\(\boxed{3}\)</span> itérations.</li>
    <li value="5">La valeur finale de <span class="arithmatex">\(u\)</span> est <span class="arithmatex">\(\boxed{24}\)</span>.</li>
    <li value="6">Le compteur indique le <span class="arithmatex">\(\boxed{\text{nombre de tours effectués}}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Un tableau de trace évite les erreurs : ligne initiale, puis une ligne par tour.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Dans une boucle « tant que », la condition d'arrêt n'est pas toujours atteinte exactement.</div>

## Série C — Lire et contrôler un algorithme

<p class="auto-meta">⏱ 8 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Associer un petit algorithme à une suite ou à une somme.
</div>

<ol class="auto-questions">
<li value="1">L'instruction <span class="arithmatex">\(u\leftarrow u+6\)</span> modélise-t-elle une évolution additive ou multiplicative ?</li>
<li value="2">L'instruction <span class="arithmatex">\(u\leftarrow 1{,}08u\)</span> modélise-t-elle une hausse de <span class="arithmatex">\(8\%\)</span> ?</li>
<li value="3">Pour <span class="arithmatex">\(u_0=2\)</span> et <span class="arithmatex">\(u_{n+1}=u_n+5\)</span>, quelle instruction met à jour <span class="arithmatex">\(u\)</span> ?</li>
<li value="4">Pour <span class="arithmatex">\(u_0=100\)</span> et <span class="arithmatex">\(u_{n+1}=0{,}9u_n\)</span>, quelle instruction met à jour <span class="arithmatex">\(u\)</span> ?</li>
<li value="5">Un algorithme additionne <span class="arithmatex">\(u_0+u_1+\cdots+u_5\)</span>. Combien de termes sont ajoutés ?</li>
<li value="6">Que faut-il initialiser pour calculer une somme dans une boucle ?</li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Addition répétée : modèle arithmétique.</li><li>Multiplication répétée : modèle géométrique.</li><li>Une somme a besoin d'un accumulateur.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>De <span class="arithmatex">\(0\)</span> à <span class="arithmatex">\(5\)</span>, il y a six rangs.</li><li>Ne pas oublier la valeur initiale de l'accumulateur.</li></ul>

??? success "Corrigé de la série C"

    <ol class="auto-corrige">
    <li value="1"><span class="arithmatex">\(u\leftarrow u+6\)</span> : évolution <span class="arithmatex">\(\boxed{\text{additive}}\)</span>.</li>
    <li value="2">Oui, multiplier par <span class="arithmatex">\(1{,}08\)</span> correspond à une <span class="arithmatex">\(\boxed{\text{hausse de $8\%$}}\)</span>.</li>
    <li value="3">L'instruction est <span class="arithmatex">\(\boxed{u\leftarrow u+5}\)</span>.</li>
    <li value="4">L'instruction est <span class="arithmatex">\(\boxed{u\leftarrow 0{,}9u}\)</span>.</li>
    <li value="5">Les rangs <span class="arithmatex">\(0;1;2;3;4;5\)</span> donnent <span class="arithmatex">\(\boxed{6}\)</span> termes.</li>
    <li value="6">Il faut initialiser une variable, par exemple <span class="arithmatex">\(\boxed{s\leftarrow 0}\)</span>.</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Un algorithme est une traduction opérationnelle : initialiser, répéter, mettre à jour, renvoyer.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Un accumulateur non initialisé rend le calcul impossible à contrôler.</div>

## Série D — QCM : sortie d'algorithme

<p class="auto-meta">⏱ 6 min · Calculatrice interdite</p>

<div class="auto-consigne" markdown>
**Consigne.** Choisir la seule réponse correcte.
</div>

<ol class="auto-questions">
<li value="1"><span class="arithmatex">\(x=10\)</span>, puis <span class="arithmatex">\(x=x-4\)</span>.<ol class="auto-choix" type="A"><li><span class="arithmatex">\(4\)</span></li><li><span class="arithmatex">\(6\)</span></li><li><span class="arithmatex">\(14\)</span></li></ol></li>
<li value="2"><span class="arithmatex">\(\texttt{range(3)}\)</span>.<ol class="auto-choix" type="A"><li><span class="arithmatex">\(1;2;3\)</span></li><li><span class="arithmatex">\(0;1;2\)</span></li><li><span class="arithmatex">\(0;1;2;3\)</span></li></ol></li>
<li value="3"><span class="arithmatex">\(u=2\)</span>, puis trois fois <span class="arithmatex">\(u\leftarrow 3u\)</span>.<ol class="auto-choix" type="A"><li><span class="arithmatex">\(18\)</span></li><li><span class="arithmatex">\(54\)</span></li><li><span class="arithmatex">\(6\)</span></li></ol></li>
<li value="4">Un seuil <span class="arithmatex">\(u\geq 50\)</span> est atteint à <span class="arithmatex">\(n=4\)</span>. On renvoie<ol class="auto-choix" type="A"><li><span class="arithmatex">\(4\)</span></li><li><span class="arithmatex">\(50\)</span></li><li><span class="arithmatex">\(u_4-50\)</span></li></ol></li>
<li value="5">Dans <span class="arithmatex">\(\texttt{L=[8,9,10]}\)</span>, <span class="arithmatex">\(\texttt{L[2]}\)</span> vaut<ol class="auto-choix" type="A"><li><span class="arithmatex">\(9\)</span></li><li><span class="arithmatex">\(10\)</span></li><li><span class="arithmatex">\(2\)</span></li></ol></li>
<li value="6">Pour calculer une somme, on utilise surtout<ol class="auto-choix" type="A"><li>un accumulateur</li><li>une racine</li><li>une tangente</li></ol></li>
</ol>

??? tip "Coup de pouce"

    <p><strong>Conseils</strong></p><ul><li>Traiter chaque proposition par élimination.</li><li>Les indices Python commencent à <span class="arithmatex">\(0\)</span>.</li><li>Une sortie d'algorithme doit être interprétée.</li></ul>
    <p><strong>Vigilance</strong></p><ul><li>Ne pas lire <span class="arithmatex">\(\texttt{x=x-4}\)</span> comme une égalité impossible.</li><li>Une variable peut changer plusieurs fois.</li></ul>

??? success "Corrigé de la série D"

    <ol class="auto-corrige">
    <li value="1"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(10-4=6\)</span>, réponse .</li>
    <li value="2"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(\texttt{range(3)}\)</span> donne <span class="arithmatex">\(0;1;2\)</span>, réponse .</li>
    <li value="3"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(2\rightarrow6\rightarrow18\rightarrow54\)</span>, réponse .</li>
    <li value="4"><strong class="auto-resultat">Réponse A</strong> : Le compteur renvoie le premier rang trouvé : réponse .</li>
    <li value="5"><strong class="auto-resultat">Réponse B</strong> : <span class="arithmatex">\(\texttt{L[2]}\)</span> est le troisième élément : réponse .</li>
    <li value="6"><strong class="auto-resultat">Réponse A</strong> : Une somme se construit avec un accumulateur : réponse .</li>
    </ol>
    <div class="auto-methode"><strong>Méthode.</strong> Pour un QCM algorithmique, refaire une trace très courte suffit souvent.</div>
    <div class="auto-vigilance"><strong>Vigilance.</strong> Une réponse numérique doit être reliée à la variable affichée ou renvoyée.</div>

---

*Ces questions reprennent le diaporama d'automatismes N14 utilisé en classe. Licence CC BY-NC-SA 4.0 : réutilisation libre en classe, en citant la source.*
