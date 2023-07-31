_explore_tokens = {
    "inventory",
    "north",
    "east",
    "south",
    "west",
    "down",
    "up"
}

_combat_tokens = {
    "attack",
    "block",
    "heal",
    "potion",
    "magic",
    "run"
}

_inventory_tokens = {
    "close",
    # "discard",
    "equip",
    "unequip",
    "use"
}


def validate_list(input_string, game_state):
    result = []

    match game_state:
        case "explore":
            for string in input_string.split():
                if string.lower() in _explore_tokens:
                    result.append(string.lower())
        case "combat":
            for string in input_string.split():
                if string.lower() in _combat_tokens:
                    result.append(string.lower())

        case "inventory":
            for string in input_string.split():
                if string.lower() in _inventory_tokens:
                    result.append(string.lower())
        case _:
            return Exception("Provided commands did not match valid tokens for state:" + game_state)
    if len(result) == 0:
        return Exception("Provided commands did not match valid tokens for state:" + game_state)
    return result
