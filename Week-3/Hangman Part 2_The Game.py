##### 1st Approach:

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long')
    mistakesMade = 8
    lettersGuessed = []
    while True:
        print('------------')
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('Congratulations, you won!')
            break
        if mistakesMade == 0:
            print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
            break
        print('You have ' + str(mistakesMade) + ' guesses left.');
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess = raw_input('Please guess a letter: ')
        guess = guess.lower()
        if guess in lettersGuessed:
            print('Oops! You\'ve already guessed that letter: ' + getGuessedWord(secretWord, lettersGuessed))
        elif guess in secretWord:
            lettersGuessed += [guess]
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += [guess]
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
            mistakesMade -= 1
            
            

###### 2nd Approach:

def hangman(secretWord):
    mistakesMade=0
    guessesRemaining=8-mistakesMade
    lettersGuessed=[]
    dostepneLiterki=getAvailableLetters(lettersGuessed)
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is "+ str(len(secretWord)) +" letters long.")
    print('-----------')
    
    while mistakesMade<8:
        guessesRemaining=8-mistakesMade
        print("You have "+str(8-mistakesMade)+" guesses left.")
        print("Available letters: "+str(getAvailableLetters(lettersGuessed)))
        litera= str(raw_input("Please guess a letter: "))
        guessInLowerCase = litera.lower()
    
        if guessInLowerCase in lettersGuessed:
            print("Oops! You've already guessed that letter: "+str(getGuessedWord(secretWord, lettersGuessed)))
        elif guessInLowerCase not in secretWord:
            lettersGuessed+=guessInLowerCase
            print("Oops! That letter is not in my word: "+str(getGuessedWord(secretWord, lettersGuessed)))
            mistakesMade+=1
        elif guessInLowerCase in dostepneLiterki:
            lettersGuessed+=guessInLowerCase
            print("Good guess: "+str(getGuessedWord(secretWord, lettersGuessed)))
            if '_' not in getGuessedWord(secretWord, lettersGuessed):
                break
        dostepneLiterki=getAvailableLetters(lettersGuessed)
        print('-----------')
        
    if '_' not in getGuessedWord(secretWord, lettersGuessed):
        print('-----------')
        print("Congratulations, you won!")
    elif '_' in getGuessedWord(secretWord, lettersGuessed):
        print("Sorry, you ran out of guesses. The word was "+str(secretWord))
    guessesRemaining=8-mistakesMade
    
    

################   3rd Approach:   ******( Applicable for both boxes/Answers)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
 
    Starts up an interactive game of Hangman.
 
    * At the start of the game, let the user know how many 
      letters the secretWord contains.
 
    * Ask the user to supply one guess (i.e. letter) per round.
 
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.
 
    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
 
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
 
    intro = str(len(secretWord))
    lettersGuessed = []
    guess = str
    mistakesMade = 0
    
    print 'Welcome to the game, Hangman!'
    print ('I am thinking of a word that is ') + intro + (' letters long.')
    print ('------------')
 
 
    while mistakesMade < 8:
        if isWordGuessed(secretWord,lettersGuessed):
            return ('Congratulations, you won!')
        print ('You have ') + str(8-mistakesMade) + (' guesses left.')
        print ('Available letters:') + getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter:').lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print ('Oops! You\'ve already guessed that letter:') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
            else:
                lettersGuessed.append(guess)
                print ('Good guess:') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
        else:
            if guess in lettersGuessed:
                print ('Oops! You\'ve already guessed that letter:') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
            else:
                lettersGuessed.append(guess)
                mistakesMade += 1
                print ('Oops! That letter is not in my word:') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
 
 
    return ('Sorry, you ran out of guesses. The word was ') + secretWord



