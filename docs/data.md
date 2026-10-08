# Structure des fichiers et des données

1. Objectif

Ce document décrit la structure des fichiers et des données utilisées par TheMirror pour gérer le catalogue de coiffures.

Le catalogue est constitué d'un ensemble d'images stockées dans le dossier `Catalogue/`. Un fichier `catalogue.json` est généré automatiquement afin de référencer ces images et de conserver, pour chacune d'elles, son nom et son chemin d'accès.

Cette organisation permet à l'application de retrouver les images du catalogue de manière structurée plutôt que de devoir définir manuellement chaque image dans le code.
2. Structure des fichiers

Les données du catalogue sont organisées de la manière suivante :

TheMirror/
├── Catalogue/
│   ├── 1900024840229248.jpeg
│   ├── 370210031892181836.jpeg
│   ├── ...
│   ├── curly side puffs.jpeg
│   ├── Perruque courte vague de doigt pour les femmes noir coupe lutin perruques sans colle 100_ cheveux.jpeg
│   └── jpeg(2)
│
├── catalogue.json
│
└── docs/
    └── data.md

Le dossier Catalogue/ contient actuellement 14 fichiers utilisés comme références pour les coiffures.

Les fichiers possèdent des noms provenant de leurs sources d'origine. La majorité des fichiers sont des images au format .jpeg, mais certains noms peuvent être différents, comme jpeg(2).

Le fichier catalogue.json contient les informations permettant de référencer ces fichiers.

Le fichier docs/data.md documente la structure et l'organisation de ces données.

3. Structure de catalogue.json

Le fichier catalogue.json contient une liste d'objets JSON. Chaque objet représente un fichier présent dans le dossier Catalogue/.

Pour chaque fichier, deux informations sont actuellement enregistrées :

nom : le nom du fichier.
chemin : le chemin permettant d'accéder au fichier sur la machine.

Un élément du fichier catalogue.json possède donc actuellement une structure similaire à celle-ci :

{
    "nom": "curly side puffs.jpeg",
    "chemin": "/home/eduleboss/Documents/TheMirror/Catalogue/curly side puffs.jpeg"
}

L'ensemble du catalogue est ensuite représenté sous la forme d'une liste contenant plusieurs de ces objets :

[
    {
        "nom": "1900024840229248.jpeg",
        "chemin": "/home/eduleboss/Documents/TheMirror/Catalogue/1900024840229248.jpeg"
    },
    {
        "nom": "370210031892181836.jpeg",
        "chemin": "/home/eduleboss/Documents/TheMirror/Catalogue/370210031892181836.jpeg"
    }
]

Cette structure permet de séparer les informations décrivant chaque fichier des instructions du programme. Le programme peut ainsi parcourir catalogue.json pour retrouver les différentes images du catalogue.

Champs utilisés
Champ	Type	Rôle
nom	chaîne de caractères	Contient le nom du fichier
chemin	chaîne de caractères	Contient le chemin d'accès au fichier

État actuel : les chemins enregistrés dans catalogue.json sont des chemins absolus correspondant à l'emplacement du projet sur la machine de développement.
4. Génération de catalogue.json

Le fichier catalogue.json est généré automatiquement à partir du contenu du dossier Catalogue/.

La première étape consiste à récupérer les éléments présents dans ce dossier avec os.listdir() :

catalogue = os.listdir("/home/eduleboss/Documents/TheMirror/Catalogue/")

Cette instruction permet d'obtenir une liste contenant les noms des fichiers présents dans le dossier.

Une boucle for permet ensuite de traiter chaque élément de cette liste :

for element in catalogue:

Pour chaque fichier, un dictionnaire est créé avec son nom et son chemin :

entree = dict(
    nom=element,
    chemin=os.path.join(chemin_catalogue, element)
)

Chaque dictionnaire est ensuite ajouté à une liste grâce à append() :

liste.append(entree)

La liste obtenue contient donc une entrée pour chaque fichier du catalogue.

Enfin, le module json permet d'enregistrer cette liste dans le fichier catalogue.json :

with open("/home/eduleboss/Documents/TheMirror/catalogue.json", "w") as fichier:
    json.dump(liste, fichier)

Le mode "w" permet de créer le fichier s'il n'existe pas encore ou de remplacer son contenu s'il existe déjà.

Le résultat est un fichier JSON contenant automatiquement les informations des fichiers présents dans Catalogue/.
Cette génération automatique évite d'avoir à écrire manuellement chaque fichier dans le catalogue.
5. Limites de l'implémentation actuelle

L'implémentation actuelle permet de générer automatiquement le catalogue, mais plusieurs points pourront être améliorés par la suite.

5.1. Utilisation de chemins absolus

