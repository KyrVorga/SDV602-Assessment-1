"""
This is the command parser for Shadowcrypt, it handles commands and movement
"""

import command.token as tkn
import inventory.inventory_manager as im
import combat.combat_manager as com
import status.status_manager as sts
import textwrap

# the current location of the player
game_location = "elmbrook village"

# the current state of the game, either explore or combat
game_state = "explore"

# all the information regarding the world
game_places = {
    "elmbrook village": {
        "story":
            "You start your adventure in Elmbrook, where you meet an old wise sage who provides you with a basic "
            "wooden staff. The sage advises you to explore the nearby locations to gather items and strength before "
            "facing the challenges ahead.",
        "story_directions":
            "North: Cloudcrest Peaks\n"
            "East: Sylvanwood Forest\n"
            "South: Forsaken Wastes\n"
            "West: Whispering Willows\n"
            "Down: Shadowcrypt",
        "directions": {
            "north": "Cloudcrest Peaks",
            "east": "Sylvanwood Forest",
            "south": "Forsaken Wastes",
            "west": "Whispering Willows",
            "down": "Shadowcrypt"
        },
        "image": "forest.png",
        "visited": False,
        "visited message": "You are in Elmbrook Village.",
        "enemy": None,
        "item": "Wooden Staff"
    },
    "sylvanwood forest": {
        "story":
            "A dense and bewitching forest lies to the east of Elmbrook. You venture into it, discovering a hidden "
            "glade with a shimmering crystal. You pick up the crystal, which allows you to cast protective spells in "
            "battle.",
        "story_directions":
            "East: Crystal Cave\n"
            "West: Elmbrook Village\n",
        "directions": {
            "east": "Crystal Cave",
            "west": "Elmbrook Village"
        },
        "image": "forest_circle.png",
        "visited": False,
        "visited message": "You are in the Sylvanwood Forest.",
        "enemy": None,
        "item": None
    },
    "crystal cave": {
        "story": "Deep within the Sylvanwood Forest, you stumble upon the Crystal Cave. Here, you find a set of "
                 "ancient armour forged from enchanted crystals. You can equip the armour, enhancing your defence "
                 "against adversaries.",
        "story_directions":
            "West: Sylvanwood Forest",
        "directions": {
            "west": "Sylvanwood Forest",
        },
        "image": "frog.png",
        "visited": False,
        "visited message": "You are in the Crystal Cave.",
        "enemy": None,
        "item": "Enchanted Armour"
    },
    "whispering willows": {
        "story": "West of Elmbrook, you encounter the eerie Whispering Willows — a haunted grove filled with "
                 "enigmatic whispers. There, you discovers a magical pendant that increases your magical powers "
                 "allowing you to cast spells with "
                 "your staff.\n",
        "story_directions":
            "East: Elmbrook Village\n",
        "directions": {
            "east": "Elmbrook Village",
        },
        "image": "frog.png",
        "visited": False,
        "visited message": "You are in the Whispering Willows.",
        "enemy": None,
        "item": "Magical Pendant"
    },
    "cloudcrest peaks": {
        "story": "To the north of Elmbrook lies the treacherous Cloudcrest Peaks. You being Climbing to the summit.\n",
        "story_directions":
            "South: Elmbrook Village\n",
        "directions": {
            "south": "Elmbrook Village",
        },
        "image": "frog.png",
        "visited": False,
        "visited message": "You are in the Cloudcrest Peaks.",
        "enemy": None,
        "item": "Invincibility Potion"
    },
    "forsaken wastes": {
        "story": "Venturing southwards, you reach the Forsaken Wastes, a vast, desolate wasteland. Amid the "
                 "scorching sands, you unearth an ancient scroll containing forgotten combat techniques that can "
                 "enhance your attack capabilities.\n",
        "story_directions":
            "North: Elmbrook Village\n"
            "South: Azure Lake\n",
        "directions": {
            "north": "Elmbrook Village",
            "south": "Azure Lake",
        },
        "image": "frog.png",
        "visited": False,
        "visited message": "You are in the Forsaken Wastes.",
        "enemy": None,
        "item": "Ancient Scroll"
    },
    "azure lake": {
        "story": "Further south, you arrive at the tranquil Azure Lake, guarded by a mythical water serpent. if you "
                 "can defeat the serpent, you may claim a vial of healing water, which fully restores your health.\n",
        "story_directions":
            "North: Forsaken Wastes.\n",
        "directions": {
            "north": "Forsaken Wastes",
        },
        "image": "frog.png",
        "visited": False,
        "visited message": "You are at the Azure Lake.",
        "enemy": "Guardian Serpent",
        "item": None
    },
    "shadowcrypt": {
        "story": "The sage back in Elmbrook told you how to enter the Shadowcrypt, the labyrinthine crypt beneath the "
                 "village, where the mage is. You've entered the Shadowcrypt in order to save the village.\n",
        "story_directions": "\n\nDown: Inner Sanctum\n"
                            "Up: Elmbrook village\n",
        "directions": {
            "down": "Inner Sanctum",
            "up": "Elmbrook village",
        },
        "image": "frog.png",
        "visited": False,
        "visited message": "You are in the Shadowcrypt.",
        "enemy": None,
        "item": "Inner Sanctum Key"
    },
    "inner sanctum": {
        "story": "After stumbling through the Shadowcrypt you finally reach the Inner Sanctum and confront the "
                 "vile mage.\n",
        "story_directions":
            "Up: Shadowcrypt",
        "directions": {
            "up": "Shadowcrypt",
        },
        "image": "frog.png",
        "visited": False,
        "visited message": "You are in the Inner Sanctum.",
        "enemy": "Great Mage Jaldabaoth",
        "item": None

    },
}


