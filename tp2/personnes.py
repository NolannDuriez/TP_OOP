"""Exercice 7: Héritage : Adulte et Enfant"""

from multipledispatch import dispatch
from habitant import Habitant


class Adulte(Habitant):
    """Classe représentant un adulte, héritant de la classe Habitant."""

    @dispatch(str, int, str)
    def __init__(self, nom, age, adresse):
        """Initialise un nouvel adulte avec les informations fournies si elles sont cohérentes."""
        if age < 18:
            raise ValueError("Un adulte doit avoir au moins 18 ans.")
        super().__init__(nom, age, adresse)

    @dispatch(str, str, int, str)
    def __init__(self, nom, prenom, age, adresse):
        """Initialise un nouvel adulte avec les informations fournies si elles sont cohérentes."""
        if age < 18:
            raise ValueError("Un adulte doit avoir au moins 18 ans.")
        super().__init__(nom, age, adresse)
        self.prenom = prenom

    def calcul_nombre_annee_avant_retraite(self):
        """Calcule le nombre d'années avant la retraite pour un adulte."""
        age_retraite = 62
        if self.age >= age_retraite:
            return "Déjà à la retraite"
        return age_retraite - self.age


class Enfant(Habitant):
    """Classe représentant un enfant, héritant de la classe Habitant."""

    @dispatch(str, int, str)
    def __init__(self, nom, age, adresse):
        """Initialise un nouvel enfant avec les informations fournies si elles sont cohérentes."""
        if age >= 18:
            raise ValueError("Un enfant doit avoir moins de 18 ans.")
        super().__init__(nom, age, adresse)

    @dispatch(str, str, int, str)
    def __init__(self, nom, prenom, age, adresse):
        """Initialise un nouvel enfant avec les informations fournies si elles sont cohérentes."""
        if age >= 18:
            raise ValueError("Un enfant doit avoir moins de 18 ans.")
        super().__init__(nom, age, adresse)
        self.prenom = prenom

    def calcul_nombre_annee_avant_retraite(self):
        """Calcule le nombre d'années avant la retraite pour un enfant."""
        return "Erreur : un enfant ne peut pas calculer sa retraite"

# Adulte : leve une ValueError si age < 18
# calcul_nombre_annee_avant_retraite() renvoie :
# - "Deja a la retraite" si age >= 62
# - 62 - age sinon
# Enfant : leve une ValueError si age >= 18
# calcul_nombre_annee_avant_retraite() renvoie toujours :
# - "Erreur: un enfant ne peut pas calculer sa retraite"

if __name__ == "__main__":

    adulte = Adulte("Dupont", "Marie", 35, "Rue A")
    enfant = Enfant("Martin", "Lucas", 12, "Rue B")

    assert isinstance(adulte, Habitant)
    assert adulte.calcul_nombre_annee_avant_retraite() == 27
    assert "enfant" in enfant.calcul_nombre_annee_avant_retraite()

    try:
        Enfant("Oups", 25, "Rue C")
        assert False, "une ValueError aurait du etre levee"
    except ValueError:
        pass
