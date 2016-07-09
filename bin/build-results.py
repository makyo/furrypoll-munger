import csv
import logging
import sys

from results import results2009
from results import results2010
from results import results2011
from results import results2012
from results import results2013
from results import results2015
from results import results2016

def main(out_dir):
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # The fieldnames used for the CSV DictWriter
    fieldnames = [
        'year',
        'furry_status',
        'birthdate',
        'biosex',
        'gender',
        'orientation',
        'country',
        'state',
        'race_white',
        'race_black',
        'race_hispanic',
        'race_asian',
        'race_native',
        'religion',
        'politics_social',
        'politics_economic',
        'occupation',
        'education',
        'relationship',
        'partner_is_furry',
        'polyamorous_romantic',
        'polyamorous_sexual',
        'howfurry',
        'years_known_fandom',
        'years_as_furry',
        'furries_known',
        'furries_known_in_person',
        'whoknows_nobody',
        'whoknows_family',
        'whoknows_SO',
        'whoknows_furryfriends',
        'whoknows_bestfriends',
        'whoknows_closerfriends',
        'whoknows_friends',
        'whoknows_coworkers',
        'whoknows_commonknowledge',
        'nonfurry_response',
        'nonfurry_response_personal',
        'nonfurry_accuracy',
        'rp_as_different_gender',
        'seximportance_overall',
        'seximportance_personal',
        'seximportance_others',
        'seximportance_public',
        'howoften_chat_online',
        'howoften_roleplay',
        'howoften_attend_conventions',
        'howoften_meet_up',
        'howoften_visit_furry_websites',
        'howoften_participate_in_furry_online_communities',
        'howoften_write',
        'howoften_draw',
        'howoften_play_nonfurry_online_games',
        'howoften_play_nonfurry_rpgs',
        'howoften_attend_nonfurry_conventions',
        'howoften_participate_in_nonfurry_online_communities',
        'is_artist',
        'is_writer',
        'is_musician',
        'is_congoer',
        'is_fursuiter',
        'is_active_online_communities',
        'is_fan_rpgs',
        'is_fan_scifi',
        'is_fan_anime',
        'is_plushophile',
        'is_zoophile',
        'is_polyglot',
        'is_animal_rights_advocate',
        'is_vegetarian',
        'is_politically_active',
        'is_otherkin',
        'opinion_artwork',
        'opinion_writing',
        'opinion_conventions',
        'opinion_fursuiting',
        'opinion_plushophilia',
        'opinion_zoophilia',
        'opinion_online_communities',
        'importance_artwork',
        'importance_writing',
        'importance_online_communities',
        'importance_muds',
        'importance_conventions',
        'importance_fursuiting',
        'website_adjspecies',
        'website_artspots',
        'website_deviantart',
        'website_e621',
        'website_flist',
        'website_fchan',
        'website_flayrah',
        'website_furaffinity',
        'website_furcadia',
        'website_furnation',
        'website_furocity',
        'website_furrag',
        'website_furry4life',
        'website_furrymate',
        'website_furryteens',
        'website_furriesxtreme',
        'website_furspace',
        'website_furtopia',
        'website_inkbunny',
        'website_pounced',
        'website_sofurry',
        'website_vcl',
        'website_weasyl',
        'website_wikifur',
        'how_much_human',
        'faith_and_spirituality',
        'friends_look_advice',
        'make_rather_than_buy',
        'more_talented_than_peers',
        'value_cutting_edge',
        'rather_patronize_small_businesses',
        'enjoy_creating_things',
        'ahead_of_pop_culture',
        'tendency_to_overthink',
        'mass_media_lcd',
        'enjoy_leading',
        'focus_on_specific_interests',
        'too_reliant_on_tech',
        'filesharing_nbd',
        'citizens_politically_active',
        'want_to_be_fashionable',
        'exciting_rather_than_predictable',
        'learning_for_learnings_sake',
        'routine_is_comforting',
        'advertising_is_useful',
        'other_people_think_important',
        'learn_about_universe',
        'find_simpler_option',
        'decisions_moral_code',
        'people_more_distant',
        'first_to_try_new_things',
        'consider_intellectual',
        'buy_on_impulse',
        'corporations_soulless',
        'enjoy_traveling',
        'animal_wolf',
        'animal_redfox',
        'animal_greyfox',
        'animal_arcticfox',
        'animal_kitsune',
        'animal_otherfox',
        'animal_coyote',
        'animal_jackal',
        'animal_germanshepherd',
        'animal_husky',
        'animal_collie',
        'animal_otherdog',
        'animal_othercanine',
        'animal_tiger',
        'animal_lion',
        'animal_leopard',
        'animal_snowleopard',
        'animal_panther',
        'animal_cheetah',
        'animal_cougar',
        'animal_domesticcat',
        'animal_otherfeline',
        'animal_dragon',
        'animal_lizard',
        'animal_dinosaur',
        'animal_otherreptile',
        'animal_raccoon',
        'animal_skunk',
        'animal_badger',
        'animal_riverotter',
        'animal_seaotter',
        'animal_weasel',
        'animal_othermustelid',
        'animal_redpanda',
        'animal_othermusteloid',
        'animal_horse',
        'animal_deer',
        'animal_otherungulate',
        'animal_brownbear',
        'animal_grizzlybear',
        'animal_pandabear',
        'animal_polarbear',
        'animal_otherbear',
        'animal_mouse',
        'animal_rat',
        'animal_squirrel',
        'animal_other',
        'animal_raven',
        'animal_raptor',
        'animal_otherbird',
        'animal_rabbit',
        'animal_kangaroo',
        'animal_koala',
        'animal_othermarsupial',
        'animal_lemur',
        'animal_monkey',
        'animal_otherprimate',
        'animal_hyaena',
        'animal_bat',
        'animal_griffin',
    ]

    # Write the results out to the CSV file
    with open(out_dir + '/results.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        logger.info('Beginning dump')
        writer.writeheader()

        logger.info('Writing 2009')
        for row in results2009.buildResults():
            writer.writerow(row)
        logger.info('Done writing 2009')

        logger.info('Writing 2010')
        for row in results2010.buildResults():
            writer.writerow(row)
        logger.info('Done writing 2010')

        logger.info('Writing 2011')
        for row in results2011.buildResults():
            writer.writerow(row)
        logger.info('Done writing 2011')

        logger.info('Writing 2012')
        for row in results2012.buildResults():
            writer.writerow(row)
        logger.info('Done writing 2012')

        logger.info('Writing 2013')
        for row in results2013.buildResults():
            writer.writerow(row)
        logger.info('Done writing 2013')

        logger.info('Writing 2015')
        for row in results2015.buildResults():
            writer.writerow(row)
        logger.info('Done writing 2015')

        logger.info('Writing 2016')
        for row in results2016.buildResults():
            writer.writerow(row)
        logger.info('Done writing 2016')

    logger.info('Finished')

if __name__ == '__main__':
    main(sys.argv[1])
