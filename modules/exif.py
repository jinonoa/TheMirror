from PIL import Image

def supprimer_exif(image, chemin_sortie):
    nouvelle_image = Image.new(image.mode, image.size)
    nouvelle_image.paste(image)
    nouvelle_image.save(chemin_sortie)
    return nouvelle_image