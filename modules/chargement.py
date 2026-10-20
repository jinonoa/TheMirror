import os

from PIL import Image, UnidentifiedImageError


def ouvrir_image(chemin: str) -> Image.Image | str:
    if not os.path.isfile(chemin):
        return "Le fichier est inexistant"

    try:
        image = Image.open(chemin)
        image.verify()
        image = Image.open(chemin)
    except UnidentifiedImageError:
        return "Le fichier n'est pas une image ou est corrompu"

    format_autorise = ["jpeg", "png"]
    if image.format is None:
        return "Votre image ne possède pas d'extension"
    propriete = image.format.lower()

    if propriete not in format_autorise:
        return "Format non autorisé"
    return image
