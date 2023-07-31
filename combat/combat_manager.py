# this module needs to store player combat stats, handle the combat actions,
# store the combat enemies and their stats.

import command.command_manager as cm

game_enemies = {
    'Guardian Serpent': {
        'health': 10,
        'attack': 1000,
        'reward': 'Vial of Healing Water',
        'location': 'azure lake'
    },
    'Great Mage Jaldabaoth': {
        'health': 100,
        'attack': 10,
        'location': 'inner sanctum'
    },
}

player_stats = {
    'health': 25,
    'attack': 5,
}


def combat_game_play(token_list):
    enemy = cm.game_places[cm.game_location]['enemy']
    match token_list[0]:
        case "run":
            cm.game_state = 'explore'
            return cm.show_current_place()
        case "attack":
            enemy['health'] - player_stats['attack']
            if enemy['health'] <= 0:

            # return updated stats
        # case "block":
        #
        # case "heal":
        #
        # case "potion":
        #
        # case "magic":
        #
        # case _:

    return True