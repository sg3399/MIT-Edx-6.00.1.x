#Problem Set 3 Problem 2
#Author: Siddhant Gokhale

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    is_secretletter_in_letters_guessed=[0]*len(secretWord)
    for i in range(0,len(secretWord)):
        for j in range(0,len(lettersGuessed)):
            if secretWord[i]==lettersGuessed[j]:
                is_secretletter_in_letters_guessed[i]=1
    ans=""
    for i in range(0,len(secretWord)):
        if is_secretletter_in_letters_guessed[i]==1:
            ans=ans+secretWord[i]
        else:
            ans=ans+" _ "
    return ans  