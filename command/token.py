_explore_tokens = {
    "inventory",
    "engage",
    "search",
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
    "back",
    # "discard",
    "equip",
    "unequip",
    "use"
}


def validate_list(input_string, game_state):
    result = []

    match game_state:
        case "explore":
            if input_string.lower() in _explore_tokens:
                result.append(input_string.lower())
        case "combat":
            if input_string.lower() in _combat_tokens:
                result.append(input_string.lower())

        case "inventory":
            string_list = [
                x.lower() for x in input_string.split()
            ]
            print(string_list)
            if string_list[0] in _inventory_tokens:
                result = string_list
        case _:
            return tuple(('Error', 'Provided commands did not match valid tokens for state'))
    if len(result) == 0:
        return tuple(('Error', 'Provided commands did not match valid tokens for state'))
    return result
