import combat.combat_manager as com

game_items = {
    "wooden staff": {
        "name": "Wooden Staff",
        "source": "Elmbrook Village",
        "description": "A simple wooden staff. Can be used for attacking.",
        "found_text": "You were given the staff by the wise old sage of Elmbrook Village.",
        "equippable": True,
        "equipped": False,
        "acquired": False,
        "usable": False,
        "used": False,
        "toggle_equip": lambda item: (
            item.update({"equipped": True if item["equipped"] is False else False})
        ),
        "equip_effect": lambda player, action: (
            player["stats"].update({"attack": player["stats"]["attack"] + (4 if action == "equip" else -4)})
        )
    },
    "enchanted armour": {
        "name": "Enchanted Armour",
        "source": "Crystal Cave",
        "description": "enhances your defence against adversaries.",
        "found_text": "You found the Enchanted Armour within the cave.",
        "equippable": True,
        "equipped": False,
        "acquired": False,
        "usable": False,
        "used": False,
        "toggle_equip": lambda item: (
            item.update({"equipped": True if item["equipped"] is False else False})
        ),
        "equip_effect": lambda player, action: (
            player["stats"].update({
                "health": player["stats"]["health"] + (25 if action == "equip" else -25),
                "max_health": player["stats"]["max_health"] + (25 if action == "equip" else -25)
            })
        )
    },
    "magical pendant": {
        "name": "Magical Pendant",
        "source": "Whispering Willows",
        "description": "increases your magical powers allowing you to cast spells with your staff.",
        "found_text": "You found a Magical Pendant by a tombstone.",
        "equippable": True,
        "equipped": False,
        "acquired": False,
        "usable": False,
        "used": False,
        "toggle_equip": lambda item: (
            item.update({"equipped": True if item["equipped"] is False else False})
        ),
        "equip_effect": lambda player, action: (
            player["stats"].update({"attack": player["stats"]["attack"] + (5 if action == "equip" else -5)})
        )
    },
    "invincibility potion": {
        "name": "Invincibility Potion",
        "source": "Cloudcrest Peaks",
        "description": "Grants you temporary invincibility during a battle.",
        "found_text": "You found an invincibility potion at the summit",
        "equippable": False,
        "equipped": False,
        "acquired": False,
        "usable": True,
        "used": False,
        "effect_active": False
    },
    "ancient scroll": {
        "name": "Ancient Scroll",
        "source": "Forsaken Wastes",
        "description": "Teaches you ancient combat techniques, increasing your attack power.",
        "found_text": "You found an Ancient scroll buried within the sand.",
        "equippable": False,
        "equipped": False,
        "acquired": False,
        "usable": True,
        "used": False,
        "use_item": lambda item: (
            item.update({"used": True})
        ),
        "use_effect": lambda player: (
            player["stats"].update({"attack": player["stats"]["attack"] + 5})
        )
    },
    "vial of healing water": {
        "name": "Vial of Healing Water",
        "source": "Guardian Serpent",
        "description": "Fully restores your health in combat.",
        "found_text": "You defeated the Guardian Serpent and claimed the Vial.",
        "equippable": False,
        "equipped": False,
        "acquired": False,
        "usable": True,
        "used": False,
        "use_item": lambda item: (
            item.update({"used": True})
        ),
        "use_effect": lambda player: (
            player["stats"].update({"health": player["stats"]["max_health"]})
        )
    },
    "inner sanctum key": {
        "name": "Inner Sanctum Key",
        "source": "Shadowcrypt",
        "description": "Allows access into the Inner Sanctum",
        "found_text": "You located the key to the Inner Sanctum.",
        "equippable": False,
        "equipped": False,
        "acquired": False,
        "usable": False,
        "used": False,
    },
    "jaldabaoth's staff": {
        "name": "Jaldabaoth's Staff",
        "source": "Great Mage Jaldabaoth",
        "description": "You defeated the Great Mage Jaldabaoth and claimed his staff!",
        "found_text": "You defeated the Great Mage Jaldabaoth and claimed his staff!",
        "equippable": True,
        "equipped": False,
        "acquired": False,
        "usable": False,
        "used": False,
        "toggle_equip": lambda item: (
            item.update({"equipped": True if item["equipped"] is False else False})
        ),
        "equip_effect": lambda player, action: (
            player["stats"].update({"attack": player["stats"]["attack"] + (15 if action == "equip" else -15)})
        )
    },
}


def equip_action(action: str, item: str):
    """
    Invokes the respective lambda from item based on action
    :param action: The action command to be performed
    :param item: The item to invoke from
    :return: A tuple containing a message to display on the window
    """
    # if the item is not acquired or unequippable return a message
    if not game_items[item]["acquired"]:
        return tuple(("Message", "You don't have this item."))

    elif not game_items[item]["equippable"]:
        return tuple(("Message", "You can't equip this item."))

    else:
        # if item's equipped state and the action are the same return a message
        if game_items[item]["equipped"] is True and action == "equip":
            return tuple(("Message", "You can't perform this action."))

        elif game_items[item]["equipped"] is False and action == "unequip":
            return tuple(("Message", "You can't perform this action."))

        else:
            # invoke both item lambdas that hold the equip logic
            game_items[item]["equip_effect"](com.player, action)
            game_items[item]["toggle_equip"](game_items[item])

            message = "You equipped the " + game_items[item]["name"]
            print(com.player)
            return tuple(("Message", message))


def use_action(item: str):
    """
    Handles using items.
    :param item: The item to invoke from
    :return: A tuple containing a message to display on the window
    """
    # if the item is not acquired or unusable return a message
    if not game_items[item]["acquired"]:
        return tuple(("Message", "You don't have this item."))

    elif not game_items[item]["usable"]:
        return tuple(("Message", "You cannot use this item like this."))

    elif game_items[item]["used"]:
        return tuple(("Message", "You already used this item."))

    else:
        # invoke both item lambdas that hold the use logic
        game_items[item]["use_effect"](com.player)
        game_items[item]["use_item"](game_items[item])

        message = "You used the " + game_items[item]["name"]
        return tuple(("Message", message))


def inventory_game_play(action, item_name):
    """
    Handles inventory commands received from command manager
    :param action: The inventory command
    :param item_name: The item to manipulate
    :return: A tuple containing a message to display on the window
    """
    # check if item_name is valid
    if item_name not in game_items:
        return tuple(("Error", "That is not a valid item."))

    match action:
        case "equip":
            return equip_action(action, item_name)

        case "unequip":
            return equip_action(action, item_name)

        case "use":
            return use_action(item_name)
