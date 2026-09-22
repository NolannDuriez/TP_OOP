"""Exercice 3: De la fonction à la classe Habitant"""

from abc import ABC, abstractmethod

class Habitant(ABC):
    """Classe représentant un habitant avec un nom, un âge, une adresse 
    et un dictionnaire d'animaux."""
    def __init__(self, nom, age, adresse, animaux=None):
        """Initialise un nouvel habitant avec les informations fournies."""
        self.__nom = nom
        self.__age = age
        self.__adresse = adresse
        self.__animaux = animaux if animaux is not None else {}

    def __str__(self):
        """Retourne une représentation en chaîne de caractères de l'habitant."""
        return f"{self.__prenom} {self.__nom}, {self.__age} ans, habite a {self.__adresse}"

    @abstractmethod
    def calcul_nombre_annee_avant_retraite(self):
        """Méthode abstraite pour calculer le nombre d'années avant la retraite."""
        pass

    def affichage_adresse(self):
        """Affiche l'adresse de l'habitant.donné"""
        print(f"{self.__nom} habite a {self.__adresse}")

    def compte_animal(self, animal):
        """Compte le nombre d'animeaux de l'espèce renseignée de l'habitant donné"""
        return self.__animaux.get(animal, 0)


    def get_nom(self):
        """Retourne le nom de l'habitant."""
        return self.__nom

    @property
    def age(self):
        """Retourne l'âge de l'habitant."""
        return self.__age

    def get_adresse(self):
        """Retourne l'adresse de l'habitant."""
        return self.__adresse

    def get_animaux(self):
        """Retourne le dictionnaire d'animaux de l'habitant."""
        return self.__animaux



    def set_nom(self, nom):
        """Modifie le nom de l'habitant."""
        self.__nom = nom

    @age.setter
    def age(self, age):
        """Modifie l'âge de l'habitant mais valide la valeur avant de l'affecter."""
        if age < 0:
            raise ValueError("L'âge doit être un nombre positif.")
        self.__age = age

    def set_adresse(self, adresse):
        """Modifie l'adresse de l'habitant."""
        self.__adresse = adresse

    def set_animaux(self, animaux):
        """Modifie le dictionnaire d'animaux de l'habitant."""
        self.__animaux = animaux

#h1 = Habitant("Alice", 25, "Rue A", {"chiens": 2, "chats": 1})

#h1.age = 26
#assert h1.age == 26

#h2 = Habitant("Bob", 30, "Rue B", {"chiens": 1})
#try:
#    h2.age = -5
#    assert False, "une ValueError aurait du etre levee"
#except ValueError:
#    pass
