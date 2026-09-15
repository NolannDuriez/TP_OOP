"""Exercice 4: Coordination d’une flotte de robots avec des ensembles"""


robots_exploration = {"R2", "R5", "R7"}
robots_transport = {"R5", "R9", "R7", "R3"}


def robots_double_mission(robots_explo, robots_transpo):
    """Renvoie l'ensemble des robots participant aux deux missions"""
    return robots_explo & robots_transpo

def robots_toutes_missions(robots_explo, robots_transpo):
    """Renvoie l'ensemble des robots participant à au moins une mission"""
    return robots_explo | robots_transpo

def robots_exploration_seulement(robots_explo, robots_transpo):
    """Renvoie l'ensemble des robots participant seulement à la mission exploration"""
    return robots_explo - robots_transpo


double_mission = robots_double_mission(robots_exploration, robots_transport)
toutes_missions = robots_toutes_missions(robots_exploration, robots_transport)
exploration_seule = robots_exploration_seulement(robots_exploration, robots_transport)

assert double_mission == {"R5", "R7"}
assert toutes_missions == {"R2", "R3", "R5", "R7", "R9"}
assert exploration_seule == {"R2"}


def ajouter_robot_mission(ensemble_robots, nouveau_robot):
    """Renvoie un nouvel ensemble de robots avec un robot rajouté"""
    nouvel_ensemble = ensemble_robots.copy()
    nouvel_ensemble.add(nouveau_robot)
    return nouvel_ensemble

def retirer_robot_mission(ensemble_robots, robot_panne):
    """Renvoie un nouvel ensemble de robots avec un robot retiré"""
    nouvel_ensemble = ensemble_robots.copy()
    nouvel_ensemble.remove(robot_panne)
    return nouvel_ensemble

ajout = ajouter_robot_mission(robots_exploration, "R8")
retrait = retirer_robot_mission(robots_transport, "R9")
assert ajout == {"R2", "R5", "R7", "R8"}
assert retrait == {"R3", "R5", "R7"}
# L’ensemble d’origine ne doit pas avoir été modifié
assert robots_transport == {"R5", "R9", "R7", "R3"}
