import psycopg
from psycopg import sql
from logzero import logger
from jinja2 import Environment, FileSystemLoader
import os


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
     
     
    
 
    
 
    
 
    

    
 
    
 
     
 
    
        
        
        
     
        
     
        


     
        
        
        
        
     
        

 
    
    
    
 
    
 
    
 
     
    
    
    
 
     















#model de brouillon

def get_instances(connexion, nom_table):
    """
    Retourne les instances de la table nom_table
    String nom_table : nom de la table
    """
    query = sql.SQL('SELECT * FROM {table}').format(table=sql.Identifier(nom_table), )
    return execute_select_query(connexion, query)



def get_episodes_for_num(connexion, numero):
    """
    Retourne le titre des épisodes numérotés numero
    Integer numero : numéro des épisodes
    """
    query = 'SELECT titre FROM episodes where numéro=%s'
    return execute_select_query(connexion, query, [numero])

def get_serie_by_name(connexion, nom_serie):
    """
    Retourne les informations sur la série nom_serie (utilisé pour vérifier qu'une série existe)
    String nom_serie : nom de la série
    """
    query = 'SELECT * FROM series where nomsérie=%s'
    return execute_select_query(connexion, query, [nom_serie])

def insert_serie(connexion, nom_serie):
    """
    Insère une nouvelle série dans la BD
    String nom_serie : nom de la série
    Retourne le nombre de tuples insérés, ou None
    """
    query = 'INSERT INTO series VALUES(%s)'
    return execute_other_query(connexion, query, [nom_serie])


#fonction officielle de test, si elle marche je supprimerai toutes les autres fonctions encombrantes
def insert_new_critique(connexion, nomserie, texte, pseudo):
    """
    Insère une nouvelle critique dans la base de données.
    :param connexion: Connection à la base de données
    :param nomserie: Nom de la série associée à la critique
    :param texte: Texte de la critique
    :param pseudo: Pseudo de l'utilisateur
    :return: True si réussi, False sinon
    """
    # Récupère le nouvel idcritique
    query_id = "SELECT MAX(idcritique) FROM critiques"
    result = execute_select_query(connexion, query_id)
    new_idcritique = (result[0][0] + 1) if result and result[0][0] is not None else 1
       # new_idcritique = (result[0][0] + 1) if result and result[0][0] is not None else 1


    # Prépare la requête d'insertion
    query_insert = "INSERT INTO critiques VALUES (%s, NOW(), %s, %s, %s)"

        
    
    # Exécute la requête avec les paramètres
    return execute_select_query(connexion, query_insert, [new_idcritique, pseudo, texte, nomserie])
    #    return execute_other_query(connexion, query_insert, [new_idcritique, pseudo, texte, nomserie])
    """
    query_insert = 
        INSERT INTO critiques (idcritique, datecritique, pseudo, texte, nomserie)
        VALUES (%s, NOW(), %s, %s, %s)
    """

    

def get_table_like(connexion, nom_table, like_pattern):
    """
    Retourne les instances de la table nom_table dont le nom correspond au motif like_pattern
    String nom_table : nom de la table
    String like_pattern : motif pour une requête LIKE
    """
    motif = '%' + like_pattern + '%'
    nom_att = 'nomsérie'  # nom attribut dans séries (à éviter)
    if nom_table == 'actrices':  # à éviter
        nom_att = 'nom'  # nom attribut dans actrices (à éviter)
    query = sql.SQL("SELECT * FROM {} WHERE {} ILIKE {}").format(
        sql.Identifier(nom_table),
        sql.Identifier(nom_att),
        sql.Placeholder())
    #    like_pattern=sql.Placeholder(name=like_pattern))
    return execute_select_query(connexion, query, [motif])




#c'est ici que commence la fonctionnalité

#pas de grosses contraintes pour le moment, la personne devra elle même insérer son pseudo, le texte et le nom du film correspondant