Les chemins enregistrés dans catalogue.json correspondent actuellement à l'emplacement exact du projet sur la machine de développement.

Par exemple :

/home/eduleboss/Documents/TheMirror/Catalogue/curly side puffs.jpeg

Ce fonctionnement peut poser un problème si le projet est déplacé sur une autre machine ou si une autre personne souhaite l'utiliser.

À terme, l'utilisation de chemins relatifs pourrait rendre le catalogue plus facilement portable.

5.2. Absence de filtrage des fichiers

os.listdir() récupère tous les éléments présents dans le dossier Catalogue/.

Le programme actuel ne vérifie donc pas encore que chaque élément correspond réellement à une image supportée par TheMirror.

Une amélioration future consistera à filtrer les fichiers selon leurs extensions autorisées avant de les ajouter au catalogue.

5.3. Validation des images

Le programme génère actuellement les entrées du catalogue à partir des noms de fichiers sans vérifier leur validité.

Une image pourrait donc être référencée dans catalogue.json alors qu'elle est corrompue ou qu'elle n'est pas réellement exploitable par l'application.

La fonction ouvrir_image() développée précédemment pourra servir à effectuer cette validation.

5.4. Informations limitées

Chaque entrée contient actuellement uniquement le nom et le chemin du fichier.

Le catalogue pourra évoluer par la suite pour contenir d'autres informations utiles à TheMirror, par exemple des informations permettant d'identifier ou de classer les coiffures.

État actuel : ces améliorations ne sont pas encore nécessaires pour faire fonctionner le catalogue actuel. Elles correspondent à des pistes d'évolution identifiées au cours du développement.
6. Validation du catalogue

Après avoir généré catalogue.json, il est important de vérifier que les données enregistrées correspondent bien aux fichiers présents dans le dossier Catalogue/.

La première vérification consiste à comparer le nombre de fichiers présents dans le dossier avec le nombre d'entrées enregistrées dans le fichier JSON.

Dans l'état actuel du projet, le dossier Catalogue/ contient 14 fichiers. Le fichier catalogue.json doit donc contenir 14 entrées.

Une deuxième vérification consiste à contrôler que chaque chemin enregistré dans le JSON correspond bien à un fichier existant.

Cette vérification permet notamment de détecter une erreur dans la construction des chemins ou une entrée faisant référence à un fichier qui aurait été déplacé ou supprimé.

Enfin, les noms enregistrés dans le champ nom doivent correspondre aux noms réels des fichiers du catalogue.

Vérifications effectuées
Vérification	                                                    Résultat attendu
Nombre de fichiers dans Catalogue/	                                        14
Nombre d'entrées dans catalogue.json	                                    14
Chemins enregistrés	                                           Correspondent aux fichiers présents
Noms enregistrés	                                           Correspondent aux noms réels des fichiers

Cette étape permet de s'assurer que le fichier JSON constitue bien une représentation fidèle du contenu actuel du dossier Catalogue/.

État actuel : le catalogue est généré à partir du contenu du dossier et peut être contrôlé en comparant les entrées du fichier JSON avec les fichiers réellement présents.
7. Évolutions prévues

La structure actuelle du catalogue constitue une première base fonctionnelle. Plusieurs améliorations pourront être apportées au fur et à mesure de l'évolution de TheMirror.

7.1. Utiliser des chemins relatifs

Les chemins absolus utilisés actuellement sont liés à l'environnement de développement.

Une prochaine évolution pourra consister à enregistrer des chemins relatifs au projet afin que le catalogue puisse fonctionner indépendamment de l'emplacement du projet sur la machine.

7.2. Filtrer les fichiers du catalogue

Le programme pourra être amélioré afin de sélectionner uniquement les fichiers correspondant aux formats d'images pris en charge par TheMirror.

Cela permettra notamment d'éviter d'ajouter accidentellement d'autres types de fichiers présents dans le dossier Catalogue/.

7.3. Ajouter des informations sur les coiffures

Le modèle actuel associe principalement un nom et un chemin à chaque fichier.

À mesure que l'application évoluera, le catalogue pourra contenir davantage d'informations permettant de mieux organiser les coiffures et de faciliter leur utilisation par l'application.

Par exemple, des catégories ou des identifiants pourront être ajoutés si ces informations deviennent nécessaires au fonctionnement de TheMirror.

7.4. Automatiser davantage la validation

La validation du catalogue pourra également être intégrée directement au processus de génération.

L'objectif serait de vérifier automatiquement que les fichiers référencés existent, qu'ils peuvent être ouverts et qu'ils correspondent aux formats pris en charge avant de les ajouter au catalogue.

Objectif : conserver une structure de données simple dans un premier temps, puis la faire évoluer uniquement lorsque les besoins réels de TheMirror le nécessiteront.