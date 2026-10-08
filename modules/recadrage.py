import PIL

def recadrer(image, coordonnees):
    x, y, largeur, hauteur = coordonnees
    x = coordonnees[0]
    y = coordonnees[1]
    largeur = coordonnees[2]
    hauteur = coordonnees[3]
    left = x
    top = y
    right = x + largeur
    bottom = y + hauteur
    image_recadree = image.crop((left, top, right, bottom))
    return image_recadree