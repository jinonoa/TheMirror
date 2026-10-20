from PIL import Image


def supprimer_exif(image: Image.Image, chemin_sortie: str) -> Image.Image:
    nouvelle_image = Image.new(image.mode, image.size)
    nouvelle_image.paste(image)
    nouvelle_image.save(chemin_sortie)
    return nouvelle_image
