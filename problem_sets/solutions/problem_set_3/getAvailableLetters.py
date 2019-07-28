#Problem Set 3 Problem 3
#Author: Siddhant Gokhale

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    lowercaseletters=str(string.ascii_lowercase)
    letterslist= [""]*len(lowercaseletters)
 
    for i in range (0, len(lowercaseletters)):
        letterslist[i]=lowercaseletters[i]
        
    for i in lettersGuessed :
        letterslist.remove(i)

    remainingletters=""
    for i in letterslist:
        remainingletters += i
    return remainingletters