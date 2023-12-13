from aocd import data
from time import perf_counter

def parseInput(inputStr=data):
    result = []
    lines = inputStr.split('\n')
    for line in lines:
        line = line.split(' ')
        spaces = line[0]
        blocks = [int(x) for x in line[1].split(',')]
        result.append([spaces,blocks])
    return result

def findCombos(puzzle, part):
    if part == 1:
        spaces = puzzle[0]
        blocks = puzzle[1]
    else:
        spaces = "?".join([puzzle[0] for x in range(5)])
        blocks = puzzle[1]*5
    return recursiveSearch(spaces,blocks)

memoi = {}
def recursiveSearch(spaces:str,blocks:list):
    # Trim empty space
    for i, char in enumerate(spaces):
        if char != ".":
            spaces = spaces[i:]
            break
    else:
        spaces = ""
    spaceBlock = spaces+"-".join([str(x) for x in blocks])
    if spaceBlock in memoi:
        return memoi[spaceBlock]
    # Not enough room for blocks
    if sum(blocks) + len(blocks) - 1 > len(spaces): return 0
    # No blocks
    if not blocks:
        if "#" not in spaces:
            return 1
        else: return 0
    if len(blocks) == 1 and "." not in spaces and "#" not in spaces:
        result = len(spaces)-blocks[0]+1
        memoi[spaceBlock] = result
        return result
    # Block at start
    if spaces[0] == "#":
        # Blocked by "."
        if "." in spaces[:blocks[0]]: 
            return 0
        # Cut off space for block
        newSpaces = spaces[blocks[0]:]
        if newSpaces:
            if newSpaces[0] == "#": return 0
            newBlocks = blocks[1:]
            result = recursiveSearch(newSpaces[1:],newBlocks)
            memoi[spaceBlock] = result
            return result
        return 1
    # "?" at start
    else:
        if spaces[0] != "?": print("wtf")
        result = 0
        # Act as "."
        blocksCopy = blocks[:]
        nextSpaces = spaces[1:]
        result += recursiveSearch(nextSpaces, blocksCopy)

        # Act as "#"
        if "." not in spaces[:blocks[0]]:
            nextSpaces = spaces[blocks[0]:]
            nextBlocks = blocks[1:]
            if nextSpaces:
                if nextSpaces[0] != "#":
                    result += recursiveSearch(nextSpaces[1:], nextBlocks)
            else:
                result += recursiveSearch(nextSpaces, nextBlocks)
        memoi[spaceBlock] = result
        return result

def solve():
    puzzles = parseInput()
    result1 = 0
    result2 = 0
    for puzzle in puzzles:
        result1 += findCombos(puzzle,1)
        result2 += findCombos(puzzle,2)
    print(result1)
    print(result2)

def main():
    start = perf_counter()
    solve()
    print(perf_counter()-start)

if __name__ == "__main__":
    main()
