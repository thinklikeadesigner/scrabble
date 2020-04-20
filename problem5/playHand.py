

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt" #make sure to also grab the words.txt file from the main repository for this to work


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
            x = print(letter, end=" ")       # print all on the same line
    print()


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if word not in wordList:
        return False
    else:
        for letter in word:
            if letter not in hand:
                return False
            else:
                newHand = hand.copy()
                for letter in word:
                    if letter not in newHand:
                        return False
                    else:
                        newHand[letter] = newHand[letter] - 1
                        if newHand[letter] < 0:
                            return False
    return True


def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.
    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.
    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)
    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    add = 0
    x = 0
    mul = 0
    wordscore = 0
    for i in word:
        x = SCRABBLE_LETTER_VALUES.get(i)
        add += x
    mul = len(word) * add
    if n == len(word):
        wordscore = mul + 50
    else:
        wordscore = mul
    return wordscore


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    newHand = hand.copy()
    for letter in word:
        newHand[letter] = newHand[letter] - 1
    return newHand


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
    endGame = False  # keeps playing game until the game is over
    total = 0
    # game is over when endGame is set to true,
    # either run out of letters or user presses '.'
    while endGame == False:
        #   Current Hand:  a c i h m m z
        # 'print current hand:' inline with displayHand
        print("Current Hand:", end=' ')
        show = displayHand(hand)  # diplays the current hand
        # Enter word, or a "." to indicate that you are finished: him
        # asks for input and sets value = word
        word = input(
            'Enter word, or a "." to indicate that you are finished: ')
        if word == '.':
            print('Goodbye! Total score: ' + str(total) + ' points.')
            break
        elif isValidWord(word, hand, wordList) == True:  # check if input is valid
            wordscore = getWordScore(word, n)  # calculates word score
            total += wordscore  # calculates running total
# "him" earned 24 points. Total: 24 points
            print(word + ' earned ' + str(wordscore) +
                  ' points. Total: ' + str(total) + ' points ')
            print()
            hand = updateHand(hand, word)  # updates hand
            zeroLetters = all(value == 0 for value in hand.values())
            if zeroLetters == True:
                print('Run out of letters. Total score: ' +
                      str(total) + ' points.')
                break
            else:
                continue
        else:  # word is not valid, and game loops through again
            print('Invalid word, please try again.')
            print()
            continue


wordList = loadWords()
# playHand(({'a': 1, 'z': 1}), wordList, 2)
# playHand(({'i': 1, 'o': 1, 'q': 1}), wordList, 3)
# playHand(({'b': 1, 's': 1, 'x': 2, 'y': 1, 'z': 2}), wordList, 7)
# playHand(({'a': 2, 'e': 2, 'p': 1, 'r': 1, 't': 1}), wordList, 7)
# playHand(({'a': 2, 'e': 1, 'p': 2, 'r': 1, 'z': 1}), wordList, 7)
playHand(({'h': 1, 'i': 1, 'j': 2, 'm': 1, 'p': 1,
           'r': 1, 's': 2, 'w': 1}), wordList, 10)
