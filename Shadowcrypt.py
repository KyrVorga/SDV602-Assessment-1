""" 
This is the main application for the Shadowcrypt text-adventure game
"""

import PySimpleGUI
import textwrap
import command.command_manager as cm
import sys
import os

# gets the path to the images folder
try:
    wd = sys._MEIPASS
except AttributeError:
    wd = os.getcwd()
file_path = os.path.join(wd, 'images\\')


def make_a_window():
    """
    Creates a game window

    Returns:
        window: The handle to the game window
    """

    # Sets the theme of the window
    PySimpleGUI.theme("DarkTeal10")

    # User text input
    prompt_input = [
        PySimpleGUI.Input(
            key="-IN-",
            size=20,
            font="Any 12"
        )
    ]

    # Enter and exit buttons
    buttons = [
        PySimpleGUI.Button(
            "Enter",
            bind_return_key=True,
            expand_x=True
        ),
        PySimpleGUI.Button(
            "Exit",
            expand_x=True
        )
    ]

    # output text, displays messages
    item_text = [
        PySimpleGUI.Text(
            "",
            font="Any 12",
            key="-MESSAGE-"
        ),
    ]

    # Location image
    image = [
        PySimpleGUI.Image(
            file_path+"forest.png",
            size=(180, 180),
            key="-IMG-"
        )
    ]

    # Main text area for story, inventory and combat functions
    story_text = [
        PySimpleGUI.Text(
            cm.show_current_place(),
            size=(30, 40),
            auto_size_text=True,
            expand_y=True,
            font="Any 12",
            key="-OUTPUT-",

        )
    ]

    # Create two columns to align content.
    column_left = PySimpleGUI.Column(
        [
            image,
            prompt_input,
            buttons,
            item_text
        ],
        element_justification="c"
    )
    column_right = PySimpleGUI.Column(
        [story_text],
        element_justification="l",
        scrollable=True,
        vertical_scroll_only=True,
    )

    # Merge columns into layout and add a seperator
    layout = [
        column_left,
        PySimpleGUI.VSeparator(),
        column_right
    ]

    return PySimpleGUI.Window("Shadowcrypt", [layout], size=(500, 400))


# If this is the file being run
if __name__ == "__main__":
    # A persistent window - stays until "Exit" is pressed
    window = make_a_window()

    while True:
        event, values = window.read()

        if event == "Enter":
            # Get string from user input
            user_input = values["-IN-"].lower().strip()
            if user_input != '':
                # Run game functions and get text to display in window
                story = cm.interpret_commands(user_input)

                # If a message is not returned then update the window with story text
                if type(story) != tuple:
                    window["-IN-"].update("")
                    window["-OUTPUT-"].update(story)
                    window["-IMG-"].update(file_path + cm.game_places[cm.game_location]["image"], size=(180, 180))
                    window["-MESSAGE-"].update("")

                # Otherwise it's a message
                else:
                    # If message is not an error update the window
                    if not story[0] == "Error":
                        wrapped = textwrap.fill(story[1], 20)
                        window["-MESSAGE-"].update(wrapped)
                        window["-IN-"].update("")

        # User quit event
        elif event == "Exit" or event is None or event == PySimpleGUI.WIN_CLOSED:
            break

        # sUer did nothing or something invalid so pass.
        else:
            pass

    window.close()
