from modules.chargement import ouvrir_image
from modules.detection import detecter_visage
from modules.recadrage import recadrer
from modules.redimensionnement import redimensionner
from modules.exif import supprimer_exif
from modules.catalogue import generer_catalogue

import os

generer_catalogue("catalogue", "catalogue.json")
chemin = input("Entrer le chemin de votre image")
image = ouvrir_image(chemin)

if isinstance(image, str):
    print('Votre image ne peut être ouverte')
else:
    coordonnees = detecter_visage(image)
    if coordonnees is not None:
        image_recadree = recadrer(image, coordonnees)
        image_redimensionnee = redimensionner(image_recadree)
        dossier_resultats = "Resultats"
        os.makedirs(dossier_resultats, exist_ok=True)
        nom_fichier = os.path.basename(chemin)
        chemin_sortie = os.path.join(dossier_resultats, nom_fichier)
        new_image = supprimer_exif(image_redimensionnee, chemin_sortie)
        new_image.show()
    else:
        print("Aucun visage n'est détecté sur l'image")