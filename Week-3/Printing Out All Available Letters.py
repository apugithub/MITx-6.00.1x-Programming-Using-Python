### 1st Approach:

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    res = string.ascii_lowercase
    for i in lettersGuessed:
        res = res.replace(i, '')
    return res
    


#### 2nd Approach:

def getAvailableLetters(lettersGuessed):
 s=list(string.ascii_lowercase)
 for a in lettersGuessed:
  if a in s:
   s.remove(a)
 return ''.join(str(x) for x in s)
 
 def ispresent(secretWord,g):
    x=list(secretWord)
    if g in x:
        return True
    else:
        return False
        
        


##### 3rd Approach:

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    L2 = []
    import string
    for c in string.ascii_lowercase:
        L2.append(c)
        #print L2
        
    def removeDupsBetter(L1,L2):
        L1Start = L1[:]
        for e in L1Start:
            if e in L2:
                L2.remove(e)
        return ''.join(str(e) for e in L2)
    
    return removeDupsBetter(lettersGuessed,L2)
    
    
    
