from model.model_pg import get_4_random_pieces
from model.model_pg import get_existing_piece



REQUEST_VARS['random_pieces'] = get_4_random_pieces(SESSION['CONNEXION'])

#modification de ce code

if POST or 'piece_id' in POST:  # Vérifie si le formulaire a été soumis 
    try:
        # Récupère l'id correspondant de la piece choisie
        id_piece = POST['piece_id'][0][0] #
        piece_existante = get_existing_piece(SESSION['CONNEXION'],id_piece)
        REQUEST_VARS['infos_pieces'] = get_existing_piece(SESSION['CONNEXION'],id_piece)

        #REQUEST_VARS['infos_piece'] = piece_existante


        
        if piece_existante :
            REQUEST_VARS['message'] = "id : {piece_existante[0]}, longueur:{piece_existante[1]}, largeur:{piece_existante[2]}, couleur:{piece_existante[4]}"
            #REQUEST_VARS['message'] = "Vous êtes un bon joueur"
            REQUEST_VARS['message_class'] = "alert-success"
            

          
    
        
    except Exception as e:
        # Gestion des erreurs et affichage d'un message clair
        REQUEST_VARS['message'] = "Une erreur inattendue est survenue lors du choix de la pièce. Veuillez réessayer."
        REQUEST_VARS['message_class'] = "alert-error"