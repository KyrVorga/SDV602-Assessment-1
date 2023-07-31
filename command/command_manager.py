import command.token as tkn
import inventory.inventory_manager as im
import combat.combat_manager as com
import textwrap

# Brief comment about how the following lines work
game_location = 'elmbrook village'
game_state = 'explore'  # explore / combat / inventory
game_places = {
    'elmbrook village': {
        'story':
            'You start your adventure in Elmbrook, where you meet an old wise sage who provides you with a basic '
            'wooden staff. The sage advises you to explore the nearby locations to gather items and strength before '
            'facing the challenges ahead.',
        'story_directions':
            'North: Cloudcrest Peaks\n'
            'East: Sylvanwood Forest\n'
            'South: Forsaken Wastes\n'
            'West: Whispering Willows\n'
            'Down: Shadowcrypt',
        'directions': {
            'north': 'Cloudcrest Peaks',
            'east': 'Sylvanwood Forest',
            'south': 'Forsaken Wastes',
            'west': 'Whispering Willows',
            'down': 'Shadowcrypt'
        },
        'image': 'forest.png',
        'visited': True,
        'visited message': 'You are in Elmbrook Village.'
    },
    'sylvanwood forest': {
        'story':
            'A dense and bewitching forest lies to the east of Elmbrook. You venture into it, discovering a hidden '
            'glade with a shimmering crystal. You pick up the crystal, which allows you to cast protective spells in '
            'battle.',
        'story_directions':
            'East: Crystal Cave\n'
            'West: Elmbrook Village\n',
        'directions': {
            'east': 'Crystal Cave',
            'west': 'Elmbrook Village'
        },
        'image': 'forest_circle.png',
        'visited': False,
        'visited message': 'You are in the Sylvanwood Forest.'
    },
    'crystal cave': {
        'story': 'Deep within the Sylvanwood Forest, you stumble upon the Crystal Cave. Here, you find a set of '
                 'ancient armour forged from enchanted crystals. You can equip the armour, enhancing your defence '
                 'against adversaries.',
        'story_directions':
                 'West: Sylvanwood Forest',
        'directions': {
            'west': 'Sylvanwood Forest',
        },
        'image': 'frog.png',
        'visited': False,
        'visited message': 'You are in the Crystal Cave.'
    },
    'whispering willows': {
        'story': 'West of Elmbrook, you encounter the eerie Whispering Willows — a haunted grove filled with '
                 'enigmatic whispers. There, you discovers a magical pendant that increases your magical powers '
                 'allowing you to cast spells with.'
                 'your staff.\n',
        'story_directions':
                 'East: Elmbrook Village\n',
        'directions': {
            'east': 'Elmbrook Village',
        },
        'image': 'frog.png',
        'visited': False,
        'visited message': 'You are in the Whispering Willows.'
    },
    'cloudcrest peaks': {
        'story': 'To the north of Elmbrook lies the treacherous Cloudcrest Peaks. Climbing to the summit, '
                 'you discover a mysterious potion that grants you temporary invincibility during battles.\n',
        'story_directions':
                 'South: Elmbrook Village\n',
        'directions': {
            'south': 'Elmbrook Village',
        },
        'image': 'frog.png',
        'visited': False,
        'visited message': 'You are in the Cloudcrest Peaks.'
    },
    'forsaken wastes': {
        'story': 'Venturing southwards, you reache the Forsaken Wastes, a vast, desolate wasteland. Amid the '
                 'scorching sands, you unearth an ancient scroll containing forgotten combat techniques that can '
                 'enhance your attack capabilities.\n',
        'story_directions':
                 'North: Elmbrook Village\n'
                 'South: Azure Lake\n',
        'directions': {
            'north': 'Elmbrook Village',
            'south': 'Azure Lake',
        },
        'image': 'frog.png',
        'visited': False,
        'visited message': 'You are in the Forsaken Wastes.'
    },
    'azure lake': {
        'story': 'Further south, you arrives at the tranquil Azure Lake, guarded by a mythical water serpent. if you '
                 'can defeat the serpent, you may claim a vial of healing water, which fully restores your health.\n',
        'story_directions':
                 'North: Forsaken Wastes.\n',
        'directions': {
            'north': 'Forsaken Wastes',
        },
        'image': 'frog.png',
        'visited': False,
        'visited message': 'You are at the Azure Lake.',
        'enemy': 'Guardian Serpent',
        'item': 'Vial of Healing Water'
    },
    'shadowcrypt': {
        'story': 'The sage back in Elmbrook told you how to enter the Shadowcrypt, the labyrinthine crypt beneath the '
                 'village, where the mage is. You\'ve entered the Shadowcrypt in order to save the village.\n',
        'story_directions': '\n\nDown: Inner Sanctum\n'
                            'Up: Elmbrook village\n',
        'directions': {
            'down': 'Inner Sanctum',
            'up': 'Elmbrook village',
        },
        'image': 'frog.png',
        'visited': False,
        'visited message': 'You are in the Shadowcrypt.'
    },
    'inner sanctum': {
        'story': 'After stumbling through the Shadowcrypt you finally reach the Inner Sanctum and confront the '
                 'vile mage.\n',
        'story_directions':
                 'Up: Shadowcrypt',
        'directions': {
            'up': 'Shadowcrypt',
        },
        'image': 'frog.png',
        'visited': False,
        'visited message': 'You are in the Inner Sanctum.',
        'enemy': 'Great Mage Jaldabaoth'
    },
}


def interpret_commands(token_list):
    tokens = tkn.validate_list(token_list, game_state)
    if type(tokens) == Exception:
        return tokens
    match game_state:
        case "explore":
            result = explore_game_play(tokens)
        case "combat":
            result = com.combat_game_play(tokens)
        case "inventory":
            result = im.inventory_game_play(tokens)
        case _:
            result = ''
    return result


def show_current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_location

    return game_places[game_location]['story']


def explore_game_play(token_list):
    global game_location
    global game_state

    if token_list[0] in game_places[game_location]['directions']:
        direction = token_list[0]
        proposed_location = game_places[game_location]['directions'][direction].lower()
        if proposed_location is not None:
            game_location = proposed_location
            if not game_places[game_location]['visited']:
                game_places[game_location]['visited'] = True
                wrapped_text = textwrap.fill(game_places[game_location]['story'],
                                             35
                                             ) + '\n\n' + (game_places[game_location]['story_directions'])
                return wrapped_text
            else:
                wrapped_text = textwrap.fill(game_places[game_location]['visited message'],
                                             35
                                             ) + '\n\n' + (game_places[game_location]['story_directions'])
                return wrapped_text

    elif token_list[0] == 'engage':
        game_state = 'combat'

    elif token_list[0] == 'inventory':
        game_state = 'inventory'





def inventory_game_play(token_list):
    return True