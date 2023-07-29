import PySimpleGUI as sg

import cmd_parser.token as token

# Brief comment about how the following lines work
game_state = 'Forest'
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


def show_current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state

    return game_places[game_state]['Story']


def game_play(direction):
    """
    Runs the game_play

    Args:
        direction string: _North or South

    Returns:
        string: the story at the current place
    """
    global game_state

    if direction.lower() in 'northsoutheastwest':  # is this a nasty check?
        game_place = game_places[game_state]
        proposed_state = game_place[direction.capitalize()]
        if proposed_state == '':
            return 'You can not go that way.\n' + game_places[game_state]['Story']
        else:
            game_state = proposed_state
            return game_places[game_state]['Story']




