from aocd import data


def parseGames(inputStr):
    lines = inputStr.split("\n")
    result = []
    for line in lines:
        line = line.split(": ")
        rounds = line[1].split("; ")
        rounds = [parseDraw(x) for x in rounds]
        gameID = int(line[0].split(' ')[1])
        result.append([gameID,rounds])
    return result

def parseDraw(drawStr):
    drawList = drawStr.split(", ")
    result = [0,0,0]
    for draw in drawList:
        draw = draw.split(" ")
        if draw[1] == "red": i=0
        elif draw[1] == "green": i=1
        elif draw[1] == "blue": i=2
        else: raise ValueError
        result[i] = int(draw[0])
    return result

def getMaxInGame(game):
    rounds = game[1]
    result = [0,0,0]
    for i in range(3):
        result[i] = max(rounds,key=lambda x: x[i])[i]
    return result

def solvePart1(games, maxRGB=[12,13,14]):
    result = 0
    for game in games:
        gameMax = getMaxInGame(game)
        for i in range(3):
            if gameMax[i] > maxRGB[i]:
                break
        else:
            result += game[0]
    return result
    
def solvePart2(games):
    result = 0
    for game in games:
        gameMax = getMaxInGame(game)
        result += gameMax[0]*gameMax[1]*gameMax[2]
    return result



def main():
    games = parseGames(data)
    print(solvePart1(games))
    print(solvePart2(games))

if __name__ == "__main__":
    main()
