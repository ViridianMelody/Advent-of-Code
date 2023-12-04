from aocd import data

#I had wayyyy more trouble with this than I should have. This code is a disaster...

def parseInput(inputStr):
    rows = inputStr.split("\n")
    symbols = set()
    nums = []
    gears = []
    for i,row in enumerate(rows):
        numIndex = None
        num = False
        for j, char in enumerate(row):
            if num and not char.isdigit():
                nums.append((i,numIndex,j))
                num = False
            elif not num and char.isdigit():
                numIndex = j
                num = True
            if char == "*":
                gears.append((i,j))
            if not char.isdigit() and char != ".":
                print(char)
                symbols.add((i,j))
                num=False
        if num:
            nums.append((i,numIndex,j+1))
    return symbols, nums, gears
            
def findAdjacentSymbols(numIndices, symbols):
    xRange = range(numIndices[1]-1, numIndices[2]+1)
    yRange = range(numIndices[0]-1, numIndices[0]+2)
    for x in xRange:
        for y in yRange:
            if (y,x) in symbols: return True
    return False

def solvePart2(gears,nums,dataStr=data):
    result = 0
    rows = dataStr.split('\n')
    for gear in gears:
        adjacentNums = []
        y = gear[0]
        x = gear[1]
        i = y-1
        j = x-1
        while y-1 <= i <= y+1 and 0<=i<len(rows):
            newNum = None
            j = x-1
            while x-1 <= j <= x+1 and 0<=j<len(rows[i]):
                if rows[i][j].isdigit():
                    newNum = getNumIndices(i,j)
                elif newNum:
                    adjacentNums.append(newNum)
                    newNum = None
                j += 1
            if newNum:
                adjacentNums.append(newNum)
            i += 1
        print(f"{gear}:{adjacentNums}")
        if len(adjacentNums) == 2:
            result += adjacentNums[0] * adjacentNums[1]
    return result


def getNumIndices(y,x,dataStr=data):
    rows = dataStr.split("\n")
    left = x
    right = x
    while  0<=left<len(rows[y]) and rows[y][left].isdigit():
        left -= 1
    while 0<=right<len(rows[y]) and rows[y][right].isdigit():
        right += 1
    return int(rows[y][left+1:right])
    

def getValidIds(nums,symbols,dataStr=data):
    result = []
    rows = dataStr.split("\n")
    for num in nums:
        if findAdjacentSymbols(num,symbols):
            validID = int(rows[num[0]][num[1]:num[2]])
            result.append(validID)
    return result

def main():
    symbols,nums,gears = parseInput(data)
    validIDs = getValidIds(nums,symbols)
    print(validIDs)
    print(sum(validIDs))
    gears = solvePart2(gears,nums)
    print(gears)


if __name__ == "__main__":
    main()