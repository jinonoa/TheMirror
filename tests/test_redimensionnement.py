from PIL import Image

from modules.redimensionnement import redimensionner


def test_redimension_image_grande():
    image = Image.new("RGB", (800, 400), "yellow")
    nouvelle_image = redimensionner(image)

    assert nouvelle_image.size == (500, 250)


def test_redimension_image_deja_petite():
    image = Image.new("RGB", (200, 100), "green")
    redimensionner(image)

    assert image.size == (200, 100)


def test_redimension_image_tres_large():
    image = Image.new("RGB", (1000, 200), "purple")
    redimensionner(image)

    assert image.size == (500, 100)


def test_redimension_image_tres_haute():
    image = Image.new("RGB", (200, 1000), "orange")
    redimensionner(image)

    assert image.size == (100, 500)
