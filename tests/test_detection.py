from functools import partial
from types import SimpleNamespace

from PIL import Image

import modules.detection as detection
from modules.detection import detecter_visage
from modules.models import DetectionResult


class FauxDetecteur:
    def __init__(self, visage_detecte):
        self.visage_detecte = visage_detecte

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def detect(self, image):
        if self.visage_detecte:
            coordonnees = DetectionResult(100, 50, 80, 120)
            boite = SimpleNamespace(
                origin_x=coordonnees.x,
                origin_y=coordonnees.y,
                width=coordonnees.largeur,
                height=coordonnees.hauteur,
            )
            detection = SimpleNamespace(bounding_box=boite)
            resultat = SimpleNamespace(detections=[detection])
            return resultat
        else:
            resultat = SimpleNamespace(detections=[])
            return resultat


def creer_faux_detecteur(model_path, visage_detecte):
    return FauxDetecteur(visage_detecte)


creer_detecteur_avec_visage = partial(creer_faux_detecteur, visage_detecte=True)

creer_detecteur_sans_visage = partial(creer_faux_detecteur, visage_detecte=False)


def test_detecter_visage_avec_visage_detecte(monkeypatch):
    monkeypatch.setattr(
        detection.mp.tasks.vision.FaceDetector,
        "create_from_model_path",
        creer_detecteur_avec_visage,
    )

    image = Image.new("RGB", (200, 200), "white")
    resultat = detecter_visage(image)

    assert resultat.x == 100
    assert resultat.y == 50
    assert resultat.largeur == 80
    assert resultat.hauteur == 120
    assert isinstance(resultat, DetectionResult)


def test_detecter_visage_sans_visage_detecte(monkeypatch):
    monkeypatch.setattr(
        detection.mp.tasks.vision.FaceDetector,
        "create_from_model_path",
        creer_detecteur_sans_visage,
    )

    image = Image.new("RGB", (200, 200), "white")

    resultat = detecter_visage(image)

    assert resultat is None
