def recadrer(image, coordonnees):
    x = coordonnees.x
    y = coordonnees.y
    largeur = coordonnees.largeur
    hauteur = coordonnees.hauteur
    left = x
    top = y
    right = x + largeur
    bottom = y + hauteur
    image_recadree = image.crop((left, top, right, bottom))
    return image_recadree