# Synchronisation automatique du site Première avec le dépôt "Version en cours"

## Objectif

Le site MkDocs ne doit plus contenir d'informations dupliquées.

La structure des notions doit être automatiquement synchronisée à partir du dépôt :

```
IA_AGENT_MATHS/
└── GPT-première/
    └── Version en cours/
        ├── N01_LOGIQUE_ENSEMBLES/
        ├── N02_CALCUL_ALGEBRIQUE_EQUATIONS/
        ├── N03_FONCTIONS_LECTURES_VARIATIONS/
        ...
```

Ces dossiers constituent la référence unique ("single source of truth").

---

# Fonctionnement attendu

Créer un script Python :

```
scripts/synchroniser_notions.py
```

qui est idempotent.

On doit pouvoir lancer :

```bash
python scripts/synchroniser_notions.py
mkdocs build
```

autant de fois que l'on veut.

---

# Le script doit automatiquement

## 1. Lire les dossiers Version en cours

Détecter automatiquement tous les dossiers de la forme

```
Nxx_XXXX
```

Exemple

```
N03_FONCTIONS_LECTURES_VARIATIONS
```

Extraire

```
numéro = N03
nom = FONCTIONS_LECTURES_VARIATIONS
```

---

## 2. Construire les informations dérivées

À partir du nom :

```
FONCTIONS_LECTURES_VARIATIONS
```

construire

slug

```
fonctions-lectures-variations
```

titre lisible

```
Fonctions : lectures et variations
```

Le code devra être facilement personnalisable pour gérer certaines règles typographiques.

Exemple :

```
TAUX_DE_VARIATION

↓

Taux de variation
```

```
FONCTION_EXPONENTIELLE

↓

Fonctions exponentielles
```

etc.

Les règles devront être regroupées dans une fonction dédiée.

---

## 3. Renommer automatiquement

Renommer

```
docs/notions/N03-*.md
```

en

```
docs/notions/N03-fonctions-lectures-variations.md
```

---

## 4. Corriger automatiquement le contenu des fichiers notion

Mettre à jour

Titre :

```
# N03 — Fonctions : lectures et variations
```

Objectifs.

Liens PDF :

```
../cours/COURS_N03_FONCTIONS_LECTURES_VARIATIONS.pdf

../td/TD_N03_FONCTIONS_LECTURES_VARIATIONS.pdf

../automatismes/AUTOMATISMES_N03_FONCTIONS_LECTURES_VARIATIONS.pdf

../corriges/CORRIGE_TD_N03_FONCTIONS_LECTURES_VARIATIONS.pdf
```

Les liens doivent être construits automatiquement.

Aucun nom ne doit être écrit en dur.

---

## 5. Mettre automatiquement à jour mkdocs.yml

La section

```
nav:
```

doit être reconstruite automatiquement.

Aucune entrée ne doit être écrite à la main.

Les notions apparaissent dans l'ordre numérique.

---

## 6. Mettre automatiquement à jour docs/index.md

La liste des notions

```
Accès rapide
```

doit être reconstruite automatiquement.

Elle ne doit jamais être modifiée manuellement.

---

## 7. Vérifier les PDF

Pour chaque notion détecter automatiquement l'existence de :

```
COURS
TD
AUTOMATISMES
CORRIGE
MINITEST
```

Si un document existe :

afficher le lien.

Sinon :

ne pas afficher le lien.

Aucun lien cassé.

---

## 8. Vérification de cohérence

Le script doit produire un rapport :

Exemple

```
✓ N01

✓ N02

✓ N03

⚠ N11
    cours absent

⚠ N12
    TD absent

⚠ N15
    automatismes absents
```

---

## 9. Architecture

Créer une classe

```
Notion
```

contenant

```
numero

nom_machine

slug

titre

cours_pdf

td_pdf

automatismes_pdf

corrige_pdf

minitest_pdf
```

Toutes les pages seront générées à partir de cette structure.

---

## 10. Idempotence

Deux exécutions successives du script ne doivent produire aucune différence.

---

## 11. Généralisation

Le script ne doit contenir aucun chemin spécifique à Première.

Créer une configuration :

```
config_site.yaml
```

contenant par exemple :

source:

```
~/ENSEIGNEMENT/IA_AGENT_MATHS/GPT-première/Version en cours
```

destination :

```
~/ENSEIGNEMENT/maths-premiere-specialite
```

Le même script devra fonctionner ensuite pour

- Seconde

- Terminale

- Maths expertes

en ne changeant que le fichier de configuration.

---

## 12. Bonus

Créer une commande unique :

```
python scripts/publier.py
```

qui effectue :

```
Synchronisation

↓

Vérifications

↓

mkdocs build

↓

Publication GitHub Pages
```

avec un rapport final clair.
