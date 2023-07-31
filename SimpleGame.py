""" 
A comment describing the game module
"""
import PySimpleGUI as sg
import textwrap
import command.token as tkn
import command.command_manager as cm


def make_a_window():
    """
    Creates a game window

    Returns:
        window: the handle to the game window
    """

    sg.theme('DarkTeal10')  # please make your windows
    prompt_input = [
        # sg.Text(
        #     'Enter your command',
        #     font='Any 12'
        # ),
        sg.Input(
            key='-IN-',
            size=20,
            font='Any 12'
        )
    ]
    buttons = [
        sg.Button(
            'Enter',
            bind_return_key=True,
            expand_x=True
        ),
        sg.Button(
            'Exit',
            expand_x=True
        )
    ]

    image = [
        sg.Image(
            'images/forest.png',
            size=(180, 180),
            key="-IMG-"
        )
    ]

    wrapped_text = textwrap.fill(
        "In a land of magic and mystery, a young adventurer embarks on a journey to save Elmbrook village from a "
        "powerful and vile mage who is holed up deep within the Shadowcrypt. You start your adventure in Elmbrook, "
        "where you meet an old wise sage who provides you with a basic wooden staff. The sage advises you to explore "
        "the nearby locations to gather items and strength before facing the challenges ahead.",
        35
    ) + ('\n\nYou are in Elmbrook village.\n'
         'North: Cloudcrest Peaks\n'
         'East: Sylvanwood Forest\n'
         'South: Forsaken Wastes\n'
         'West: Whispering Willows'
         )

    story_text = [
        sg.Text(
            wrapped_text,
            # size=(100, 4),
            auto_size_text=True,
            expand_x=True,
            expand_y=True,
            font='Any 12',
            key='-OUTPUT-'
        )
    ]

    column_left = sg.Column(
        [
            image,
            prompt_input,
            buttons
        ],
        element_justification='c'
    )
    column_right = sg.Column(
        [story_text],
        element_justification='l'
    )

    layout = [
        column_left,
        column_right
    ]

    return sg.Window('Adventure Game', [layout], size=(500, 400))


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
            story = cm.interpret_commands(values['-IN-'].lower())

            if type(story) != Exception:
                window['-OUTPUT-'].update(story)
                window['-IN-'].update('')
                window['-IMG-'].update('images/' + cm.game_places[cm.game_location]['image'], size=(180, 180))

        elif event == 'Exit' or event is None or event == sg.WIN_CLOSED:
            break

        else:
            pass

    window.close()
