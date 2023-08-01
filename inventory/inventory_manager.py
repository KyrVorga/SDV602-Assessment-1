import command.command_manager as cm
import textwrap
import command.token as tkn

game_items = {
    'vial of healing water': {
        'name': 'Vial of Healing Water',
        'source': 'Guardian Serpent',
        'description': 'Can fully restore your health in combat.',
        'found_text': 'You defeated the Guardian Serpent and claimed the Vial.',
        'equippable': False,
        'equipped': False,
        'acquired': False
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
        'name': 'Vial of Healing Water',
        'source': 'Guardian Serpent',
        'description': 'azure lake',
        'equippable': False,
        'equipped': False,
        'acquired': False
    },
    'enchanted armour': {
        'name': 'Vial of Healing Water',
        'source': 'Guardian Serpent',
        'description': 'azure lake',
        'equippable': True,
        'equipped': False,
        'acquired': False
    },
    'magical pendant': {
        'name': 'Vial of Healing Water',
        'source': 'Guardian Serpent',
        'description': 'azure lake',
        'equippable': True,
        'equipped': False,
        'acquired': False
    },
    'invincibility potion': {
        'name': 'Vial of Healing Water',
        'source': 'Guardian Serpent',
        'description': 'azure lake',
        'equippable': False,
        'equipped': False,
        'acquired': False
    },
    'ancient scroll': {
        'name': 'Vial of Healing Water',
        'source': 'Guardian Serpent',
        'description': 'azure lake',
        'equippable': False,
        'equipped': False,
        'acquired': False
    },
    'inner sanctum key': {
        'name': 'Vial of Healing Water',
        'source': 'Guardian Serpent',
        'description': 'azure lake',
        'equippable': False,
        'equipped': False,
        'acquired': False
    },
}


def inventory_game_play(token_list):
    match token_list[0]:
        case "back":
            cm.game_state = 'explore'
            return cm.show_current_place()
        case "equip":
            pass
        case "unequip":
            pass
        case "use":
            pass


def show_inventory_text(intial_text=None):
    inventory_list = []

    if intial_text is not None:
        inventory_list.append(textwrap.fill(intial_text, 35))
        inventory_list.append('\n\n')

    for item in game_items:
        if game_items[item]['acquired']:
            inventory_list.append(game_items[item]['name'])
            inventory_list.append('\n')
            inventory_list.append(textwrap.fill(game_items[item]['description'], 35))
            inventory_list.append('\n\n')

    inventory_list.append('Actions:\nback\nequip <item>\nunequip <item>\nuse <item>')

    return ''.join(inventory_list)
