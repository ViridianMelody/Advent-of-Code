from aocd import data

# First intuition is to convert all the numbers to int, 
# but there's no math to do, so it's easier to just put
# the strings in a set directly and check intersection.

def parseData(inputStr=data):
    lines = data.split("\n")
    result = {}
    for line in lines:
        line = line.split(": ")
        cardID = int(line[0][5:8].strip())
        game = line[1].split("|")
        winning = set()
        myNumbers = set()
        for i in range(0,28,3):
            winning.add(game[0][i:i+2])
            print
        for i in range(1, 74, 3):
            myNumbers.add(game[1][i:i+2])
        matches = len(winning.intersection(myNumbers))
        result[cardID] = matches
    return result

def solvePart1(ticketDict):
    result = 0
    for matches in ticketDict.values():
        if matches > 0:
            result += 2**(matches-1)
    return result

def solvePart2(ticketDict):
    ticketCount = {}
    for i, matches in ticketDict.items():
        print(f"Card {i}: {matches}")
        if i in ticketCount: ticketCount[i] += 1
        else: ticketCount[i] = 1
        for j in range(1,matches+1):
            if i+j in ticketCount: ticketCount[i+j] += ticketCount[i]
            else: ticketCount[i+j] = ticketCount[i]
    return sum(ticketCount.values())

def main():
    ticketDict = parseData()
    part1Score = solvePart1(ticketDict)
    print(f"Part 1: {part1Score}")
    part2Score = solvePart2(ticketDict)
    print(f"Part 2: {part2Score}")



if __name__ == "__main__":
    main()