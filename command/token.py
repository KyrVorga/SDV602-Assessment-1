_explore_tokens = {
    "inventory",
    "engage",
    "search",
    "north",
    "east",
    "south",
    "west",
    "down",
    "up",
    "location",
    "equipment",
    "back",
    "actions",
    # "discard",
    "equip",
    "unequip",
    "use"
}

_combat_tokens = {
    "attack",
    "block",
    "heal",
    "potion",
    "magic",
    "run"
}


def validate_list(input_string, game_state):
    result = []

    match game_state:
        case "explore":
            string_list = [
                x.lower() for x in input_string.split()
            ]
            print(string_list)
            if string_list[0] in _explore_tokens:
                result = string_list

        case "combat":
            if input_string.lower() in _combat_tokens:
                result.append(input_string.lower())

        case _:
            return tuple(('Error', 'Provided commands did not match valid tokens for state'))
    if len(result) == 0:
        return tuple(('Error', 'Provided commands did not match valid tokens for state'))
    return result
