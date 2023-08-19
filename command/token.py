"""
Input validation for command_manager.py.
"""

# Valid tokens for explore gameplay
explore_tokens = {
    "engage",
    "search",
    "north",
    "east",
    "south",
    "west",
    "down",
    "up",
}

# Valid tokens for inventory manipulation
inventory_tokens = {
    "equip",
    "unequip",
    "use"
}

# Valid tokens for combat gameplay
combat_tokens = {
    "attack",
    "heal",
    "potion",
    "run"
}

# Valid tokens for status commands
status_tokens = {
    "inventory",
    "equipment",
    "actions",
}


# Validates passed list using provided game_state and above valid token lists
def validate_list(input_string: str, game_state: str):
    """
    Validates input based on game_state
    :param input_string: A string of game commands
    :param game_state: The current game_state
    :return: A list of validated command tokens
    """
    result = []

    # combat only allows one token, but explore allows multiple due to inventory manipulation.
    match game_state:
        case "explore":
            # use list comprehension to lower() all strings
            string_list = [
                x.lower() for x in input_string.split()
            ]

            # add to result if token is a valid explore token
            if string_list[0] in explore_tokens or string_list[0] in status_tokens or string_list[
                    0] in inventory_tokens:
                result = string_list

        case "combat":
            # add to result if token is a valid combat token and apply lower()
            if input_string.lower() in combat_tokens:
                result.append(input_string.lower())

        # exists only to remove an IDE warning, the default will never be reached.
        case _:
            return tuple(('Error', 'Provided commands did not match valid tokens for state'))

    # if none of the tokens provided were valid return an error tuple.
    if len(result) == 0:
        return tuple(('Error', 'Provided commands did not match valid tokens for state'))

    # otherwise return the validated tokens
    else:
        return result
