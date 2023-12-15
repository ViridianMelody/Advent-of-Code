from aocd import data

#Find a loop, do modular arithmatic to find billionth index.

def shiftAllNorth(mapp):
    for i,row in enumerate(mapp):
        for j,char in enumerate(row):
            if char == 'O':
                newI, newJ = shiftNorth(mapp,i,j)
                mapp[i][j] = '.'
                mapp[newI][newJ] = "O"
    return mapp


def shiftNorth(mapp, i, j):
    i -= 1
    while i >= 0:
        if mapp[i][j] != '.':
            break
        i-=1
    return i+1,j

def checkLoad(mapp):
    result = 0
    mappLen = len(mapp)
    for i,row in enumerate(mapp):
        for j,char in enumerate(row):
            if char == 'O':
                result += mappLen-i
    return result

def rotate(mapp):
    return [x[::-1] for x in list(map(list,zip(*mapp)))]

def solvePart1(inputStr=data):
    mapp = [list(x) for x in inputStr.split('\n')]
    shiftedMapp = shiftAllNorth(mapp)
    print(checkLoad(shiftedMapp))


def solvePart2(inputStr=data):
    mapp = [list(x) for x in inputStr.split('\n')]
    mappStr = "\n".join(["".join(x) for x in mapp])
    cache = {}
    i = 0
    while True:
        for j in range(4): 
            mapp = shiftAllNorth(mapp)
            mapp = rotate(mapp)
        mappStr = "\n".join(["".join(x) for x in mapp])
        i+=1
        if mappStr not in cache:
            cache[mappStr] = i
        else:
            break
    loopStart = cache[mappStr]
    loopLength = i - cache[mappStr]
    mod = (1000000000 - loopStart) % loopLength
    print(f"Loop found: {cache[mappStr]}, {i}")
    for i in range(mod):
        for j in range(4):
            mapp = shiftAllNorth(mapp)
            mapp = rotate(mapp)
    print(f"{checkLoad(mapp)}")



def main():
    solvePart1()
    solvePart2()

if __name__ == "__main__":
    main()