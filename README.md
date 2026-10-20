💻 Prérequis
Pour installer et exécuter le prototype, les éléments suivants sont nécessaires :
- Python et pip.
- Git.
- Un terminal.
- Un environnement de développement tel que Visual Studio Code, facultatif mais recommandé.
- Les dépendances Python indiquées dans requirements.txt.
- Le fichier du modèle de détection blaze_face_short_range.tflite.
Le projet a été développé et testé dans un environnement Linux sous Ubuntu.

Les commandes ci-dessous utilisent le terminal Ubuntu. Elles peuvent nécessiter quelques adaptations sur un autre système d'exploitation.
🚀 Installation
1. Récupérer le projet
Clone le dépôt GitHub :
git clone https://github.com/jinonoa/TheMirror.git

Accède ensuite au dossier du projet :
cd TheMirror

2. Vérifier Python
Vérifie que Python est installé :
python3 --version

Vérifie également que pip est disponible :
python3 -m pip --version

Le projet doit être utilisé avec une version de Python compatible avec les dépendances déclarées dans requirements.txt.
3. Créer un environnement virtuel
Un environnement virtuel permet d'isoler les dépendances du projet de celles installées sur la machine.

Sous Ubuntu, crée l'environnement virtuel avec :
python3 -m venv mirror-env

Si la création échoue parce que le module venv n'est pas installé, installe le paquet correspondant à ta version de Python, puis recommence.

Active ensuite l'environnement :
source mirror-env/bin/activate

Lorsque l'environnement est activé, le terminal affiche généralement (mirror-env) au début de la ligne de commande.
4. Installer les dépendances
Mets pip à jour :
python -m pip install --upgrade pip

Installe ensuite les dépendances déclarées dans le projet :
python -m pip install -r requirements.txt

Cette commande installe notamment les bibliothèques nécessaires au traitement des images et à la détection de visage.
5. Vérifier l'installation
Vérifie que les principales bibliothèques sont accessibles :
python -m pip show Pillow
python -m pip show mediapipe
python -m pip show numpy

Les outils de développement peuvent également être vérifiés :
python -m pip show pytest
python -m pip show mypy
python -m pip show ruff

Si un outil de développement n'est pas présent dans l'environnement, installe-le si nécessaire :
python -m pip install pytest mypy ruff

6. Vérifier le modèle de détection
Le prototype utilise le modèle MediaPipe BlazeFace Short Range.

Vérifie que le fichier suivant est présent :
model/blaze_face_short_range.tflite

Le fichier doit être accessible à l'emplacement attendu par le code de détection.

Si le modèle est absent, la détection ne pourra pas fonctionner tant que le fichier nécessaire n'aura pas été installé au bon emplacement.
🗂️ Configuration des données
Catalogue de coiffures
Le dossier Catalogue/ contient les images sources des coiffures utilisées par le prototype.

Le script de génération du catalogue parcourt les images prises en charge et produit un fichier catalogue.json contenant les informations associées aux fichiers.

La structure des données est documentée dans :
docs/data.md

Avant de lancer le traitement du catalogue, vérifie que le dossier source existe et contient les images attendues.
Images de test
Pour tester le traitement des images, utilise des fichiers adaptés aux formats pris en charge par le code.

Il est également utile de prévoir des cas particuliers, par exemple :
- un fichier image valide ;
- un fichier inexistant ;
- un fichier qui n'est pas une image ;
- une image corrompue ;
- une image dans laquelle aucun visage n'est détecté ;
- une image contenant plusieurs visages.
Ces situations permettent de vérifier le comportement du programme au-delà du cas idéal.
▶️ Exécution du projet
Lancer le prototype
Le projet dispose d'un script de lancement :
./lancer_themirror.sh

Depuis la racine du dépôt, cette commande lance le traitement prévu par le point d'entrée du projet.

Le script a été conçu pour retrouver le dossier du projet et exécuter TheMirror sans nécessiter l'activation manuelle de mirror-env.

Si le terminal indique que le script ne possède pas les permissions nécessaires, vérifie ses droits d'exécution.

Tu peux alors, si nécessaire, lui accorder ce droit :
chmod +x lancer_themirror.sh

Puis relancer :
./lancer_themirror.sh

Comprendre le résultat
Le prototype réalise des opérations de traitement d'images et de gestion de données. Il ne dispose pas encore de l'ensemble de l'interface graphique de prévisualisation virtuelle envisagée pour la version finale.

