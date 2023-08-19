"""
This is the status manager for Shadowcrypt, it displays player status information such as inventory and equipment.
"""

import inventory.inventory_manager as im
import command.command_manager as cm
import combat.combat_manager as com
import textwrap


def show_status_text(to_show: str, initial_text=None):
    text_list = []

    # if there is initial text append it to the list
    if initial_text is not None:
        text_list.append(textwrap.fill(initial_text, 30))
        text_list.append("\n\n")

    match to_show:
        # appends the text of the current location
        case "story":
            # if its the first time visiting display story text
            if not cm.game_places[cm.game_location]["visited"]:
                cm.game_places[cm.game_location]["visited"] = True
                text_list.append(textwrap.fill(cm.game_places[cm.game_location]["story"], 30))
            # other wise append the visited text
            else:
                text_list.append(textwrap.fill(cm.game_places[cm.game_location]["visited message"], 30))

            # if there is an enemy that is alive, append its description
            if "enemy" in cm.game_places[cm.game_location]:
                location_enemy = cm.game_places[cm.game_location]["enemy"].lower()
                if not com.game_enemies[location_enemy]["defeated"]:
                    text_list.append("\n\n")
                    text_list.append(textwrap.fill(com.game_enemies[location_enemy]["description"], 30))

            # append the locations directions
            text_list.append("\n\n")
            text_list.append(cm.game_places[cm.game_location]["story_directions"])

        # appends all of the items in the players inventory
        case "inventory":
            text_list.append("Inventory:\n")
            for item in im.game_items:
                if im.game_items[item]["acquired"]:
                    text_list.append(im.game_items[item]["name"])
                    text_list.append("\n")
                    text_list.append(textwrap.fill(im.game_items[item]["description"], 30))
                    text_list.append("\n\n")

        # appends all of the players equipped items
        case "equipment":
            text_list.append("Equipped:\n")
            for item in im.game_items:
                if im.game_items[item]["equipped"]:
                    text_list.append(im.game_items[item]["name"])
                    text_list.append("\n\n")

        # appends some of the players possible actions. Incomplete.
        case "actions":
            text_list.append("Actions:\nback\nequip <item>\nunequip <item>\nuse <item>")

        # incomplete
        case "game over":
            pass

        # incomplete
        case "help":
            pass

    # join and return all of the text
    return "".join(text_list)