def interpret_commands(user_input: str):
    """
    Takes user input commands and decides where to send it.
    :param user_input: user input from window
    :return: Text to display or a message tuple
    """

    # validate the tokens based on game state
    tokens = tkn.validate_list(user_input, game_state)

    # if type is tuple than an error has occurred, pass to window.
    if type(tokens) is tuple:
        return tokens

    action = tokens.pop(0)

    # based on game state pass tokens to respective game_play manager
    match game_state:
        case "explore":
            if action in tkn.explore_tokens:
                result = explore_game_play(action)

            elif action in tkn.inventory_tokens:
                item_name = " ".join(tokens)
                result = im.inventory_game_play(action, item_name)

            elif action in tkn.status_tokens:
                result = sts.show_status_text(action)

        case "combat":
            result = com.combat_game_play(action)
        case _:
            result = ""
    return result


def show_current_place():
    """
    Gets the story at the game_state place
    :return: the story at the current place
    """

    global game_location
    story_list = []

    # if location is not visited, set to visited and add story text to story_list
    if not game_places[game_location]["visited"]:
        game_places[game_location]["visited"] = True
        story_list.append(textwrap.fill(game_places[game_location]["story"], 30))

    # else location has been visited, add visited text to story_list
    else:
        story_list.append(textwrap.fill(game_places[game_location]["visited message"], 30))

    # if there is an undefeated enemy at the location append its description to story_list
    if game_places[game_location]["enemy"] is not None:
        location_enemy = game_places[game_location]["enemy"].lower()

        # check if enemy is defeated
        if not com.game_enemies[location_enemy]["defeated"]:
            story_list.append("\n\n")
            story_list.append(textwrap.fill(com.game_enemies[location_enemy]["description"], 30))

    # append the locations directions regardless of above
    story_list.append("\n\n")
    story_list.append(game_places[game_location]["story_directions"])

    return "".join(story_list)


def explore_game_play(action: str):
    """
    Handles the explore gameplay
    :param action: An explore game token
    :return: Text to display on window
    """

    global game_location
    global game_state

    # if first token is a valid direction move the player there
    if action in game_places[game_location]["directions"]:
        proposed_location = game_places[game_location]["directions"][action].lower()

        # player must have a key to enter the inner sanctum
        if proposed_location == "inner sanctum" and not im.game_items["inner sanctum key"]["acquired"]:
            return tuple(("Message", "The way is locked..."))

        # if the player has jaldabaoth"s staff and goes back to the village display endgame text
        elif proposed_location == "elmbrook village" and im.game_items["jaldabaoth's staff"]["acquired"]:
            return sts.show_status_text(
                "game over",
                "You have defeated the Great Mage Jaldabaoth who has been plaguing the lands, well done great hero!"
            )

        # otherwise display normal text and update game_location
        else:
            game_location = proposed_location
            return show_current_place()

    elif action == "search":
        # check if location has an item
        if game_places[game_location]["item"] is None:
            return tuple(("Message", "You found nothing..."))

        item_name = game_places[game_location]["item"].lower()

        # check if item is acquired
        if im.game_items[item_name]["acquired"]:
            return tuple(("Message", "You found nothing..."))

        # set item to acquired and return found_text
        im.game_items[item_name]["acquired"] = True
        message = im.game_items[item_name]["found_text"]
        return tuple(("Message", message))

    elif action == "engage":
        # check if there are enemies
        if game_places[game_location]["enemy"] is None:
            return tuple(("Message", "This region has no enemies."))

        # set state to combat and return combat text
        game_state = "combat"
        return com.show_combat_text(game_places[game_location]["enemy"].lower())
