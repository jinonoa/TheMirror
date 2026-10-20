from PIL import Image

from modules.models import DetectionResult


def recadrer(image: Image.Image, coordonnees: DetectionResult) -> Image.Image:
    (largeur_image, hauteur_image) = image.size
    x = coordonnees.x
    y = coordonnees.y
    largeur = coordonnees.largeur
    hauteur = coordonnees.hauteur
    left = x
    top = y
    right = min(x + largeur, largeur_image)
    bottom = min(y + hauteur, hauteur_image)
    image_recadree = image.crop((left, top, right, bottom))
    return image_recadree
