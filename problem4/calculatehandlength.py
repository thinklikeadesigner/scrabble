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
        print('word not in wordList')
        return False
    else:
        for letter in word:
            if letter not in hand:
                print('letter not in hand')
                return False
            else:
                newHand = hand.copy()
                for letter in word:
                    if letter not in newHand:  # this if statement is here to prevent keyError
                        print('letter not in newHand')
                        return False
                    else:
                        newHand[letter] = newHand[letter] - 1
                        if newHand[letter] < 0:
                            print('no letter left')
                            return False
    return True


wordList = ['rapture', 'quilt', 'bunny', 'tomorrow', 'raptures']
hand1 = {'r': 2, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}
hand2 = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}

# word present in wordList
# letters present in word and correct amt in hand1
print(isValidWord('rapture', hand1, wordList))
print(isValidWord('raptures', hand1, wordList))  # letter s not in hand1
# letters present in hand2, but not enough letters
print(isValidWord('raptures', hand2, wordList))
# word not present in wordList
print(isValidWord('dog', hand2, wordList))
