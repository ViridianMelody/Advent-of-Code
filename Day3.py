def splitPack(contents):
    half = len(contents)//2
    left = contents[:half]
    right = contents[half:]
    return left,right

def findCommonElement(left,right):
    return (set(left) & set(right)).pop()

def getScore(char):
    if char.isupper():
        return ord(char)-38
    else:
        return ord(char)-96

def solvePart1(rows):
    result = 0
    for row in rows:
        left,right = splitPack(row)
        char = findCommonElement(left,right)
        result += getScore(char)
    return result

def solvePart2(rows):
    result = 0
    while rows:
        elf1 = set(rows.pop())
        elf2 = set(rows.pop())
        elf3 = set(rows.pop())
        commonItem = (elf1 & elf2 & elf3).pop()
        result += getScore(commonItem)
    return result




def main():
    path = "Day3Input.txt"
    inputFile = open(path, "r")
    rows = inputFile.read().split("\n")
    print(solvePart1(rows))
    print(solvePart2(rows))


if __name__ == "__main__":
    main()