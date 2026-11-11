---
title: "QCM automatismes Première spécialité – Algorithmique (interactif, corrigé)"
description: "QCM en ligne d'automatismes de Première spécialité (algorithmique) : chronomètre, score immédiat et correction détaillée, sans calculatrice."
---

# QCM interactif — Algorithmique

Entraînement **sans calculatrice**. Rien n'est enregistré ni envoyé : tout se passe dans le navigateur.

[← Énoncés et corrigés à lire](automatismes-N14-algorithmique.md)

<div class="auto-qcm" data-banque="banque-automatismes"></div>

<script type="application/json" id="banque-automatismes">
{
 "notion": "N14",
 "cle": "N14",
 "titre": "Algorithmique",
 "niveau": "Première spécialité",
 "series": [
  {
   "lettre": "A",
   "theme": "Tracer des affectations",
   "duree": "6 min",
   "consigne": "Compléter mentalement les valeurs obtenues après les instructions.",
   "qcm": false,
   "figure": ""
  },
  {
   "lettre": "B",
   "theme": "Boucles et répétitions",
   "duree": "8 min",
   "consigne": "Déterminer le résultat obtenu après une boucle courte.",
   "qcm": false,
   "figure": ""
  },
  {
   "lettre": "C",
   "theme": "Lire et contrôler un algorithme",
   "duree": "8 min",
   "consigne": "Associer un petit algorithme à une suite ou à une somme.",
   "qcm": false,
   "figure": ""
  },
  {
   "lettre": "D",
   "theme": "QCM : sortie d'algorithme",
   "duree": "6 min",
   "consigne": "Choisir la seule réponse correcte.",
   "qcm": true,
   "figure": ""
  }
 ],
 "questions": [
  {
   "id": "N14-A1",
   "serie": "A",
   "theme": "Tracer des affectations",
   "type": "flash",
   "enonce": "<span class=\"arithmatex\">\\(\\texttt{x=4 ; x=x+3}\\)<\/span>. Quelle est la valeur finale de <span class=\"arithmatex\">\\(x\\)<\/span> ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(x\\)<\/span> vaut d'abord <span class=\"arithmatex\">\\(4\\)<\/span>, puis <span class=\"arithmatex\">\\(4+3\\)<\/span>, donc <span class=\"arithmatex\">\\(\\boxed{7}\\)<\/span>.",
   "methode": "Faire une trace d'exécution : une ligne par instruction, une colonne par variable."
  },
  {
   "id": "N14-A2",
   "serie": "A",
   "theme": "Tracer des affectations",
   "type": "flash",
   "enonce": "<span class=\"arithmatex\">\\(\\texttt{a=2 ; b=5 ; a=a+b}\\)<\/span>. Quelle est la valeur finale de <span class=\"arithmatex\">\\(a\\)<\/span> ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(a\\)<\/span> devient <span class=\"arithmatex\">\\(2+5\\)<\/span>, donc <span class=\"arithmatex\">\\(\\boxed{7}\\)<\/span>.",
   "methode": "Faire une trace d'exécution : une ligne par instruction, une colonne par variable."
  },
  {
   "id": "N14-A3",
   "serie": "A",
   "theme": "Tracer des affectations",
   "type": "flash",
   "enonce": "<span class=\"arithmatex\">\\(\\texttt{u=3}\\)<\/span>, puis deux fois <span class=\"arithmatex\">\\(\\texttt{u=2*u+1}\\)<\/span>. Valeur finale ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(3\\rightarrow 7\\rightarrow 15\\)<\/span>, donc la valeur finale est <span class=\"arithmatex\">\\(\\boxed{15}\\)<\/span>.",
   "methode": "Faire une trace d'exécution : une ligne par instruction, une colonne par variable."
  },
  {
   "id": "N14-A4",
   "serie": "A",
   "theme": "Tracer des affectations",
   "type": "flash",
   "enonce": "<span class=\"arithmatex\">\\(\\texttt{s=0}\\)<\/span>, puis on ajoute <span class=\"arithmatex\">\\(2\\)<\/span> ; <span class=\"arithmatex\">\\(4\\)<\/span> ; <span class=\"arithmatex\">\\(6\\)<\/span>. Valeur finale de <span class=\"arithmatex\">\\(s\\)<\/span> ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(s=0+2+4+6=\\boxed{12}\\)<\/span>.",
   "methode": "Faire une trace d'exécution : une ligne par instruction, une colonne par variable."
  },
  {
   "id": "N14-A5",
   "serie": "A",
   "theme": "Tracer des affectations",
   "type": "flash",
   "enonce": "Dans la liste <span class=\"arithmatex\">\\(\\texttt{L=[4,7,10]}\\)<\/span>, que vaut <span class=\"arithmatex\">\\(\\texttt{L[0]}\\)<\/span> ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(\\texttt{L[0]}\\)<\/span> désigne le premier élément : <span class=\"arithmatex\">\\(\\boxed{4}\\)<\/span>.",
   "methode": "Faire une trace d'exécution : une ligne par instruction, une colonne par variable."
  },
  {
   "id": "N14-A6",
   "serie": "A",
   "theme": "Tracer des affectations",
   "type": "flash",
   "enonce": "Quelles valeurs prend <span class=\"arithmatex\">\\(k\\)<\/span> dans <span class=\"arithmatex\">\\(\\texttt{range(4)}\\)<\/span> ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(\\texttt{range(4)}\\)<\/span> donne <span class=\"arithmatex\">\\(\\boxed{0;1;2;3}\\)<\/span>.",
   "methode": "Faire une trace d'exécution : une ligne par instruction, une colonne par variable."
  },
  {
   "id": "N14-B1",
   "serie": "B",
   "theme": "Boucles et répétitions",
   "type": "flash",
   "enonce": "<span class=\"arithmatex\">\\(u=5\\)<\/span>. On répète trois fois : <span class=\"arithmatex\">\\(u\\leftarrow u+4\\)<\/span>. Valeur finale ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(5\\rightarrow 9\\rightarrow 13\\rightarrow 17\\)<\/span>, donc <span class=\"arithmatex\">\\(\\boxed{17}\\)<\/span>.",
   "methode": "Un tableau de trace évite les erreurs : ligne initiale, puis une ligne par tour."
  },
  {
   "id": "N14-B2",
   "serie": "B",
   "theme": "Boucles et répétitions",
   "type": "flash",
   "enonce": "<span class=\"arithmatex\">\\(v=80\\)<\/span>. On répète deux fois : <span class=\"arithmatex\">\\(v\\leftarrow 0{,}75v\\)<\/span>. Valeur finale ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(80\\rightarrow 60\\rightarrow 45\\)<\/span>, donc <span class=\"arithmatex\">\\(\\boxed{45}\\)<\/span>.",
   "methode": "Un tableau de trace évite les erreurs : ligne initiale, puis une ligne par tour."
  },
  {
   "id": "N14-B3",
   "serie": "B",
   "theme": "Boucles et répétitions",
   "type": "flash",
   "enonce": "<span class=\"arithmatex\">\\(s=0\\)<\/span>. Pour <span class=\"arithmatex\">\\(k=1;2;3;4\\)<\/span>, on fait <span class=\"arithmatex\">\\(s\\leftarrow s+k\\)<\/span>. Valeur finale ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(s=1+2+3+4=\\boxed{10}\\)<\/span>.",
   "methode": "Un tableau de trace évite les erreurs : ligne initiale, puis une ligne par tour."
  },
  {
   "id": "N14-B4",
   "serie": "B",
   "theme": "Boucles et répétitions",
   "type": "flash",
   "enonce": "<span class=\"arithmatex\">\\(u=3\\)<\/span>. On répète <span class=\"arithmatex\">\\(u\\leftarrow 2u\\)<\/span> jusqu'à obtenir <span class=\"arithmatex\">\\(u\\geq 20\\)<\/span>. Combien d'itérations ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(3\\rightarrow 6\\rightarrow 12\\rightarrow 24\\)<\/span>. Il faut <span class=\"arithmatex\">\\(\\boxed{3}\\)<\/span> itérations.",
   "methode": "Un tableau de trace évite les erreurs : ligne initiale, puis une ligne par tour."
  },
  {
   "id": "N14-B5",
   "serie": "B",
   "theme": "Boucles et répétitions",
   "type": "flash",
   "enonce": "Après la question 4, quelle est la valeur finale de <span class=\"arithmatex\">\\(u\\)<\/span> ?",
   "contexte": [
    "<strong>Q4.<\/strong> <span class=\"arithmatex\">\\(u=3\\)<\/span>. On répète <span class=\"arithmatex\">\\(u\\leftarrow 2u\\)<\/span> jusqu'à obtenir <span class=\"arithmatex\">\\(u\\geq 20\\)<\/span>. Combien d'itérations ?"
   ],
   "choix": [],
   "bonne": null,
   "corrige": "La valeur finale de <span class=\"arithmatex\">\\(u\\)<\/span> est <span class=\"arithmatex\">\\(\\boxed{24}\\)<\/span>.",
   "methode": "Un tableau de trace évite les erreurs : ligne initiale, puis une ligne par tour."
  },
  {
   "id": "N14-B6",
   "serie": "B",
   "theme": "Boucles et répétitions",
   "type": "flash",
   "enonce": "Dans une boucle de seuil, que représente le compteur <span class=\"arithmatex\">\\(n\\)<\/span> ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Le compteur indique le <span class=\"arithmatex\">\\(\\boxed{\\text{nombre de tours effectués}}\\)<\/span>.",
   "methode": "Un tableau de trace évite les erreurs : ligne initiale, puis une ligne par tour."
  },
  {
   "id": "N14-C1",
   "serie": "C",
   "theme": "Lire et contrôler un algorithme",
   "type": "flash",
   "enonce": "L'instruction <span class=\"arithmatex\">\\(u\\leftarrow u+6\\)<\/span> modélise-t-elle une évolution additive ou multiplicative ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "<span class=\"arithmatex\">\\(u\\leftarrow u+6\\)<\/span> : évolution <span class=\"arithmatex\">\\(\\boxed{\\text{additive}}\\)<\/span>.",
   "methode": "Un algorithme est une traduction opérationnelle : initialiser, répéter, mettre à jour, renvoyer."
  },
  {
   "id": "N14-C2",
   "serie": "C",
   "theme": "Lire et contrôler un algorithme",
   "type": "flash",
   "enonce": "L'instruction <span class=\"arithmatex\">\\(u\\leftarrow 1{,}08u\\)<\/span> modélise-t-elle une hausse de <span class=\"arithmatex\">\\(8\\%\\)<\/span> ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Oui, multiplier par <span class=\"arithmatex\">\\(1{,}08\\)<\/span> correspond à une <span class=\"arithmatex\">\\(\\boxed{\\text{hausse de $8\\%$}}\\)<\/span>.",
   "methode": "Un algorithme est une traduction opérationnelle : initialiser, répéter, mettre à jour, renvoyer."
  },
  {
   "id": "N14-C3",
   "serie": "C",
   "theme": "Lire et contrôler un algorithme",
   "type": "flash",
   "enonce": "Pour <span class=\"arithmatex\">\\(u_0=2\\)<\/span> et <span class=\"arithmatex\">\\(u_{n+1}=u_n+5\\)<\/span>, quelle instruction met à jour <span class=\"arithmatex\">\\(u\\)<\/span> ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "L'instruction est <span class=\"arithmatex\">\\(\\boxed{u\\leftarrow u+5}\\)<\/span>.",
   "methode": "Un algorithme est une traduction opérationnelle : initialiser, répéter, mettre à jour, renvoyer."
  },
  {
   "id": "N14-C4",
   "serie": "C",
   "theme": "Lire et contrôler un algorithme",
   "type": "flash",
   "enonce": "Pour <span class=\"arithmatex\">\\(u_0=100\\)<\/span> et <span class=\"arithmatex\">\\(u_{n+1}=0{,}9u_n\\)<\/span>, quelle instruction met à jour <span class=\"arithmatex\">\\(u\\)<\/span> ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "L'instruction est <span class=\"arithmatex\">\\(\\boxed{u\\leftarrow 0{,}9u}\\)<\/span>.",
   "methode": "Un algorithme est une traduction opérationnelle : initialiser, répéter, mettre à jour, renvoyer."
  },
  {
   "id": "N14-C5",
   "serie": "C",
   "theme": "Lire et contrôler un algorithme",
   "type": "flash",
   "enonce": "Un algorithme additionne <span class=\"arithmatex\">\\(u_0+u_1+\\cdots+u_5\\)<\/span>. Combien de termes sont ajoutés ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Les rangs <span class=\"arithmatex\">\\(0;1;2;3;4;5\\)<\/span> donnent <span class=\"arithmatex\">\\(\\boxed{6}\\)<\/span> termes.",
   "methode": "Un algorithme est une traduction opérationnelle : initialiser, répéter, mettre à jour, renvoyer."
  },
  {
   "id": "N14-C6",
   "serie": "C",
   "theme": "Lire et contrôler un algorithme",
   "type": "flash",
   "enonce": "Que faut-il initialiser pour calculer une somme dans une boucle ?",
   "contexte": [],
   "choix": [],
   "bonne": null,
   "corrige": "Il faut initialiser une variable, par exemple <span class=\"arithmatex\">\\(\\boxed{s\\leftarrow 0}\\)<\/span>.",
   "methode": "Un algorithme est une traduction opérationnelle : initialiser, répéter, mettre à jour, renvoyer."
  },
  {
   "id": "N14-D1",
   "serie": "D",
   "theme": "QCM : sortie d'algorithme",
   "type": "qcm",
   "enonce": "<span class=\"arithmatex\">\\(x=10\\)<\/span>, puis <span class=\"arithmatex\">\\(x=x-4\\)<\/span>.",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(4\\)<\/span>",
    "<span class=\"arithmatex\">\\(6\\)<\/span>",
    "<span class=\"arithmatex\">\\(14\\)<\/span>"
   ],
   "bonne": 1,
   "corrige": "<span class=\"arithmatex\">\\(10-4=6\\)<\/span>.",
   "methode": "Pour un QCM algorithmique, refaire une trace très courte suffit souvent."
  },
  {
   "id": "N14-D2",
   "serie": "D",
   "theme": "QCM : sortie d'algorithme",
   "type": "qcm",
   "enonce": "<span class=\"arithmatex\">\\(\\texttt{range(3)}\\)<\/span>.",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(1;2;3\\)<\/span>",
    "<span class=\"arithmatex\">\\(0;1;2\\)<\/span>",
    "<span class=\"arithmatex\">\\(0;1;2;3\\)<\/span>"
   ],
   "bonne": 1,
   "corrige": "<span class=\"arithmatex\">\\(\\texttt{range(3)}\\)<\/span> donne <span class=\"arithmatex\">\\(0;1;2\\)<\/span>.",
   "methode": "Pour un QCM algorithmique, refaire une trace très courte suffit souvent."
  },
  {
   "id": "N14-D3",
   "serie": "D",
   "theme": "QCM : sortie d'algorithme",
   "type": "qcm",
   "enonce": "<span class=\"arithmatex\">\\(u=2\\)<\/span>, puis trois fois <span class=\"arithmatex\">\\(u\\leftarrow 3u\\)<\/span>.",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(18\\)<\/span>",
    "<span class=\"arithmatex\">\\(54\\)<\/span>",
    "<span class=\"arithmatex\">\\(6\\)<\/span>"
   ],
   "bonne": 1,
   "corrige": "<span class=\"arithmatex\">\\(2\\rightarrow6\\rightarrow18\\rightarrow54\\)<\/span>.",
   "methode": "Pour un QCM algorithmique, refaire une trace très courte suffit souvent."
  },
  {
   "id": "N14-D4",
   "serie": "D",
   "theme": "QCM : sortie d'algorithme",
   "type": "qcm",
   "enonce": "Un seuil <span class=\"arithmatex\">\\(u\\geq 50\\)<\/span> est atteint à <span class=\"arithmatex\">\\(n=4\\)<\/span>. On renvoie",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(4\\)<\/span>",
    "<span class=\"arithmatex\">\\(50\\)<\/span>",
    "<span class=\"arithmatex\">\\(u_4-50\\)<\/span>"
   ],
   "bonne": 0,
   "corrige": "Le compteur renvoie le premier rang trouvé.",
   "methode": "Pour un QCM algorithmique, refaire une trace très courte suffit souvent."
  },
  {
   "id": "N14-D5",
   "serie": "D",
   "theme": "QCM : sortie d'algorithme",
   "type": "qcm",
   "enonce": "Dans <span class=\"arithmatex\">\\(\\texttt{L=[8,9,10]}\\)<\/span>, <span class=\"arithmatex\">\\(\\texttt{L[2]}\\)<\/span> vaut",
   "contexte": [],
   "choix": [
    "<span class=\"arithmatex\">\\(9\\)<\/span>",
    "<span class=\"arithmatex\">\\(10\\)<\/span>",
    "<span class=\"arithmatex\">\\(2\\)<\/span>"
   ],
   "bonne": 1,
   "corrige": "<span class=\"arithmatex\">\\(\\texttt{L[2]}\\)<\/span> est le troisième élément.",
   "methode": "Pour un QCM algorithmique, refaire une trace très courte suffit souvent."
  },
  {
   "id": "N14-D6",
   "serie": "D",
   "theme": "QCM : sortie d'algorithme",
   "type": "qcm",
   "enonce": "Pour calculer une somme, on utilise surtout",
   "contexte": [],
   "choix": [
    "un accumulateur",
    "une racine",
    "une tangente"
   ],
   "bonne": 0,
   "corrige": "Une somme se construit avec un accumulateur.",
   "methode": "Pour un QCM algorithmique, refaire une trace très courte suffit souvent."
  }
 ]
}
</script>

<noscript>Le QCM interactif nécessite JavaScript. Les énoncés et corrigés sont aussi disponibles <a href="../automatismes-N14-algorithmique/">en lecture</a>.</noscript>
