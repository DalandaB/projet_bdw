from model.model_pg import random_grille
from model.model_pg import is_valid_cell


#on fait un formulaire post



if 'longueur' and 'hauteur' in POST:
    longueur = int(POST['longueur'][0])
    hauteur = int(POST['hauteur'][0])
    REQUEST_VARS['longueur'] = longueur
    REQUEST_VARS['hauteur'] = hauteur
    REQUEST_VARS['grille_aleatoire'] = random_grille(longueur,hauteur)













