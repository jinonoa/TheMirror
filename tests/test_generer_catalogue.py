import json

import pytest

from modules.catalogue import generer_catalogue


def test_fichier_json_cree(tmp_path):
    dossier_catalogue = tmp_path / "catalogue"
    dossier_catalogue.mkdir()

    image = dossier_catalogue / "coiffure_1.png"
    image.touch()

    chemin_json = tmp_path / "catalogue.json"

    generer_catalogue(dossier_catalogue, chemin_json)

    assert chemin_json.is_file()


def test_contenu_catalogue_correct(tmp_path):
    dossier_catalogue = tmp_path / "catalogue"
    dossier_catalogue.mkdir()

    image = dossier_catalogue / "coiffure_1.png"
    image.touch()

    chemin_json = tmp_path / "catalogue.json"

    generer_catalogue(dossier_catalogue, chemin_json)

    with open(chemin_json, encoding="utf-8") as fichier:
        catalogue = json.load(fichier)

    assert len(catalogue) == 1
    assert catalogue[0]["nom"] == "coiffure_1"
    assert catalogue[0]["chemin"] == str(image)


def test_fichiers_non_autorises_ignores(tmp_path):
    dossier_catalogue = tmp_path / "catalogue"
    dossier_catalogue.mkdir()

    (dossier_catalogue / "coiffure_1.png").touch()
    (dossier_catalogue / "coiffure_2.jpeg").touch()
    (dossier_catalogue / "notes.txt").touch()

    chemin_json = tmp_path / "catalogue.json"

    generer_catalogue(dossier_catalogue, chemin_json)

    with open(chemin_json, encoding="utf-8") as fichier:
        catalogue = json.load(fichier)

    assert len(catalogue) == 2
    assert {entree["nom"] for entree in catalogue} == {
        "coiffure_1",
        "coiffure_2",
    }

    def test_sous_dossier_ignore(tmp_path):
        dossier_catalogue = tmp_path / "catalogue"
        dossier_catalogue.mkdir()

        (dossier_catalogue / "coiffure_1.png").touch()
        (dossier_catalogue / "ancien_catalogue").mkdir()

        chemin_json = tmp_path / "catalogue.json"

        generer_catalogue(dossier_catalogue, chemin_json)

        with open(chemin_json, encoding="utf-8") as fichier:
            catalogue = json.load(fichier)

        assert len(catalogue) == 1
        assert catalogue[0]["nom"] == "coiffure_1"

    def test_catalogue_vide(tmp_path):
        dossier_catalogue = tmp_path / "catalogue"
        dossier_catalogue.mkdir()

        chemin_json = tmp_path / "catalogue.json"

        generer_catalogue(dossier_catalogue, chemin_json)

        with open(chemin_json, encoding="utf-8") as fichier:
            catalogue = json.load(fichier)

        assert catalogue == []

    def test_dossier_inexistant(tmp_path):
        dossier_catalogue = tmp_path / "dossier_inexistant"
        chemin_json = tmp_path / "catalogue.json"

        with pytest.raises(FileNotFoundError):
            generer_catalogue(dossier_catalogue, chemin_json)
