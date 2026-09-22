"""Exercice 5: Composition et agrégation : la classe Village"""

class Habitant:
    """Classe représentant un habitant avec un nom, un âge, une adresse 
    et un dictionnaire d'animaux."""
    def __init__(self, nom, age, adresse, animaux=None):
        """Initialise un nouvel habitant avec les informations fournies."""
        self.nom = nom
        self.age = age
        self.adresse = adresse
        self.animaux = animaux if animaux is not None else {}

class Village:
    """Classe représentant un village avec un nom et une liste d'habitants."""
    def __init__(self, nom):
        """Initialise un nouveau village avec le nom fourni."""
        self.nom = nom
        self.habitants = []

    def get_habitants(self):
        """Retourne la liste des habitants du village."""
        return self.habitants

    def ajouter_habitant_composition(self, nom, age, adresse, animaux=None):
        """Ajoute un nouvel habitant au village en utilisant la composition."""
        nouvel_habitant = Habitant(nom, age, adresse, animaux)
        self.habitants.append(nouvel_habitant)

    def ajouter_habitant_agregation(self, habitant):
        """Ajoute un nouvel habitant au village en utilisant l'agrégation."""
        self.habitants.append(habitant)

    def afficher_habitants(self):
        for habitant in self.habitants:
            print(f"{habitant.nom} ")


pytown = Village("PyTown")
pytown.ajouter_habitant_composition("Aldric", 25, "Rue A", {"vaches": 3})

elise = Habitant("Elise", 28, "Rue B", {"poules": 10})
pytown.ajouter_habitant_agregation(elise)

autre_village = Village("VillageVoisin")
autre_village.ajouter_habitant_agregation(elise) # meme habitant dans 2 villages

assert len(pytown.get_habitants()) == 2
assert elise in autre_village.get_habitants()
