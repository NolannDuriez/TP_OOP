"""Exercice 5: nventaire de pièces détachées avec des dictionnaires"""


pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}

def quantite_piece(stock, modele, piece):
    """Retourne la quantité disponible d’une pièce 
    pour un modèle donné"""
    return stock[modele][piece]

assert quantite_piece(pieces_stock, "ModeleA", "moteurs") == 10


def consommer_piece(stock, modele, piece, nb_pieces_consommees):
    """Retourne le stock sans les pièces consommées"""
    stock[modele][piece] -= nb_pieces_consommees
    return stock

consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
assert pieces_stock["ModeleA"]["moteurs"] == 7

def ajouter_modele(stock, nouveau_modele, moteurs, capteurs, roues):
    """Retourne le stock avec un nouveau modèle et ses pièces enregistrés"""
    stock[nouveau_modele] = {"moteurs": moteurs, "capteurs": capteurs, "roues": roues}
    return stock

ajouter_modele(pieces_stock, "ModeleC", moteurs=4, capteurs=10, roues=16)
assert pieces_stock["ModeleC"] == \
    {"moteurs": 4, "capteurs": 10, "roues": 16}

def total_pieces(stock):
    """Retourne la quantité totale de chaque pièce, modeles confondus"""
    total_moteurs = 0
    total_capteurs = 0
    total_roues = 0
    for modele in stock:
        total_moteurs += stock[modele]["moteurs"]
        total_capteurs += stock[modele]["capteurs"]
        total_roues += stock[modele]["roues"]
    quantites = {"moteurs": total_moteurs, "capteurs": total_capteurs, "roues": total_roues}
    return quantites

totaux = total_pieces(pieces_stock)
assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}
