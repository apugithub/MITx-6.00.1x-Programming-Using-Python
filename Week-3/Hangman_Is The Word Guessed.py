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
            
            
