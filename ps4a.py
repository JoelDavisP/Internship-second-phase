# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#

def getWordScore(word,n):
    """
    inputs: word is a string which the user enters and n is an integer representing hand size.
    output: Score(an integer) of a word calculated after the specified methods
    """
    score = 0
    for letters in word:
        if letters in SCRABBLE_LETTER_VALUES.keys():
            score += SCRABBLE_LETTER_VALUES[letters]
    score_new = score*len(word)
    if len(word) == n:
        score_new += 50
    return score_new
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, words):
    """
    input: hand is a dictionary contains different letters as keys and their     count as values.It represent current 'hand' of the gamer. word is a 
     string which is created by the gamer when he plays the game.
    output: An updated 'hand' that used the letters in the word and reduced
     their respective counts in the dictionary.
    """
    #keys = []
    #keys = hand.keys()
    new_hand = hand.copy()
    for l in words:
        if l in new_hand.keys():
            new_hand[l] -= 1
    return new_hand

#
# Problem #3: Test word validity
def isValidWord(word, hand, wordList):
    """
    Input: 'word' is a string generated by user, hand is a dictionary contains the letters and their count in the hand of player and 
       wordList is the list of lowercase strings, which we used as a reference directory for checking a word.  
        output: Returns True if word is in the wordList and is entirely composed of letters in the hand. Otherwise, returns False.
    """
    if word not in wordList:
        return False
    else:

        for l in word:
            if l not in hand.keys():
                return False
            elif hand[l] == 0:
                return False
            elif word.count(l) > hand[l]:
                return False
    return True
#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string-> int)
    returns: integer,which is the number of letters in the list
    """
    count = 0
    for letters in hand:
        count += hand[letters]
    return count


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    hand_len = calculateHandlen(hand)
    scoreTot = 0
    print("Current Score is: ", scoreTot)
    while(hand_len!=0):
        print("Current hand length is: ", hand_len)
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
                
        # Display the hand
        print("Current hand is: ")
        displayHand(hand)
        
        # Ask user for input
        usr_inp =input("Enter word, or a \".\" to indicate that you are finished: ")
        val = isValidWord(usr_inp,hand,wordList)
        # If the input is a single period:
            # End the game (break out of the loop)
        if val == True and len(usr_inp) == hand_len:
            score1 = getWordScore(usr_inp,n)
            scoreTot += score1
            print("The word", usr_inp, "earned:",score1, "points....")
            break
        # Otherwise (the input is not a single period):
        if usr_inp != ".":

            # If the word is not valid:
            if val == False:            
                # Reject invalid word (print a message followed by a blank line)
                print("The entered word is not valid, please enter another word")
                print("-----------------------------------------")

            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score = getWordScore(usr_inp,n)
                scoreTot += score
                print("The word", usr_inp, "earned:",score, "points..", end=" ")
                print("Total Score: ", scoreTot)
                print()
                # Update the hand 
                hand = updateHand(hand,usr_inp)        
                hand_len -= len(usr_inp)
            
        if usr_inp == ".":
            print("Good bye, your total score is: ", scoreTot)
            break
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if hand_len == 0:   
        print("Run out of letters, Your Score is: ", scoreTot)
#
# Problem #5: Playing a game
wordList = loadWords()
# playHand({"l":1,"d":1,"e":2,"s":1,"o":2,"n":1},wordList,7)

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n'or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    print("Welcome to the Word game !!!")
    print("This game checks your vocabulary power and knowledge about english words")
    char = input("Please input any one letter of the following, \"n\" to play a new hand, or \"e\" to stop game........")
    while char!= "e":
        if char not in ['n','e']:
            print("Invalid input.. Try again!!!")
        if char == "n":
            l = int(input("How many letters do you want to play the game?"))
            hand = dealHand(l)
            playHand(hand,wordList,l)
            break
        else:
            break    
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
