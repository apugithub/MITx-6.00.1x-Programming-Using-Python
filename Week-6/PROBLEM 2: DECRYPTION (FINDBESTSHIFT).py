def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    max_real_words = 0
    best_shift = 0
    
    for i in range(0, 26):
        coded_text = applyShift(text, i)
        list_coded_words = coded_text.split(' ')
        n_valid_words = 0
        for word in list_coded_words:
            if isWord(wordList, word):
                n_valid_words += 1
        if n_valid_words > max_real_words:
            max_real_words = n_valid_words
            best_shift = i
    return best_shift    
        
