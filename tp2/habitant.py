"""Exercice 3: De la fonction à la classe Habitant"""

class Habitant:
    """Classe représentant un habitant avec un nom, un âge, une adresse 
    et un dictionnaire d'animaux."""
    def __init__(self, nom, age, adresse, animaux=None):
        """Initialise un nouvel habitant avec les informations fournies."""
        self.nom = nom
        self.age = age
        self.adresse = adresse
        self.animaux = animaux if animaux is not None else {}

    def affichage_adresse(self):
        """Affiche l'adresse de l'habitant.donné"""
        print(f"{self.nom} habite a {self.adresse}")

    def compte_animal(self, animal):
        """Compte le nombre d'animeaux de l'espèce renseignée de l'habitant donné"""
        return self.animaux.get(animal, 0)


h1 = Habitant("Aldric", 25, "Rue A", {"vaches": 3})

assert h1.nom == "Aldric"
assert h1.compte_animal("vaches") == 3
assert h1.compte_animal("moutons") == 0

h1.affichage_adresse() # affiche "Aldric habite a Rue A"
