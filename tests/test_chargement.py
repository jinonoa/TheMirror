from PIL import Image

from modules.chargement import ouvrir_image


def test_ouvrir_image_jpeg_valide(tmp_path):
    image = Image.new("RGB", (100, 100), "white")
    chemin_image = tmp_path / "test.jpg"
    image.save(chemin_image)

    resultat = ouvrir_image(str(chemin_image))

    assert isinstance(resultat, Image.Image)


def test_ouvrir_image_png_valide(tmp_path):
    image = Image.new("RGB", (100, 100), "white")
    chemin_image = tmp_path / "test.png"
    image.save(chemin_image)

    resultat = ouvrir_image(str(chemin_image))

    assert isinstance(resultat, Image.Image)


def test_ouvrir_image_fichier_inexistant(tmp_path):
    chemin_inexistant = tmp_path / "inconnu.jpg"
    resultat = ouvrir_image(str(chemin_inexistant))

    assert resultat == "Le fichier est inexistant"


def test_ouvrir_image_format_non_autorisee(tmp_path):
    image = Image.new("RGB", (100, 100), "blue")
    chemin_gif = tmp_path / "test.gif"
    image.save(chemin_gif)

    resultat = ouvrir_image(str(chemin_gif))

    assert resultat == "Format non autorisé"


def test_ouvrir_image_corrompu(tmp_path):
    chemin_image_corrompue = tmp_path / "image_corrompu.jpg"
    chemin_image_corrompue.write_text("Ceci est une image corrompue")

    resultat = ouvrir_image(str(chemin_image_corrompue))

    assert resultat == "Le fichier n'est pas une image ou est corrompu"
