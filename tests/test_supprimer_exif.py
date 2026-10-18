from PIL import Image
from modules.exif import supprimer_exif

def test_fichier_enregistre(tmp_path):
    image = Image.new("RGB", (200, 200), "brown")
    chemin_fichier_enregistre = tmp_path/"image_enregistre.png"
    image_enregistree = supprimer_exif(image, chemin_fichier_enregistre)
    assert chemin_fichier_enregistre.is_file()

def test_dimension_fichier_enregistre(tmp_path):
    image = Image.new("RGB", (200, 150), "brown")
    chemin_dimension_fichier = tmp_path/"image_test.jpg"

    image_enregistree = supprimer_exif(image, chemin_dimension_fichier)
    with Image.open(chemin_dimension_fichier) as image_fichier:
        assert image_fichier.size == (200, 150)

def test_supprimer_exif(tmp_path):
    image = Image.new("RGB", (200, 150), "black")
    exif = image.getexif()
    exif[270] = "Photo de test"
    chemin_source = tmp_path / "image_avec_exif.jpg"
    image.save(chemin_source, exif=exif)

    with Image.open(chemin_source) as image_source:
        assert image_source.getexif().get(270) == "Photo de test"

        chemin_sortie = tmp_path / "image_sans_exif.jpg"
        supprimer_exif(image_source, chemin_sortie)

    with Image.open(chemin_sortie) as image_resultat:
        assert 270 not in image_resultat.getexif()