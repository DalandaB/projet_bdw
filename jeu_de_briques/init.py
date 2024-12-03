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

    {% for instance in REQUEST_VARS['infos_pieces'] %}
        <p>id : {instance[0]}, longueur:{instance[1]}, largeur:{instance[2]}, couleur:{instance[4]}</p>
    {%endfor%}


    
    .container{
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
        grid-template-rows:  1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
        grid-gap: 1px;
    }

    .black{
        background : black;
        height: 50px;
    }

    #special {
        background-color: green; /* Couleur spécifique */
      }

    .cell {
width: 50px;
height: 50px;
border: 1px solid black;
}

.container {
display: grid;
grid-template-columns: repeat(9, 1fr);
gap: 1px;
}



.container {
display: grid;
grid-template-columns: repeat(9, 1fr);
}

.green {
background-color: green;
}

.black{
    background : black;
    height: 50px;
    width: 50px;
}
"""