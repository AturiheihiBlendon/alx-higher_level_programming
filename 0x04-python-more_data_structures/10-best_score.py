#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
        
    bigest= list(a_dictionary.keys())[0]
    big = a_dictionary[bigest]
    for key, value in a_dictionary.items():
        if value > big:
            big = value
            bigest = key
    return(bigest)
