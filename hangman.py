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


def hangman(secretWord):
	"""
	Input: secretWord which is a string, the secret word to guess.
	Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
	Output: Whether the user won or lose in the game
	"""
	print("Welcome to the game, \"HANGMAN !!!!\"\n\n")
	print("Wishing You all the best, Guesser!!!\n")
	print("Try to guess the word, in my mind..\n")
	print("You have total 8 guesses in a game. If you find it, then you are the winner\n")
	print("And if you couldn't find the word in 8 guesses, sorry man, You lose, and You have to pay for that!!!! \n")
	print("ARE YOU READY FOR THE GAME????\n")
	print("\n\n\n")
	word_len = len(secretWord)
	print("I am thinking a word that is", word_len, " letters long.\n")
	gogame(secretWord)
def gogame(secretWord):
	guess_count = 8
	lettersGuessed = []
	op = False
	while (guess_count != 0) and op == False: 	
		op = isWordGuessed(secretWord,lettersGuessed)
		if op==True:
			print("Congratsss Mate, You won the game!!!!")
			break
		print("----------------")
		print("You have now", guess_count, " guesses left\n\n")
		availableLetters = getAvailableLetters(lettersGuessed)
		print("Available letters: ", availableLetters)
		letterGuess = input("\n\nPlease guess a letter:")
		if letterGuess in lettersGuessed:
			print("\nOops! You've already guessed that letter...")
			s2 = getGuessedWord(secretWord,lettersGuessed)
			print("\nNow the revealed word is: ",s2)
		if letterGuess not in lettersGuessed:
			lettersGuessed.append(letterGuess)
			if letterGuess in secretWord:
				print("\nThat's a good Guess, Mate!!!")
				s1 = getGuessedWord(secretWord,lettersGuessed)
				print("\nNow the revealed word is: ",s1)
			elif letterGuess not in secretWord:
				print("\nSorry, mate.. You guessed a wrong one, You lose one guess")
				guess_count -= 1
				print("\nYou have ", guess_count, "more guesses left")	
				s3 = getGuessedWord(secretWord,lettersGuessed)
				print("\nNow the revealed word is: ",s3)
		if guess_count == 0:
			print("\nSorry man, You failed!!! You ran out of guesses and you are gonna pay for that!!!!!")
			print("\nThe word in my mind was", secretWord, "...")
			break
			
def isWordGuessed(secretWord,lettersGuessed):
	"""
	Input: secretWord, which is a string and lettersGuessed which is a list
	Output: Returns True, if all the letters in secretWord are in list,
		    otherwise return False.
	"""
	flag = 0
	for letter in secretWord:
		if letter in lettersGuessed:
			flag += 1
	if flag == len(secretWord):
		return True
	else:
		return False


def getAvailableLetters(lettersGuessed):
	"""
	Input: It takes a list of guessed letters as input
		   Returns a list of small letters that are not present in the list
	"""
	tot = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	out = []
	for l in tot:
		if l not in lettersGuessed:
			out.append(l)
	s = ''.join(out)
	return s



def getGuessedWord(secretWord,lettersGuessed):
	"""
	Input: secretWord, which is a string and lettersGuessed which is a list
	Output: Returns a string that comprised of letters and underscores that            represents what letters in secretWord have been guessed so far.
	"""
	l = len(secretWord)
	out = []
	for l in range(len(secretWord)):
		i = 0
		if secretWord[l] in lettersGuessed:
			out.append(secretWord[l])
			i += 1
		else:
			out.append('_')
			i += 1
	s = ''.join(out)
	return s		
		
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
