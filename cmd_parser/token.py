from enum import Enum
"""_summary_

Take string containing a proposed command produce a list of tokens
"""
_vocab_tokens = set(['north', 'south', 'east', 'west', 'monster', 'fight', 'pick', 'up',
                    'open', 'close', 'run', 'duck', 'hide', 'go', 'swing', 'number', 'operator', 'name'])
_operators = set(['+', '-', 'x', '/', '(', ')'])

# _white_space = set('\t', '\r', '\n', ' ')


def valid_list(p_input_string):
    """
    Takes a string, that is a sequence of command and operators 
    separated by "white space" characaters 
    returns a list of valid tokens - in order 

    Args:
        p_input_string (string): a string of characters 
    """
    result = []
    for astring in p_input_string.split():
        if astring.lower() in _vocab_tokens or astring in _operators:
            result += [astring]

    return result
