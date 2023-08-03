import command.command_manager as cm
import combat.combat_manager as com
import textwrap
import command.token as tkn

game_items = {
    'vial of healing water': {
        'name': 'Vial of Healing Water',
        'source': 'Guardian Serpent',
        'description': 'Fully restores your health in combat.',
        'found_text': 'You defeated the Guardian Serpent and claimed the Vial.',
        'equippable': False,
        'equipped': False,
        'acquired': False,
        'used': False
    },
    'wooden staff': {
        'name': 'Wooden Staff',
        'source': 'Elmbrook Village',
        'description': 'A simple wooden staff. Can be used for attacking.',
        'found_text': 'You were given the staff by the wise old sage of Elmbrook Village.',
        'equippable': True,
        'equipped': False,
        'acquired': False
    },
    'shimmering crystal': {
        'name': 'Shimmering Crystal',
        'source': 'Sylvanwood Forest',
        'description': 'Allows you to cast protective spells in battle.',
        'found_text': 'You found a Shimmering Crystal in a hidden grove.',
        'equippable': False,
        'equipped': False,
        'acquired': False,
        'effect_active': False
    },
    'enchanted armour': {
        'name': 'Enchanted Armour',
        'source': 'Crystal Cave',
        'description': 'enhances your defence against adversaries.',
        'found_text': 'You found the Enchanted Armour within the cave.',
        'equippable': True,
        'equipped': False,
        'acquired': False
    },
    'magical pendant': {
        'name': 'Magical Pendant',
        'source': 'Whispering Willows',
        'description': 'increases your magical powers allowing you to cast spells with your staff.',
        'found_text': 'You found a Magical Pendant by a tombstone.',
        'equippable': True,
        'equipped': False,
        'acquired': False
    },
    'invincibility potion': {
        'name': 'Invincibility Potion',
        'source': 'Cloudcrest Peaks',
        'description': 'Grants you temporary invincibility during a battle.',
        'found_text': 'You found an invincibility potion at the summit',
        'equippable': False,
        'equipped': False,
        'acquired': False,
        'used': False,
        'effect_active': False
    },
    'ancient scroll': {
        'name': 'Ancient Scroll',
        'source': 'Forsaken Wastes',
        'description': 'Teaches you ancient combat techniques, increasing your attack power.',
        'found_text': 'You found an Ancient scroll buried within the sand.',
        'equippable': False,
        'equipped': False,
        'acquired': False,
        'used': False
    },
    'inner sanctum key': {
        'name': 'Inner Sanctum Key',
        'source': 'Shadowcrypt',
        'description': 'Allows access into the Inner Sanctum',
        'found_text': 'You located the key to the Inner Sanctum.',
        'equippable': False,
        'equipped': False,
        'acquired': False
    },
    'jaldabaoth\'s staff': {
        'name': 'Jaldabaoth\'s Staff',
        'source': 'Great Mage Jaldabaoth',
        'description': 'You defeated the Great Mage Jaldabaoth and claimed his staff!',
        'found_text': 'You defeated the Great Mage Jaldabaoth and claimed his staff!',
        'equippable': False,
        'equipped': False,
        'acquired': False
    },
}


def toggle_equip_status(action, item):
    health = 0
    attack = 0
    if not game_items[item]['acquired']:
        return tuple(('Message', 'You don\'t have this item.'))
    elif not game_items[item]['equippable']:
        return tuple(('Message', 'You can\'t equip this item.'))
    else:
        match item:
            case 'wooden staff':
                attack += 4

            case 'enchanted armour':
                health += 25

            case 'magical pendant':
                attack += 5

        if action == 'unequip':
            game_items[item]['equipped'] = False;
            health *= -1
            attack *= -1
        else:
            game_items[item]['equipped'] = True;

        com.player['stats']['attack'] += attack
        com.player['stats']['max_health'] += health
        com.player['stats']['health'] += health


def inventory_game_play(token_list):
    match token_list[0]:
        # case "back":
        #     cm.game_state = 'explore'
        #     return cm.show_current_place()

        case "equip":
            if len(token_list) <= 1:
                return tuple(('Error', 'Incorrect amount of arguments.'))
            else:
                action = token_list.pop(0)
                item_name = ' '.join(token_list)
                if item_name in game_items:
                    toggle_equip_status(action, item_name)
                    message = 'You equipped the ' + game_items[item_name]['name']
                    return tuple(('Message', message))
                else:
                    return tuple(('Error', 'That is not a valid item.'))

        case "unequip":
            if len(token_list) <= 1:
                return tuple(('Error', 'Incorrect amount of arguments.'))
            else:
                action = token_list.pop(0)
                item_name = ' '.join(token_list)
                if item_name in game_items:
                    toggle_equip_status(action, item_name)
                    message = 'You unequipped the ' + game_items[item_name]['name']
                    return tuple(('Message', message))
                else:
                    return tuple(('Error', 'That is not a valid item.'))
                # return show_inventory_text()
        case "use":
            if len(token_list) <= 1:
                return tuple(('Error', 'Incorrect amount of arguments.'))
            else:
                token_list.pop(0)
                item_name = ' '.join(token_list)
                if not item_name == 'ancient scroll':
                    return tuple(('Message', 'You cannot use this item like this.'))
                else:
                    if game_items['ancient scroll']['used']:
                        return tuple(('Message', 'You already learned from the scroll'))
                    else:
                        game_items['ancient scroll']['used'] = True
                        com.player['stats']['attack'] += 4

