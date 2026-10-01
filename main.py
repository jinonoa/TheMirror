import numpy as np
import mediapipe as mp
import os
from PIL import Image, UnidentifiedImageError
def ouvrir_image(chemin):
    if not os.path.isfile(chemin):
        return "Le fichier est inexistant"

    try:
        image = Image.open(chemin)
        image.verify()
        image = Image.open(chemin)
    except UnidentifiedImageError:
       return "Le fichier n'est pas une image ou est corrompu"

    format_autorise = ['jpeg', 'png']
    propriete = image.format.lower()
    
    if propriete not in format_autorise:
        return "Format non autorisé"
    return image

def reperage(chemin):
    image = ouvrir_image(chemin)
    if isinstance(image, str):
        print("L'opération est impossible")
    else:
        image_mp = mp.Image(image_format = mp.ImageFormat.SRGB, data = np.array(image))
        model_path = 'model/blaze_face_short_range.tflite'
        FaceDetector = mp.tasks.vision.FaceDetector 
        with FaceDetector.create_from_model_path(model_path) as detector:
            resultat = detector.detect(image_mp)
            if resultat.detections:
                visage = resultat.detections[0]
                x = visage.bounding_box.origin_x
                y = visage.bounding_box.origin_y
                largeur = visage.bounding_box.width
                hauteur = visage.bounding_box.height
                left = x
                top = y
                right = x + largeur
                bottom = y + hauteur
                image_recadree = image.crop((left, top, right, bottom))
                image_recadree.thumbnail((500, 500))
                nouvelle_image = Image.new(image_recadree.mode, image_recadree.size)
                nouvelle_image.paste(image_recadree)
                nouvelle_image.save("/home/eduleboss/Documents/TheMirror/resultat/photo_01.jpg")

catalogue = os.listdir("/home/eduleboss/Documents/TheMirror/Catalogue/")
chemin_catalogue = "/home/eduleboss/Documents/TheMirror/Catalogue/"
Liste = []
for element in catalogue:
    entree = dict(nom = element, chemin = os.path.join(chemin_catalogue, element))
    Liste.append(entree)

with open("/home/eduleboss/Documents/TheMirror/catalogue.json", "w") as fichier:
    json.dump(liste, fichier)