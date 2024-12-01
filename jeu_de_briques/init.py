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

    piece :{{ id_piece[0] }},longueur :{{ id_piece[1] }},largeur :{{ id_piece[2] }},couleur :{{ id_piece[4] }}

{% if POST['piece_id'] != 0 %}
<p>id : {REQUEST_VARS['infos_pieces'][0]}, longueur:{REQUEST_VARS['infos_pieces'][1]}, largeur:{REQUEST_VARS['infos_pieces'][2]}, couleur:{REQUEST_VARS['infos_pieces'][4]}</p>
{%endif%}
"""