from enum import Enum
"""_summary_

Take string containing a proposed command produce a list of tokens
"""
_vocab_tokens = {'north', 'south', 'east', 'west', 'monster', 'fight', 'pick', 'up', 'open', 'close', 'run', 'duck',
                 'hide', 'go', 'swing', 'number', 'operator', 'name'}
_operators = {'+', '-', 'x', '/', '(', ')'}

# _white_space = set('\t', '\r', '\n', ' ')


def validate_list(input_string):
    """
    Takes a string, that is a sequence of command and operators 
    separated by "white space" characaters 
    returns a list of valid tokens - in order 

    Args:
        input_string (string): a string of characters
    """
    result = []
    for string in input_string.split():
        if string.lower() in _vocab_tokens or string in _operators:
            result.append(string)

    return result
