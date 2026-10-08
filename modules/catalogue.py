import os
import json
def generer_catalogue(dossier_catalogue, chemin_json):
    catalogue = os.listdir(dossier_catalogue)
    liste = []
    extension_autorisee = ['.jpeg', '.png']
    for element in catalogue:
        nom, extension = os.path.splitext(element)
        if extension in extension_autorisee:
            entree = dict(nom = element, chemin = os.path.join(dossier_catalogue, element))
            liste.append(entree)

    with open(chemin_json, "w") as fichier:
        json.dump(liste, fichier)