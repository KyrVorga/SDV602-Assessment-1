"""
This is the status manager for Shadowcrypt, it displays player status information such as inventory and equipment.
"""

import inventory.inventory_manager as im
import command.command_manager as cm
import combat.combat_manager as com
import command.token as tkn
import textwrap


def show_status_text(to_show: str, initial_text=None):
    text_list = []

    # If there is initial text append it to the list
    if initial_text is not None:
        text_list.append(textwrap.fill(initial_text, 30))
        text_list.append("\n\n")

    match to_show:
        # Appends the text of the current location
        case "location":
            # If it's the first time visiting display story text
            if not cm.game_places[cm.game_location]["visited"]:
                cm.game_places[cm.game_location]["visited"] = True
                text_list.append(textwrap.fill(cm.game_places[cm.game_location]["story"], 30))

            # Otherwise append the visited text
            else:
                text_list.append(textwrap.fill(cm.game_places[cm.game_location]["visited message"], 30))

            # If there is an enemy that is alive, append its description
            if cm.game_places[cm.game_location]["enemy"] is not None:
                location_enemy = cm.game_places[cm.game_location]["enemy"].lower()

                # Check if enemy is defeated
                if not com.game_enemies[location_enemy]["defeated"]:
                    text_list.append("\n\n")
                    text_list.append(textwrap.fill(com.game_enemies[location_enemy]["description"], 30))

            # Append the locations directions
            text_list.append("\n\n")
            text_list.append(cm.game_places[cm.game_location]["story_directions"])

        # Appends all the items in the players inventory
        case "inventory":
            text_list.append("Inventory:\n")
            for item in im.game_items:
                if im.game_items[item]["acquired"]:
                    text_list.append(im.game_items[item]["name"])
                    text_list.append("\n")
                    text_list.append(textwrap.fill(im.game_items[item]["description"], 30))
                    text_list.append("\n\n")

        # Appends all the players equipped items
        case "equipment":
            text_list.append("Equipped:\n")
            for item in im.game_items:
                if im.game_items[item]["equipped"]:
                    text_list.append(im.game_items[item]["name"])
                    text_list.append("\n\n")

        # Appends the story text of the current location
        case "story":
            # Append the story text
            text_list.append(textwrap.fill(cm.game_places[cm.game_location]["story"], 30))

            # If there is an enemy that is alive, append its description
            if cm.game_places[cm.game_location]["enemy"] is not None:
                location_enemy = cm.game_places[cm.game_location]["enemy"].lower()

                # Check if enemy is defeated
                if not com.game_enemies[location_enemy]["defeated"]:
                    text_list.append("\n\n")
                    text_list.append(textwrap.fill(com.game_enemies[location_enemy]["description"], 30))

            # Append the locations directions regardless of above
            text_list.append("\n\n")
            text_list.append(cm.game_places[cm.game_location]["story_directions"])

        # Intentionally blank
        case "game over":
            pass

        # Display all possible commands
        case "help":

            text_list.append("Exploration:\n")
            for token in tkn.explore_tokens:
                text_list.append("     "+token)
                text_list.append("\n")
            text_list.append("\n")

            text_list.append("Inventory:\n")
            for token in tkn.inventory_tokens:
                text_list.append("     "+token)
                text_list.append("\n")
            text_list.append("\n")

            text_list.append("Status:\n")
            for token in tkn.status_tokens:
                text_list.append("     "+token)
                text_list.append("\n")
            text_list.append("\n")

            text_list.append("Combat:\n")
            for token in tkn.combat_tokens:
                text_list.append("     "+token)
                text_list.append("\n")

    # Join and return all the text
    return "".join(text_list)


# If this is the file being run
if __name__ == "__main__":
    raise Exception("This file should not be run directly.")
