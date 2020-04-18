def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    add = 0
    for i in hand:
        add += hand.get(i)
    return add

hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}
print(calculateHandlen(hand))
