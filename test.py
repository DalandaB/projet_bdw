import random

def is_valid_cell(row,column,hauteur_grille,longueur_grille,grid):
    return 0<=row<hauteur_grille and 0<=column<longueur_grille and grid[row][column]==0


def random_grille(longueur_grille,hauteur_grille):
    nb_total_cases = longueur_grille*hauteur_grille
    min_cases_cibles = int((nb_total_cases*10)/100)
    max_cases_cibles = int((nb_total_cases*20)/100)
    nb_cases_cibles = random.randint(min_cases_cibles,max_cases_cibles)
    #initialiser une grille avec uniquement des cases vides
    #pour les cases cibles on mettre 2.
    grid = []
    for row in range(hauteur_grille):
        grid.append([])
        for column in range(longueur_grille):
            grid[row].append(0)  
    #sélectionner aléatoirement une première case cible
    init_row = random.randint(0, hauteur_grille-1)  
    init_column = random.randint(0, longueur_grille-1)  
    grid[init_row][init_column] = 2
    nb_cases_cibles -= 1

    for i in range(nb_cases_cibles):
        #choisir une direction aléatoire
        #alea_row = random.randint(init_row-1,init_row+1)
        #alea_column = random.randint(init_column-1,init_column+1)
        #alea_row,alea_column = -1 en faite c'est déconseillé de faire ce genre de décla de variables
        alea_row = -1
        alea_column = -1
        while not is_valid_cell(alea_row,alea_column,hauteur_grille,longueur_grille,grid):
            alea_row = random.randint(init_row-1,init_row+1)
            alea_column = random.randint(init_column-1,init_column+1)
        if is_valid_cell(alea_row,alea_column,hauteur_grille,longueur_grille,grid):
            grid[alea_row][alea_column]=2
            init_row = alea_row
            init_column = alea_column
            #else:
                #alea_row = random.randint(init_row-1,init_row+1)
                #alea_column = random.randint(init_column-1,init_column+1)
                #continue
    return grid




random_grille(9,8)







