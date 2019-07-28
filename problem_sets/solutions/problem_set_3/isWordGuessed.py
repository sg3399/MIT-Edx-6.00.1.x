#Problem Set 3 Problem 1
#Author: Siddhant Gokhale


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    is_secretletter_in_letters_guessed=[0]*len(secretWord)
    for i in range(0,len(secretWord)):
        for j in range(0,len(lettersGuessed)):
            if secretWord[i]==lettersGuessed[j]:
                is_secretletter_in_letters_guessed[i]=1
            
    if is_secretletter_in_letters_guessed==[1]*len(secretWord):
        return True
    else:
        return False
