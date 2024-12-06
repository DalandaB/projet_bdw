import psycopg
from psycopg import sql
from logzero import logger
import random


def execute_select_query(connexion, query, params=[]):
    """
    Méthode générique pour exécuter une requête SELECT (qui peut retourner plusieurs instances).
    Utilisée par des fonctions plus spécifiques.
    """
    with connexion.cursor() as cursor:
        try:
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result 
        except psycopg.Error as e:
            logger.error(e)
    return None

def execute_other_query(connexion, query, params=[]):
    """
    Méthode générique pour exécuter une requête INSERT, UPDATE, DELETE.
    Utilisée par des fonctions plus spécifiques.
    """
    with connexion.cursor() as cursor:
        try:
            cursor.execute(query, params)
            result = cursor.rowcount
            return result 
        except psycopg.Error as e:
            logger.error(e)
    return None

#nombre d’instances pour 3 tables de votre choix 
def count_instances(connexion, nom_table):
    """
    Retourne le nombre d'instances de la table nom_table
    String nom_table : nom de la table
    """
    query = sql.SQL('SELECT COUNT(*) AS nb FROM {table}').format(table=sql.Identifier(nom_table))
    return execute_select_query(connexion, query)

#top-5 des couleurs ayant le plus de briques 
def get_couleurs_briques(connexion,nombre):
    query = 'SELECT couleur FROM piece GROUP BY couleur ORDER BY COUNT(*) DESC  LIMIT %s'
    return execute_select_query(connexion,query,[nombre])
    #return execute_other_query(connexion, query, [nom_table])
     
# Pour chaque joueuse, son score minimal et son score maximal avec un JOIN
def get_scores_persos(connexion):
    select_part = 'SELECT t2.prenom_joueuse, MIN(t1.score_perso) AS score_minimal, MAX(t1.score_perso) AS score_maximal'
    from_part = 'FROM jouer t1 INNER JOIN joueuse t2 ON t1.id_joueuse = t2.id_joueuse GROUP BY t2.prenom_joueuse'
    query = f"{select_part} {from_part}"
    return execute_select_query(connexion, query)


#Parties avec le plus petit et plus grand nombre de pièces défaussées, de pièces piochées 
def stats_parties(connexion):
    select_1 = 'WITH stats AS (SELECT id_partie,COUNT(CASE WHEN piocher = true THEN 1 END) AS nb_pieces_piochées,COUNT(CASE WHEN piocher = false THEN 1 END) '
    select_2 = 'AS nb_pieces_defaussées FROM tour GROUP BY id_partie),min_max AS (SELECT MIN(nb_pieces_piochées) AS min_piochées,MAX(nb_pieces_piochées) AS max_piochées,'
    select_3 = 'MIN(nb_pieces_defaussées) AS min_defaussées,MAX(nb_pieces_defaussées) AS max_defaussées FROM stats) SELECT s.id_partie,s.nb_pieces_piochées'
    select_4 = ',s.nb_pieces_defaussées FROM stats s JOIN min_max m ON s.nb_pieces_piochées = m.min_piochées'
    select_5 = ' OR s.nb_pieces_piochées = m.max_piochées OR s.nb_pieces_defaussées = m.min_defaussées OR s.nb_pieces_defaussées = m.max_defaussées;'
    query = f" {select_1} {select_2} {select_3} {select_4} {select_5}"
    return execute_select_query(connexion, query)
    
def get_nb_tours(connexion):
    select_1 = 'SELECT TO_CHAR(j.date_inscrip_joueuse, \'MM-YYYY\') AS mois_annee,AVG(t.numero_tour) AS nombre_moyen_tours FROM tour t'
    select_2 = 'JOIN joueuse j ON t.id_joueuse = j.id_joueuse GROUP BY TO_CHAR(j.date_inscrip_joueuse, \'MM-YYYY\');'
    query = f"{select_1} {select_2}"
    return execute_select_query(connexion, query)

def get_top3_parties(connexion):
    select_1 = 'SELECT t.id_partie,COUNT(*) AS nombre_pieces_utilisees,MAX(p.longueur * p.largeur) AS plus_grande_piece FROM tour t'
    select_2 = 'JOIN piece p ON t.id = p.id GROUP BY t.id_partie ORDER BY nombre_pieces_utilisees DESC LIMIT 3;'
    query = f"{select_1} {select_2}"
    return execute_select_query(connexion, query)
     
     
def get_4_random_pieces(connexion):
    query = 'SELECT * FROM piece WHERE longueur <= 2 OR largeur <= 2 ORDER BY RANDOM() LIMIT 4;'
    return execute_select_query(connexion,query)

def get_existing_piece(connexion,id_piece):
    query = 'SELECT * FROM piece where id = %s'
    return execute_select_query(connexion, query, [id_piece])

    
    #content
    column +=4
 

 
def grille():
    grid = []
    for row in range(8):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(9):
            grid[row].append(0)  # Append a cell
    #J'avais confondu == avec =
    for row in range(1,7):
        if row == 1 or row == 6:
            for column in range(1,8,4):
                grid[row][column] = 1
                grid[row][column + 1] = 1
                #grid[row][column+1] = 1
        else:
            for column in range (1,8,2): 
                grid[row][column] = 1

    grid[3][2] = 1 
    grid[4][2] = 1 
    # Vérifiez les dimensions de la grille
    assert len(grid) == 8 and all(len(row) == 9 for row in grid), "Grille incorrecte"
    return grid


#on crée la fonctionnalité pour la grille aléatoire   
#longueur_grille = 9
#hauteur_grille = 8


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

 
 
    
 
     
"""
def grille(connexion):
    grid = []
    for row in range(8):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
    for column in range(9):
        grid[row].append(0)  # Append a cell


    #J'avais confondu == avec =
    for row in range(1,7):
        if row == 1 or row == 6:
            
            column = 1
            while column < 9 :
                if column+2 < 9:
                    grid[row][column] = 1
                if column + 1 < 9:
                    grid[row][column + 1] = 1
                #grid[row][column+1] = 1
                column += 4
        else:
            for column in range (1,8,2): 
                grid[row][column] = 1

    grid[3][2] = 1 
    grid[4][2] = 1 
    # Vérifiez les dimensions de la grille
    assert len(grid) == 8 and all(len(row) == 9 for row in grid), "Grille incorrecte"
    return grid

 
 
 """
    
        
        
        
     
        
     
        


     
        
        
        
        
     
        

 
    
    
    
 
    
 
    
 
     
    
    
    
 
     

















