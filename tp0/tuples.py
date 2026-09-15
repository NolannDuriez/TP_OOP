"""Exercice 3: Journal de bord d’un robot avec des tuples"""


releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]

def afficher_releve(releve):
    """retourne une chaîne de caractères décrivant un relevé"""
    nom_capteur, valeur, unite = releve
    return f"Capteur {nom_capteur} : {valeur} {unite}"

assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"


def recalibrer(liste_releves, nom_capteur, nouvelle_valeur):
    """reconstruit la liste des relevés avec la nouvelle valeur pour le capteur concerné, 
    et laisse les autres relevés inchangés"""
    nouvelle_liste_releves = liste_releves
    for i in range(len(liste_releves)):
        if nouvelle_liste_releves[i][0] == nom_capteur:
            nouveau_releve = (nom_capteur, nouvelle_valeur, nouveaux_releves[i][2])
            nouvelle_liste_releves[i] = nouveau_releve
    return nouvelle_liste_releves

nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)
assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3
