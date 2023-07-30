import cmd_parser.token as tkn

# Brief comment about how the following lines work
game_location = 'Elmbrook Village'
game_state = 'explore' # explore / combat / inventory
game_places = {
    'Elmbrook Village': {
        'Story': 'You start your adventure in Elmbrook, where you meet an old wise sage who provides you with a basic '
                 'wooden staff. The sage advises you to explore the nearby locations to gather items and strength '
                 'before facing the challenges ahead.\n'
                 'North: Cloudcrest Peaks\n'
                 'East: Sylvanwood Forest\n'
                 'South: Forsaken Wastes\n'
                 'West: Whispering Willows'
                 'Down: Shadowcrypt',
        'Directions': {
            'North': 'Cloudcrest Peaks',
            'East': 'Sylvanwood Forest',
            'South': 'Forsaken Wastes',
            'West': 'Whispering Willows',
            'Down': 'Shadowcrypt'
        },
        'Image': 'forest.png',
        'Visited': True,
        'Visited Message': 'You are in Elmbrook Village'
    },
    'Sylvanwood Forest': {
        'Story': 'A dense and bewitching forest lies to the east of Elmbrook. You venture into it, discovering a '
                 'hidden glade with a shimmering crystal. You pick up the crystal, which allows you to cast '
                 'protective spells in battle.\n'
                 'East: Crystal Cave\n'
                 'West: Elmbrook Village',
        'Directions': {
            'East': 'Crystal Cave',
            'West': 'Elmbrook Village'
        },
        'Image': 'forest_circle.png',
        'Visited': False,
        'Visited Message': 'You are in the Sylvanwood Forest'
    },
    'Crystal Cave': {
        'Story': 'Deep within the Sylvanwood Forest, you stumble upon the Crystal Cave. Here, you find a set of '
                 'ancient armour forged from enchanted crystals. You can equip the armour, enhancing your defence '
                 'against adversaries.\n'
                 'West: Whispering Willows',
        'Directions': {
            'West': 'Sylvanwood Forest',
        },
        'Image': 'frog.png',
        'Visited': False,
        'Visited Message': 'You are in the Crystal Cave'
    },
    'Whispering Willows': {
        'Story': 'West of Elmbrook, you encounter the eerie Whispering Willows — a haunted grove filled with '
                 'enigmatic whispers. There, you discovers a magical pendant that increases your magical powers '
                 'allowing you to cast spells with'
                 'your staff.\n'
                 'East: Sylvanwood Forest\n',
        'Directions': {
            'East': 'Elmbrook Village',
        },
        'Image': 'frog.png',
        'Visited': False,
        'Visited Message': 'You are in the Whispering Willows'
    },
    'Cloudcrest Peaks': {
        'Story': 'To the north of Elmbrook lies the treacherous Cloudcrest Peaks. Climbing to the summit, '
                 'you discover a mysterious potion that grants you temporary invincibility during battles.\n'
                 'South: Forsaken Wastes\n',
        'Directions': {
            'South': 'Elmbrook Village',
        },
        'Image': 'frog.png',
        'Visited': False,
        'Visited Message': 'You are in the Cloudcrest Peaks'
    },
    'Forsaken Wastes': {
        'Story': 'Venturing southwards, you reache the Forsaken Wastes, a vast, desolate wasteland. Amid the '
                 'scorching sands, you unearth an ancient scroll containing forgotten combat techniques that can '
                 'enhance your attack capabilities.\n'
                 'North: Elmbrook Village\n'
                 'South: Azure Lake\n',
        'Directions': {
            'North': 'Elmbrook Village',
            'South': 'Azure Lake',
        },
        'Image': 'frog.png',
        'Visited': False,
        'Visited Message': 'You are in the Forsaken Wastes'
    },
    'Azure Lake': {
        'Story': 'Further south, you arrives at the tranquil Azure Lake, guarded by a mythical water serpent. if you '
                 'can defeat the serpent, you may claim a vial of healing water, which fully restores your health.\n'
                 'North: Forsaken Wastes\n',
        'Directions': {
            'North': 'Forsaken Wastes',
        },
        'Image': 'frog.png',
        'Visited': False,
        'Visited Message': 'You are at the Azure Lake'
    },
    'Shadowcrypt': {
        'Story': 'The sage back in Elmbrook told you how to enter the Shadowcrypt, the labyrinthine crypt beneath the '
                 'village, where the mage is. You\'ve entered the Shadowcrypt in order to save the village\n'
                 'Down: Inner Sanctum\n'
                 'Up: Elmbrook village\n',
        'Directions': {
            'Down': 'Inner Sanctum',
            'Up': 'Elmbrook village',
        },
        'Image': 'frog.png',
        'Visited': False,
        'Visited Message': 'You are in the Shadowcrypt'
    },
    'Inner Sanctum': {
        'Story': 'After stumbling through the Shadowcrypt you finally reache the Inner Sanctum and confront the '
                 'vile mage.\n'
                 'Up: Shadowcrypt',
        'Directions': {
            'Up': 'Shadowcrypt',
        },
        'Image': 'frog.png',
        'Visited': False,
        'Visited Message': 'You are in the Inner Sanctum'
    },
}


def interpret_commands(token_list):
    tokens = tkn.validate_list(token_list, game_state)
    match game_state:
        case "explore":
            explore_game_play(tokens)
        case "combat":
            combat_game_play(tokens)
        case "inventory":
            inventory_game_play(tokens)


def show_current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_location

    return game_places[game_location]['Story']


def explore_game_play(token_list):
    return True


def combat_game_play(token_list):
    return True


def inventory_game_play(token_list):
    return True


def game_play(direction):
    """
    Runs the game_play

    Args:
        direction string: _North or South

    Returns:
        string: the story at the current place
    """
    global game_location

    if direction.lower() in 'northsoutheastwest':  # is this a nasty check?
        game_place = game_places[game_location]
        proposed_state = game_place[direction.capitalize()]
        if proposed_state == '':
            return 'You can not go that way.\n' + game_places[game_location]['Story']
        else:
            game_location = proposed_state
            return game_places[game_location]['Story']




