def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    upper_dict = {}
    lower_dict = {}
    offset = shift
    for letter in string.ascii_uppercase:
        upper_dict[letter] = string.ascii_uppercase[offset%26]
        offset += 1
         
    offset = shift
    for letter in string.ascii_lowercase:
        lower_dict[letter] = string.ascii_lowercase[offset%26]
        offset += 1 
            
    return  dict(upper_dict.items() + lower_dict.items())
