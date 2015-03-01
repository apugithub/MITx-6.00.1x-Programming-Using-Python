def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    text_coded = ''
    for index in range(0, len(text)):
        text_coded += str(coder.get(text[index], text[index]))
    return text_coded
