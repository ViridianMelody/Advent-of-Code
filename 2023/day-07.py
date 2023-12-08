from aocd import data
from collections import Counter

# I rewrote my code for part 2, and refactoring to do both made things a little weird.

cardRank = {
    "A": "14",
    "K": "13",
    "Q": "12",
    "J": "11",
    "T": "10",
    "9": "09",
    "8": "08",
    "7": "07",
    "6": "06",
    "5": "05",
    "4": "04",
    "3": "03",
    "2": "02",
    "1": "01"
}
savedRanks = {}

def parseData(inputStr=data):
    lines = inputStr.split('\n')
    hands = [x.split(' ') for x in lines]
    return hands
    
def compareHands(a,b):
    a = a[0]
    b = b[0]
    return getRank(a) > getRank(b)

def getRank(hand,joker,savedRanks):
    hand = hand[0]
    if hand in savedRanks:
        return savedRanks[hand]
    handCounts = Counter(hand)
    if 'J' in handCounts and joker:
        jokers = handCounts.pop('J')
        if len(handCounts.keys()) == 0:
            handCounts["J"] = 0
        mostCommon = handCounts.most_common(1)
        handCounts[mostCommon[0][0]] += jokers

    numUnique = len(handCounts.keys())
    rank = ''
    if numUnique == 1: rank = '7' 
    elif numUnique == 2:
        if 4 in handCounts.values(): rank = '6'
        else: rank = '5'
    elif numUnique == 3:
        if 3 in handCounts.values(): rank = '4'
        else: rank = '3'
    elif numUnique == 4: rank = '2'
    else: rank = '1'
    for card in hand:
        rank += cardRank[card]
    rank = int(rank)
    savedRanks[hand] = rank
    return rank

def calculateScore(hands):
    score = 0
    for i,hand in enumerate(hands):
        score += (i+1) * int(hand[1])
    return score


def main():
    hands = parseData()
    savedRanks = {}
    hands.sort(key=lambda x: getRank(x,False,savedRanks))
    print(calculateScore(hands))
    cardRank["J"] = "00"
    savedRanks = {}
    hands.sort(key=lambda x: getRank(x,True,savedRanks))
    print(calculateScore(hands))





if __name__ == "__main__":
    main()