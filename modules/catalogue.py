import os
import json
from modules.models import Coiffure
from dataclasses import asdict 
def generer_catalogue(dossier_catalogue, chemin_json):
    catalogue = os.listdir(dossier_catalogue)
    liste = []
    extension_autorisee = ['.jpeg', '.png']
    for element in catalogue:
        chemin_element = os.path.join(dossier_catalogue, element)
        if not os.path.isfile(chemin_element):
            continue
        nom, extension = os.path.splitext(element)
        if extension.lower() in extension_autorisee:
            entree = Coiffure(nom= nom, chemin= chemin_element)
            liste.append(entree)
    liste_json= [asdict(coiffure) for coiffure in liste]

    with open(chemin_json, "w", encoding= "utf-8") as fichier:
        json.dump(liste_json, fichier, indent="\t")