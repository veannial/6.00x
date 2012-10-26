# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    # FILL IN YOUR CODE HERE...
    count = 0
    for l in secretWord:
        if l not in lettersGuessed:
            return False
        else:
            count += 1
    if count == len(secretWord):
        return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word=''
    for l in secretWord:
        if l not in lettersGuessed:
            word = word +'_ '
        else:
            word = word + l
    return word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters = string.ascii_lowercase
    for l in lettersGuessed:
        if l in letters:
            letters = letters.replace(l,"")
    return letters
            
        

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
##    guesses = 8
##    lettersGuessed=[]
##    print "Welcome to the game, Hangman!"
##    print "I am thinking of a word that is "+ str(len(secretWord)) +" letters long."
##    print "----------"
##
##    while guesses > 0:
##        print "You have " + str(guesses) + " guesses left"
##        print "Avaliable Letters: " + getAvailableLetters(lettersGuessed)
##        guess = raw_input("Please guess a letter: ").lower()
##        if guess in lettersGuessed:
##            lettersGuessed.append(guess)
##            print "Good guess: " + getGuessedWord(secretWord,lettersGuessed)
##            print "---------"
##            if isWordGuessed == True:
##                print "Congratulations, you won!"
##                break
##        if guess in lettersGuessed:
##            print "You've already guessed that letter:" + getGuessedWord(secretWord,lettersGuessed)
##            print "----------"
##        else:
##            lettersGuessed += guess
##            print "Sorry, that letter is not in the word: " + getGuessedWord(secretWord,lettersGuessed)
##            guesses -= 1
##            print "---------"
##            if guesses == 0:
##                print "Sorry, you ran out of guesses. The word was " + secretWord
##                break

    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    print('----------------')
    guesses = 8
    lettersGuessed = []
    while guesses > 0:
        print 'You have ' + str(guesses) + ' guesses left'
        print "Avaliable Letters: " + getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter: ').lower()
        reduce = 0
        if guess in secretWord:
            if guess in lettersGuessed:
                if  secretWord == getGuessedWord(secretWord,lettersGuessed):
                    print 'Good guess: ' + getGuessedWord(secretWord,lettersGuessed)
                    print('----------------')
                    print('Congratulations, you won!')
                    return
                print 'Oops! You''ve already guessed that letter: ' + getGuessedWord(secretWord,lettersGuessed)
                print('----------------')
            if guess not in lettersGuessed:
                lettersGuessed.append(guess)
                if getGuessedWord(secretWord,lettersGuessed) == secretWord:
                    print 'Good guess: ' + getGuessedWord(secretWord,lettersGuessed)
                    print('----------------')
                    print('Congratulations, you won!')
                    return
                print 'Good guess: ' + getGuessedWord(secretWord,lettersGuessed)
                print('----------------')
        if guess not in secretWord:
            if guess in lettersGuessed:
                print 'Oops! You\'ve already guessed that letter: ' + getGuessedWord(secretWord,lettersGuessed)
                print('----------------')
            if guess not in lettersGuessed:
                lettersGuessed.append(guess)
                soFar = getGuessedWord(secretWord,lettersGuessed)
                reduce = 1
                guesses = (guesses - reduce)
                print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord,lettersGuessed)
                print('----------------')
                if guesses == 0:
                    print('Sorry, you ran out of guesses. The word was ' + secretWord)
                    return
    return


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
