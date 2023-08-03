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
        'effect_active': False
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
        'equippable': False,
        'equipped': False,
        'acquired': False,
        'effect_active': False
    },
    'enchanted armour': {
        'name': 'Enchanted Armour',
        'source': 'Crystal Cave',
        'description': 'enhances your defence against adversaries.',
        'equippable': True,
        'equipped': False,
        'acquired': False
    },
    'magical pendant': {
        'name': 'Magical Pendant',
        'source': 'Whispering Willows',
        'description': 'increases your magical powers allowing you to cast spells with your staff.',
        'equippable': True,
        'equipped': False,
        'acquired': False
    },
    'invincibility potion': {
        'name': 'Invincibility Potion',
        'source': 'Cloudcrest Peaks',
        'description': 'Grants you temporary invincibility during a battle.',
        'equippable': False,
        'equipped': False,
        'acquired': False,
        'effect_active': False
    },
    'ancient scroll': {
        'name': 'Ancient Scroll',
        'source': 'Forsaken Wastes',
        'description': 'Teaches you ancient combat techniques, increasing your attack power.',
        'equippable': False,
        'equipped': False,
        'acquired': False
    },
    'inner sanctum key': {
        'name': 'Inner Sanctum Key',
        'source': 'Shadowcrypt',
        'description': 'Allows access into the Inner Sanctum',
        'equippable': False,
        'equipped': False,
        'acquired': False
    },
}


def toggle_equip_status(action, item):
    health = 0
    attack = 0
    if not game_items[item]['acquired']:
        return Exception("You don't have this item.")
    elif not game_items[item]['equippable']:
        return Exception("You can't equip this item.")
    else:
        match item:
            case 'wooden staff':
                attack += 4
                pass

            case 'enchanted armour':
                health += 25

            case 'magical pendant':
                attack += 5
                pass
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
        case "back":
            cm.game_state = 'explore'
            return cm.show_current_place()

        case "equip":
            if len(token_list) <= 1:
                return Exception("Incorrect amount of arguments.")
            else:
                action = token_list.pop(0)
                item_name = ' '.join(token_list)
                toggle_equip_status(action, item_name)
                return show_inventory_text()

        case "unequip":
            if len(token_list) <= 1:
                return Exception("Incorrect amount of arguments.")
            else:
                action = token_list.pop(0)
                item_name = ' '.join(token_list)
                toggle_equip_status(action, item_name)
                return show_inventory_text()
        case "use":
            pass


def show_inventory_text(intial_text=None):
    inventory_list = []

    if intial_text is not None:
        inventory_list.append(textwrap.fill(intial_text, 35))
        inventory_list.append('\n\n')

    inventory_list.append('Inventory:\n')
    for item in game_items:
        if game_items[item]['acquired']:
            inventory_list.append(game_items[item]['name'])
            inventory_list.append('\n')
            inventory_list.append(textwrap.fill(game_items[item]['description'], 35))
            inventory_list.append('\n\n')

    inventory_list.append('Equipped:\n')
    for item in game_items:
        if game_items[item]['equipped']:
            inventory_list.append(game_items[item]['name'])
            inventory_list.append('\n\n')

    inventory_list.append('Actions:\nback\nequip <item>\nunequip <item>\nuse <item>')

    return ''.join(inventory_list)
