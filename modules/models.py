from dataclasses import dataclass

@dataclass
class DetectionResult:
    x: int
    y: int
    largeur: int
    hauteur: int

@dataclass
class Coiffure:
    nom: str
    chemin: str