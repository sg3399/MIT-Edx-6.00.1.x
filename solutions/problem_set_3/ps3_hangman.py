# Hangman game
#
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

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
    number_of_guesses=8
    lettersGuessed=[]
    x=False
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+ str(len(secretWord)) + ' letters long.')
    print('-------------')

    while x==False and number_of_guesses>0:
        print('You have ' + str(number_of_guesses) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed)) 
        guessed_letter=str(input('Please guess a letter: '))
        
        if guessed_letter in lettersGuessed:
            print("Oops! You've already guessed that letter:" + getGuessedWord(secretWord, lettersGuessed))
        else: 
            lettersGuessed.append(guessed_letter) 
            if guessed_letter in secretWord:
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            else:
                print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)) 
                number_of_guesses -= 1
        print('-------------')       
        x=isWordGuessed(secretWord, lettersGuessed)
                    
    
    if isWordGuessed(secretWord, lettersGuessed)==True:
        print('Congratulations, you won!')
    elif number_of_guesses==0:
        print('Sorry, you ran out of guesses. The word was '+ secretWord +'.') 

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
