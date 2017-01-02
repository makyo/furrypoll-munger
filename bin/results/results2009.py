import csv
import MySQLdb
import sys
from meta import FIELDNAMES

from MySQLResults import Results

class Results2009(Results):

    questionIndex = {
        'month': 3,
        'year': 4,
        'biosex': 5,
        'gender': 6,
        'orientation': 7,
        'country': 8,
        'state': None,
        'race_white': 10,
        'race_black': 11,
        'race_hispanic': 12,
        'race_asian': 13,
        'race_native': 14,
        'religion': 17,
        'politics_social': None,
        'politics_economic': None,
        'occupation': 21,
        'education': 23,
        'relationship': 25,
        'partner_is_furry': 27,
        'howfurry': 28,
        'years_known_fandom': 29,
        'years_as_furry': 30,
        'furries_known': 31,
        'furries_known_in_person': 32,
        'whoknows_nobody': 33,
        'whoknows_family': None,
        'whoknows_SO': 34,
        'whoknows_furryfriends': 35,
        'whoknows_bestfriends': 36,
        'whoknows_closerfriends': 37,
        'whoknows_friends': 38,
        'whoknows_coworkers': 39,
        'whoknows_commonknowledge': 40,
        'nonfurry_response': 41,
        'nonfurry_response_personal': 42,
        'nonfurry_accuracy': 43,
        'rp_as_different_gender': 44,
        'seximportance': 45,
        'seximportance_personal': 46,
        'seximportance_others': 47,
        'seximportance_public': 48,
        'howoften_chat_online': 49,
        'howoften_roleplay': 50,
        'howoften_attend_conventions': 51,
        'howoften_meet_up': 52,
        'howoften_visit_furry_websites': 53,
        'howoften_participate_in_furry_online_communities': 54,
        'howoften_write': 55,
        'howoften_draw': 56,
        'howoften_play_nonfurry_online_games': 57,
        'howoften_play_nonfurry_rpgs': 58,
        'howoften_attend_nonfurry_conventions': 59,
        'howoften_participate_in_nonfurry_online_communities': 60,
        'is_artist': 61,
        'is_writer': 62,
        'is_musician': 63,
        'is_congoer': 64,
        'is_fursuiter': 65,
        'is_active_online_communities': 66,
        'is_fan_rpgs': 67,
        'is_fan_scifi': 68,
        'is_fan_anime': 69,
        'is_plushophile': 70,
        'is_zoophile': 71,
        'is_polyglot': 72,
        'is_animal_rights_advocate': 73,
        'is_vegetarian': 74,
        'is_politically_active': 75,
        'is_otherkin': None,
        'opinion_artwork': 76,
        'opinion_writing': 77,
        'opinion_conventions': 78,
        'opinion_fursuiting': 79,
        'opinion_plushophilia': 80,
        'opinion_zoophilia': 81,
        'opinion_online_communities': 82,
        'importance_artwork': 83,
        'importance_writing': 84,
        'importance_online_communities': 85,
        'importance_muds': 86,
        'importance_conventions': 87,
        'importance_fursuiting': 88,
        'website_furaffinity': 99,
        'website_sofurry': 100,
        'website_vcl': 101,
        'website_pounced': 102,
        'website_furtopia': 103,
        'website_deviantart': 104,
        'website_furnation': 105,
        'website_artspots': 106,
        'website_wikifur': 107,
        'website_furcadia': 108,
        'how_much_human': 171,
        'animal_wolf': 110,
        'animal_redfox': 111,
        'animal_greyfox': 112,
        'animal_arcticfox': 113,
        'animal_kitsune': 114,
        'animal_otherfox': 115,
        'animal_coyote': 116,
        'animal_germanshepherd': 117,
        'animal_husky': 118,
        'animal_collie': 119,
        'animal_otherdog': 120,
        'animal_othercanine': 121,
        'animal_tiger': 122,
        'animal_lion': 123,
        'animal_leopard': 124,
        'animal_panther': 125,
        'animal_cheetah': 126,
        'animal_cougar': 127,
        'animal_domesticcat': 128,
        'animal_otherfeline': 129,
        'animal_dragon': 130,
        'animal_lizard': 131,
        'animal_dinosaur': 132,
        'animal_otherreptile': 133,
        'animal_raccoon': 134,
        'animal_skunk': 135,
        'animal_badger': 136,
        'animal_riverotter': 137,
        'animal_seaotter': 138,
        'animal_weasel': 139,
        'animal_othermustelid': 140,
        'animal_redpanda': 141,
        'animal_othermusteloid': 142,
        'animal_horse': 143,
        'animal_deer': 144,
        'animal_otherungulate': 145,
        'animal_brownbear': 146,
        'animal_grizzlybear': 147,
        'animal_pandabear': 148,
        'animal_polarbear': 149,
        'animal_otherbear': 150,
        'animal_mouse': 151,
        'animal_rat': 152,
        'animal_squirrel': 153,
        'animal_other': 154,
        'animal_raven': 155,
        'animal_raptor': 156,
        'animal_otherbird': 157,
        'animal_rabbit': 158,
        'animal_kangaroo': 159,
        'animal_koala': 160,
        'animal_othermarsupial': 161,
        'animal_lemur': 162,
        'animal_monkey': 163,
        'animal_otherprimate': 164,
        'animal_hyaena': 165,
        'animal_bat': 166,
        'animal_griffin': 167,
        'animal_jackal': None,
        'animal_snowleopard': None,
    }

def buildResults():
    results = Results2009(year=2009)
    return results.getResults()

if __name__ == '__main__':
    outfile = sys.argv[1]
    with open(outfile, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        for row in buildResults():
            writer.writerow(row)
