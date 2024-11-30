from model.model_pg import count_instances
from model.model_pg import get_couleurs_briques
from model.model_pg import get_scores_persos
from model.model_pg import stats_parties
from model.model_pg import get_nb_tours
from model.model_pg import get_top3_parties





REQUEST_VARS['nb_instances_1'] = count_instances(SESSION['CONNEXION'],'joueuse')
#toujours garder les noms de tableaux en minuscule
REQUEST_VARS['nb_instances_2'] = count_instances(SESSION['CONNEXION'],'piece')
REQUEST_VARS['nb_instances_3'] = count_instances(SESSION['CONNEXION'],'construction')


REQUEST_VARS['top_5'] = get_couleurs_briques(SESSION['CONNEXION'],5)

REQUEST_VARS['infos_joueuses'] = get_scores_persos(SESSION['CONNEXION'])

REQUEST_VARS['parties'] = stats_parties(SESSION['CONNEXION'])

REQUEST_VARS['nb_tours'] = get_nb_tours(SESSION['CONNEXION'])

REQUEST_VARS['top_3'] = get_top3_parties(SESSION['CONNEXION'])







