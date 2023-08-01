# this module needs to store player combat stats, handle the combat actions,
# store the combat enemies and their stats.

import command.command_manager as cm

game_enemies = {
    'Guardian Serpent': {
        'health': 10,
        'attack': 1000,
        'reward': 'Vial of Healing Water',
        'location': 'azure lake',
        'defeated': False,
        'description': "The Guardian Serpent circles the Azure Lake, should you approach it will defend the lake.",
        'death_message': ''
    },
    'Great Mage Jaldabaoth': {
        'health': 100,
        'attack': 10,
        'location': 'inner sanctum',
        'reward': 'Jaldabaoth\'s Staff',
        'defeated': False,
        'description': "The great mage Jaldabaoth stands impatiently before you, waiting for you to take the first "
                       "strike..",
        'death_message': ''
    },
}

player = {
    'actions': [
        'attack\n',
        'run\n'
    ],

    'stats': {
        'health': 25,
        'attack': 5,
    },
    'death_message': ''
}


def combat_game_play(token_list):
    enemy_name = cm.game_places[cm.game_location]['enemy']
    enemy = game_enemies[enemy_name]
    match token_list[0]:
        case "run":
            cm.game_state = 'explore'
            return cm.show_current_place()
        case "attack":
            enemy['health'] = enemy['health'] - player['stats']['attack']
            player['stats']['health'] = player['stats']['health'] - enemy['attack']
            if enemy['health'] <= 0:
                return enemy['death_message']
            elif player['stats']['health'] <= 0:
                return player['death_message']

            return show_combat_text(enemy_name)
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


def show_combat_text(enemy):
    combat_list = [
        'Name: ',
        enemy,
        '\n',
        'Health: ',
        str(game_enemies[enemy]['health']),
        '\n',
        'Attack: ',
        str(game_enemies[enemy]['attack']),
        '\n',
        'Defeated: ',
        str(game_enemies[enemy]['defeated']),
        '\n\n',
        'Player:\n',
        'Health: ',
        str(player['stats']['health']),
        '\n',
        'Attack: ',
        str(player['stats']['attack']),
        '\n',
        'Player Actions:\n',
        ''.join(player['actions'])
    ]
    return ''.join(combat_list)