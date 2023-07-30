from enum import Enum

"""_summary_

Take string containing a proposed command produce a list of tokens
"""
# _vocab_tokens = {'north', 'south', 'east', 'west', 'monster', 'fight', 'pick', 'up', 'open', 'close', 'run', 'duck',
#                  'hide', 'go', 'swing', 'number', 'operator', 'name'}
# _operators = {'+', '-', 'x', '/', '(', ')'}

# _white_space = set('\t', '\r', '\n', ' ')

_explore_tokens = {
    "search",
    "engage",
    "inventory",
    "elmbrook village",
    "sylvanwood forest",
    "crystal cave",
    "cloudcrest peaks",
    "whispering willows",
    "forsaken wastes",
    "azure lake",
    "shadowcrypt",
    "inner sanctum"
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
    return result
