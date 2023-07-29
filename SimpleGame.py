""" 
A comment describing the game module
"""
import PySimpleGUI as sg

import cmd_parser.token as tkn
import cmd_parser.command_manager as cm


def make_a_window():
    """
    Creates a game window

    Returns:
        window: the handle to the game window
    """

    sg.theme('DarkTeal10')  # please make your windows
    prompt_input = [sg.Text('Enter your command', font='Any 12'), sg.Input(
        key='-IN-', size=(20, 1), font='Any 12')]
    buttons = [sg.Button('Enter', bind_return_key=True), sg.Button('Exit')]
    command_col = sg.Column([prompt_input, buttons], element_justification='r')

    layout = [
        [sg.Image('images/forest.png', size=(100, 100), key="-IMG-"),
         sg.Text(cm.show_current_place(), size=(100, 4), font='Any 12', key='-OUTPUT-')],
        [command_col]
    ]

    return sg.Window('Adventure Game', layout, size=(320, 200))


if __name__ == "__main__":
    # testing for now
    # print(show_current_place())
    # current_story = game_play('North')
    # print(show_current_place())

    # A persistent window - stays until "Exit" is pressed
    window = make_a_window()

    while True:
        event, values = window.read()
        # print(event)
        if event == 'Enter':
            tokens = tkn.validate_list(values['-IN-'].lower())

            for token in tokens:
                window['-OUTPUT-'].update(cm.game_play(token))

            window['-IMG-'].update('images/' + cm.game_places[cm.game_state]['Image'], size=(100, 100))
            pass

        elif event == 'Exit' or event is None or event == sg.WIN_CLOSED:
            break

        else:
            pass

    window.close()
