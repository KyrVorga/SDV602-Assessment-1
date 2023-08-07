# this module needs to store player combat stats, handle the combat actions,
# store the combat enemies and their stats.

import command.command_manager as cm
import inventory.inventory_manager as im
import status.status_manager as sts

game_enemies = {
    'guardian serpent': {
        'name': 'Guardian Serpent',
        'health': 10,
        'attack': 1000,
        'reward': 'Vial of Healing Water',
        'location': 'azure lake',
        'defeated': False,
        'description': "The Guardian Serpent circles the Azure Lake, should you approach it will defend the lake.",
        'death_message': 'You defeated the Guardian Serpent and claimed the Vial.'
    },
    'great mage jaldabaoth': {
        'name': 'Great Mage Jaldabaoth',
        'health': 100,
        'attack': 10,
        'location': 'inner sanctum',
        'reward': 'Jaldabaoth\'s Staff',
        'defeated': False,
        'description': "The great mage Jaldabaoth stands impatiently before you, waiting for you to take the first "
                       "strike..",
        'death_message': 'You defeated the Great Mage Jaldabaoth and claimed his staff!\nYou should return to Elmbrook '
                         'Village'
    },
}

player = {
    'actions': [
        'attack\n',
        'run\n'
    ],
    'stats': {
        'max_health': 25,
        'health': 25,
        'attack': 1,
    },
    'death_message': 'You died... Elmbrook Village is doomed.'
}


def combat_game_play(token_list):
    enemy_name = cm.game_places[cm.game_location]['enemy'].lower()
    enemy = game_enemies[enemy_name]
    if player['stats']['health'] <= 0:
        return tuple(('Message', 'You are dead... Dead things cat\'t do much...'))
    match token_list[0]:
        case "run":
            cm.game_state = 'explore'
            return cm.show_current_place()
        case "attack":
            enemy['health'] = enemy['health'] - player['stats']['attack']

            if not im.game_items['invincibility potion']['effect_active']:
                im.game_items['invincibility potion']['effect_active'] = False
                player['stats']['health'] = player['stats']['health'] - enemy['attack']

            if player['stats']['health'] <= 0:
                return sts.show_status_text('game over', player['death_message'])
            elif enemy['health'] <= 0:
                cm.game_state = 'explore'
                for item in im.game_items:
                    if im.game_items[item]['source'].lower() == enemy_name:
                        im.game_items[item]['acquired'] = True
                    game_enemies[enemy_name]['defeated'] = True
                return sts.show_status_text('story', enemy['death_message'])

            return show_combat_text(enemy_name.lower())

        case "block":
            if not im.game_items['shimmering crystal']['acquired']:
                return tuple(('Message', 'You can\'t perform this action'))
            else:
                return tuple(('Message', 'You blocked the attack.'))

        case "heal":
            if not im.game_items['vial of healing water']['acquired']:
                return tuple(('Message', 'You can\'t perform this action'))
            else:
                if im.game_items['vial of healing water']['used']:
                    return tuple(('Message', 'You already used this item.'))
                else:
                    max_health = player['stats']['max_health']
                    player['stats']['health'] = max_health
                    im.game_items['vial of healing water']['used'] = True
                    return tuple(('Message', 'You restored your health.'))

        case "potion":
            if not im.game_items['invincibility potion']['acquired']:
                return tuple(('Message', 'You can\'t perform this action'))
            else:
                if im.game_items['invincibility potion']['used']:
                    return tuple(('Message', 'You already used this item.'))
                else:
                    im.game_items['invincibility potion']['used'] = True
                    im.game_items['invincibility potion']['effect_active'] = True
                    return tuple(('Message', 'You are invincible until after your next attack.'))

    if enemy['health'] <= 0 < player['stats']['health']:
        for item in im.game_items:
            if im.game_items[item]['source'] == enemy['name']:
                im.game_items[item]['acquired'] = True
    return show_combat_text(enemy_name.lower())


# Try change to a comprehension
def show_combat_text(enemy):
    combat_list = [
        'Name: ',
        game_enemies[enemy]['name'],
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
        '\n\n',
        'Player Actions:\n',
        ''.join(player['actions'])
    ]

    return ''.join(combat_list)
