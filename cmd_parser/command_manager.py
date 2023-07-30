import cmd_parser.token as tkn

# Brief comment about how the following lines work
game_location = 'Forest'
game_state = 'explore' # explore / combat / inventory
game_places = {'Forest': {'Story': 'You are in the forest.\nTo the north is a cave.\nTo the south is a castle.\nTo '
                                   'the east are mountains',
                          'North': 'Cave', 'South': 'Castle', 'East': 'Mountains', 'Image': 'forest.png'},
               'Cave': {'Story': 'You are at the cave.\nTo the south is forest.',
                        'North': '', 'South': 'Forest', 'Image': 'forest_circle.png'},
               'Castle': {'Story': 'You are at the castle.\nTo the north is forest.',
                          'North': 'Forest', 'South': '', 'Image': 'frog.png'},
               'Mountains': {'Story': 'You are in the mountains.\nTo the west is forest.',
                             'West': 'Forest', 'Image': 'mountains.png'},
               }


def interpret_commands(token_list):
    tokens = tkn.validatelist(token_list, game_state)
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


def explore_game_play():
    return True


def combat_game_play():
    return True


def inventory_game_play():
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




