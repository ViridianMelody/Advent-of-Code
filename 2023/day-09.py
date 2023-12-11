from aocd import data
from functools import reduce

# Misunderstood part two for far too long. 
# Thought it was the sum of all extrapolated values, 
# not just the ones at the root

def parseInput(inputStr=data):
    lines = [[int(y) for y in x.split(' ')] for x in data.split('\n')]
    return lines

def generateSequences(history):
    sequences = [history]
    while not reduce(lambda x,y: x and y == 0, sequences[-1], True):
        currentSeq = sequences[-1]
        newSeq = [currentSeq[i+1]-currentSeq[i] for i in range(len(currentSeq)-1)]
        sequences.append(newSeq)
    return sequences

def sumOfLast(sequences):
    return sum([x[-1] for x in sequences])

def solvePart1():
    lines = parseInput()
    allSequences = [generateSequences(x) for x in lines]
    answer = sum([sumOfLast(x) for x in allSequences])
    print(f'Part one solution: {answer}')

def extrapolateBackwards(sequences):
    left = 0
    revFirst = [x[0] for x in sequences[::-1]]
    for num in revFirst:
        left = num - left
    return left

def solvePart2():
    result = sum([extrapolateBackwards(generateSequences(x)) for x in parseInput()])
    print(f'Part two solution: {result}')



def main():
    solvePart1()
    solvePart2()



if __name__ == "__main__":
    main()