"""
This is the combat manager for Shadowcrypt, it holds the player and enemy stats, and handle combat interactions.
"""

import command.command_manager as cm
import inventory.inventory_manager as im
import status.status_manager as sts

# all the games enemies, and their stats and information
game_enemies = {
    "guardian serpent": {
        "name": "Guardian Serpent",
        "health": 10,
        # subtracts damage from entity's health
        "take_damage": lambda entity, damage: (
            entity.update({"health": entity["health"] - damage})
        ),
        "attack": 1000,
        "reward": "Vial of Healing Water",
        "location": "azure lake",
        "defeated": False,
        "description": "The Guardian Serpent circles the Azure Lake, should you approach it will defend the lake.",
        "death_message": "You defeated the Guardian Serpent and claimed the Vial."
    },
    "great mage jaldabaoth": {
        "name": "Great Mage Jaldabaoth",
        "health": 100,
        # subtracts damage from entity's health
        "take_damage": lambda entity, damage: (
            entity.update({"health": entity["health"] - damage})
        ),
        "attack": 10,
        "location": "inner sanctum",
        "reward": "Jaldabaoth's Staff",
        "defeated": False,
        "description": "The great mage Jaldabaoth stands impatiently before you, waiting for you to take the first "
                       "strike..",
        "death_message": "You defeated the Great Mage Jaldabaoth and claimed his staff!\nYou should return to Elmbrook "
                         "Village"
    },
}

player = {
    "actions": [
        "attack\n",
        "run\n"
    ],
    "stats": {
        "max_health": 25,
        "health": 25,
        "attack": 1
    },
    # sets the player's stat to value. Used by inventory
    "set_stat": lambda stats, stat, value: (
        stats.update({stat: stats[stat] + value})
    ),
    # subtracts damage from player's health
    "take_damage": lambda stats, damage: (
        stats.update({"health": stats["health"] - damage})
    ),
    "death_message": "You died... Elmbrook Village is doomed."
}


def combat_game_play(action: str):
    """
    The main combat manager that handles combat commands.
    :param action: The combat action to be performed
    :return: text to display on the window or a tuple message
    """
    # get the enemy and their name based on current location
    enemy_name = cm.game_places[cm.game_location]["enemy"].lower()
    enemy = game_enemies[enemy_name]

    # check if player is dead
    if player["stats"]["health"] <= 0:
        return tuple(("Message", "You are dead... Dead things can't do much..."))

    # otherwise player is still alive , continue as normal
    match action:
        # escape from combat, set games state to explore
        case "run":
            cm.game_state = "explore"
            return cm.show_current_place()

        # attack the enemy
        case "attack":
            enemy["take_damage"](enemy, player["stats"]["attack"])

            # if the invincibility potion is not active, player takes damage
            if not im.game_items["invincibility potion"]["effect_active"]:
                player["take_damage"](player["stats"], enemy["attack"])

            # if it was active set the effect_active to false
            else:
                im.game_items["invincibility potion"]["effect_active"] = False

            # if player died from the attack, show death message
            if player["stats"]["health"] <= 0:
                return sts.show_status_text("game over", player["death_message"])

            # if the enemy died from that attack
            elif enemy["health"] <= 0:
                cm.game_state = "explore"
                # find the item that belongs to the enemy and give it to the player
                for item in im.game_items:
                    if im.game_items[item]["source"].lower() == enemy_name:
                        im.game_items[item]["acquired"] = True
                    game_enemies[enemy_name]["defeated"] = True
                # return story text, with victory message / enemy death message
                return sts.show_status_text("story", enemy["death_message"])

            return show_combat_text(enemy_name.lower())

        # heal the player with the vial
        case "heal":
            # check if the player has the vial
            if not im.game_items["vial of healing water"]["acquired"]:
                return tuple(("Message", "You can't perform this action"))

            # check if its already been used
            else:
                if im.game_items["vial of healing water"]["used"]:
                    return tuple(("Message", "You already used this item."))

                # heal the player and set the vial to used
                else:
                    player["set_stat"](player["stats"], "health", player["stats"]["max_health"])
                    im.game_items["vial of healing water"]["use_item"]()
                    return tuple(("Message", "You restored your health."))

        # become invincible
        case "potion":
            # check if the player has the potion
            if not im.game_items["invincibility potion"]["acquired"]:
                return tuple(("Message", "You can't perform this action"))

            # check if its already been used
            else:
                if im.game_items["invincibility potion"]["used"]:
                    return tuple(("Message", "You already used this item."))

                # set the effect to active and the item to used
                else:
                    im.game_items["invincibility potion"]["use_item"]()
                    im.game_items["invincibility potion"]["effect_active"] = True
                    return tuple(("Message", "You are invincible until after your next attack."))

    return show_combat_text(enemy_name.lower())


def show_combat_text(enemy):
    """
    Shows the text for combat.
    :param enemy: the enemy to show stats for
    :return: string to display in the window
    """
    combat_list = [
        "Name: ",
        game_enemies[enemy]["name"],
        "\n",
        "Health: ",
        str(game_enemies[enemy]["health"]),
        "\n",
        "Attack: ",
        str(game_enemies[enemy]["attack"]),
        "\n",
        "Defeated: ",
        str(game_enemies[enemy]["defeated"]),
        "\n\n",
        "Player:\n",
        "Health: ",
        str(player["stats"]["health"]),
        "\n",
        "Attack: ",
        str(player["stats"]["attack"]),
        "\n\n",
        "Player Actions:\n",
        "".join(player["actions"])
    ]

    return "".join(combat_list)
