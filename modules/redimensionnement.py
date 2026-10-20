from PIL import Image


def redimensionner(image: Image.Image) -> Image.Image:
    image.thumbnail((500, 500))
    return image
