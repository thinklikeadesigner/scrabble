def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string int)
    returns: integer
    """
    add = 0
    for i in hand:
        x = hand.get(i)
        add += x
    return add


hand = {'e': 1, 'v': 2, 'n': 1, 'i': 1, 'l': 2}
print(calculateHandlen(hand))