Selon le traitement exécuté, les résultats peuvent notamment concerner :
- la localisation d'un visage ;
- une image recadrée ;
- une image redimensionnée ;
- une image enregistrée sans métadonnées EXIF ;
- les données du catalogue de coiffures.
Consulte le terminal ainsi que les dossiers de résultats prévus par le projet pour vérifier les opérations effectuées.
🧪 Tests
Les tests automatisés sont regroupés dans le dossier tests/.

Ils servent à vérifier que les fonctions se comportent comme prévu, y compris lorsque les données fournies ne sont pas valides.
1. Activer l'environnement virtuel
Si ce n'est pas déjà fait :
source mirror-env/bin/activate

2. Installer pytest
Si pytest n'est pas encore installé :
python -m pip install pytest

3. Exécuter les tests
Depuis la racine du projet :
python -m pytest tests

Pytest recherche et exécute les tests présents dans le dossier tests/, puis affiche un résumé du résultat.

Pour obtenir plus de détails sur chaque test :
python -m pytest -v tests

4. Types de cas testés
Les tests couvrent les différentes responsabilités du projet, notamment :
- le chargement d'images valides ;
- la gestion des fichiers absents ou invalides ;
- le recadrage et les dimensions des images produites ;
- la conservation des proportions lors du redimensionnement ;
- la suppression des métadonnées EXIF ;
- la génération du catalogue JSON ;
- la gestion de dossiers absents ou vides ;
- les situations où la détection de visage ne produit pas de résultat exploitable.
Les tests de recadrage vérifient également les pixels de l'image obtenue, et pas uniquement ses dimensions. Cela permet de s'assurer que le recadrage correspond bien à la zone attendue.

Pour la détection de visage, les tests doivent distinguer les cas où aucun visage n'est détecté et ceux où plusieurs visages sont présents, conformément au comportement attendu du module.
🔍 Vérification de la qualité du code
TheMirror utilise des outils complémentaires pour améliorer la fiabilité et la lisibilité du code.
Ruff : vérification du code
Pour détecter les problèmes de style, les imports inutilisés et d'autres erreurs courantes :
python -m ruff check modules tests

Pour appliquer automatiquement les corrections prises en charge :
python -m ruff check --fix modules tests

Pour vérifier le formatage :
python -m ruff format --check modules tests

Pour formater les fichiers :
python -m ruff format modules tests

La configuration de Ruff se trouve dans pyproject.toml.
mypy : vérification des types
Le projet utilise des annotations de types afin de rendre les fonctions plus explicites et de détecter certaines erreurs avant l'exécution.

La commande suivante a été utilisée pour vérifier les modules :
python -m mypy --disable-error-code=import-untyped modules

La désactivation de import-untyped évite de traiter l'absence de métadonnées de typage de certaines dépendances comme une erreur bloquante. Elle ne signifie pas que toutes les erreurs de types sont ignorées.
⚠️ Limitations actuelles
TheMirror est encore un prototype en cours de développement.

À ce stade :
- le traitement des images constitue la base technique de l'application ;
- la détection de visage sert à localiser une zone du visage, mais ne permet pas à elle seule d'essayer virtuellement une coiffure ;
- la gestion du catalogue est orientée vers les fichiers et les données ;
- l'expérience complète de prévisualisation virtuelle n'est pas encore disponible ;
- aucune décision automatique sur la pertinence d'une coiffure pour une cliente n'est prise.
Le projet évoluera progressivement à mesure que les fonctionnalités seront développées et testées.
🛣️ Améliorations envisagées
Les prochaines étapes du développement pourront inclure :
- [ ] Développer une interface utilisateur.
- [ ] Permettre à une cliente de sélectionner un modèle dans le catalogue.
- [ ] Mettre en place la prévisualisation d'une coiffure sur une image.
- [ ] Améliorer le positionnement et le rendu des coiffures.
- [ ] Faciliter la comparaison entre plusieurs modèles.
- [ ] Ajouter des fonctions de gestion du catalogue depuis l'interface.
- [ ] Renforcer les tests à mesure que de nouvelles fonctionnalités apparaissent.
- [ ] Améliorer la documentation technique et utilisateur.
Cette liste représente des pistes d'évolution et ne signifie pas que ces fonctionnalités sont déjà implémentées.
