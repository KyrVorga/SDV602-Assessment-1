""" 
This is the main application for the Shadowcrypt text-adventure game
"""

import PySimpleGUI as sg
import textwrap
import command.command_manager as cm
import os

# gets the path to the images folder
file_path = os.path.join(os.getcwd(), 'images/')


def make_a_window():
    """
    Creates a game window

    Returns:
        window: the handle to the game window
    """

    # sets the theme of the window
    sg.theme("DarkTeal10")

    # user text input
    prompt_input = [
        sg.Input(
            key="-IN-",
            size=20,
            font="Any 12"
        )
    ]

    # enter and exit buttons
    buttons = [
        sg.Button(
            "Enter",
            bind_return_key=True,
            expand_x=True
        ),
        sg.Button(
            "Exit",
            expand_x=True
        )
    ]

    # output text, displays messages
    item_text = [
        sg.Text(
            "",
            font="Any 12",
            key="-MESSAGE-"
        ),
    ]

    # location image
    image = [
        sg.Image(
            file_path+"forest.png",
            size=(180, 180),
            key="-IMG-"
        )
    ]

    # Main text area for story, inventory and combat functions
    story_text = [
        sg.Text(
            cm.show_current_place(),
            size=(30, 40),
            auto_size_text=True,
            # expand_x=True,
            expand_y=True,
            font="Any 12",
            key="-OUTPUT-",

        )
    ]

    # create two columns to align content.
    column_left = sg.Column(
        [
            image,
            prompt_input,
            buttons,
            item_text
        ],
        element_justification="c"
    )
    column_right = sg.Column(
        [story_text],
        element_justification="l",
        scrollable=True,
        vertical_scroll_only=True,
    )

    # merge columns into layout and add a seperator
    layout = [
        column_left,
        sg.VSeparator(),
        column_right
    ]

    return sg.Window("Shadowcrypt", [layout], size=(500, 400))


if __name__ == "__main__":
    # A persistent window - stays until "Exit" is pressed
    window = make_a_window()

    while True:
        event, values = window.read()

        if event == "Enter":
            # Get string from user input
            user_input = values["-IN-"].lower().strip()
            if user_input != '':
                # run game functions and get text to display in window
                story = cm.interpret_commands(user_input)

                # if a message is not returned then update the window with story text
                if type(story) != tuple:
                    window["-IN-"].update("")
                    window["-OUTPUT-"].update(story)
                    window["-IMG-"].update(file_path + cm.game_places[cm.game_location]["image"], size=(180, 180))
                    window["-MESSAGE-"].update("")

                # otherwise it"s a message
                else:
                    # if message is not an error update the window
                    if not story[0] == "Error":
                        wrapped = textwrap.fill(story[1], 20)
                        window["-MESSAGE-"].update(wrapped)
                        window["-IN-"].update("")

        # User quit event
        elif event == "Exit" or event is None or event == sg.WIN_CLOSED:
            break

        # user did nothing or something invalid so pass.
        else:
            pass

    window.close()
