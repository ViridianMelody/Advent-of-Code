def parseInput(inputStr):
    elfPairs = inputStr.split("\n")
    elfPairs = [x.split(",") for x in elfPairs]
    elfPairs = [[x[0].split("-"),x[1].split("-")]for x in elfPairs]
    return elfPairs

def splitPair(pair):
    elf1 = [int(x) for x in pair[0]]
    elf2 = [int(x) for x in pair[1]]
    return elf1,elf2


def checkPair1(elf1,elf2):
    if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
        return 1
    elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
        return 1
    return 0

def checkPair2(elf1,elf2):
    for x in elf1:
        if elf2[0] <= x <= elf2[1]:
            return 1
    for x in elf2:
        if elf1[0] <= x <= elf1[1]:
            return 1
    return 0


def solve(elfPairs):
    result1 = 0
    result2 = 0
    for pair in elfPairs:
        elf1,elf2 = splitPair(pair)
        result1 += checkPair1(elf1,elf2)
        result2 += checkPair2(elf1,elf2)
    return result1,result2

def main():
    path = "Day4Input.txt"
    inputFile = open(path, "r")
    inputStr = inputFile.read()
    elfPairs = parseInput(inputStr)
    result1,result2 = solve(elfPairs)
    print(result1)
    print(result2)

if __name__ == "__main__":
    main()