from PIL import Image, ImageDraw
from modules.models import DetectionResult
from modules.recadrage import recadrer


def test_recadrer_dimensions_correctes():
    image = Image.new("RGB", (200, 200), "white")
    coordonnees = DetectionResult(
        x=100,
        y=50,
        largeur=80,
        hauteur=120
    )

    resultat = recadrer(image, coordonnees)

    assert resultat.size == (80, 120)

def test_recadrer_dimensions_limites():
    image = Image.new("RGB", (200, 200), "blue")
    coordonnees = DetectionResult(x=170, y=150, largeur=60, hauteur=70)

    resultat = recadrer(image, coordonnees)

    assert resultat.size == (30, 50)

def test_recadrer_zone_correct():
    image = Image.new("RGB", (200, 200), "red")

    draw = ImageDraw.Draw(image)
    draw.rectangle([100, 0, 199, 199], fill = "blue")

    coordonnees = DetectionResult(
        x = 100,
        y = 0,
        largeur = 100,
        hauteur = 200
    )

    zone = recadrer(image, coordonnees)
    assert zone.size == (100, 200)
    assert zone.getpixel((50, 100)) == (0, 0, 255)



