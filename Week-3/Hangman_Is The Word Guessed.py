##### 1st Approach:

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    return set(secretWord) <= set(lettersGuessed)
    
    
    
    
##### 2nd Approach:
def isWordGuessed(secretWord, lettersGuessed):
    if secretWord=='':
        return True
    
    for c in secretWord:
        if c in lettersGuessed:
            return isWordGuessed(secretWord[1:], lettersGuessed)
        elif c not in lettersGuessed:
            return False
            
            


###### 3rd Approach:

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    res = ''
    for i in secretWord:
        if i in lettersGuessed:
            res += i
        else:
            res += "_ "
    return res




            
