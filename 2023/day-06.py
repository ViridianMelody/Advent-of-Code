import cmath
from math import sqrt, ceil, floor
races = [(42,284),(68,1005),(69,1122),(85,1341)]
bigRace = (42686985,284100511221341)

# Oh hey, the quadratic formula I will never get 
# out of my head was vaguely handy!

def solvePart1():
    result = 1
    for race in races:
        maxTime = race[0]
        target = race[1]
        wins = 0
        for i in range(maxTime):
            isWin = i*(maxTime-i) > target
            if not isWin and wins:
                break
            if isWin:
                wins += 1
        result *= wins
    return result

def solvePart2():
    maxTime = - bigRace[0] #b
    target = bigRace[1] #c
    bound1 = ceil((-maxTime - sqrt((maxTime ** 2) - (4 * target)))/2)
    bound2 = floor((-maxTime + sqrt((maxTime ** 2) - (4 * target)))/2)
    print(floor(bound2)-ceil(bound1)+1)

    

def main():
    print(solvePart1())
    solvePart2()

if __name__ == "__main__":
    main()