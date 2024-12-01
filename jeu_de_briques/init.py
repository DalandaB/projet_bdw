"""
Ficher initialisation (eg, constantes chargées au démarrage dans la session)
"""

from datetime import datetime
from os import path
 

SESSION['APP'] = "Jeu de Briques" #Serial Critique
SESSION['BASELINE'] = "Jouez à votre jeu préféré tout de suite !"
SESSION['DIR_HISTORIQUE'] = path.join(SESSION['DIRECTORY'], "historiques")
SESSION['HISTORIQUE'] = dict()
SESSION['CURRENT_YEAR'] = datetime.now().year




"""

[[routes]]
url = "grille_pygame"
controleur = "controleurs/grille_pygame.py"
template = "grille_pygame.html"

"""