class RPS:
    def __init__(self):
        self.throwScores = {
            "A":1, #rock
            "B":2, #paper
            "C":3, #scissors
            "X":1, #rock
            "Y":2, #paper
            "Z":3  #scissors
        }
        self.guideOffsets = {
            "X":2,
            "Y":0,
            "Z":1
        }
        self.winScores = {
            0:3,
            1:6,
            2:0
        }
    
    def getWinScore(self, player, opp):
        diff = player - opp
        if diff < 0:
            diff += 3
        return self.winScores[diff]
    
    def getScore(self, playerStr, oppStr):
        player = self.throwScores[playerStr]
        opp = self.throwScores[oppStr]
        return player + self.getWinScore(player, opp)

    def getScore2(self, oppStr, guideStr):
        opp = self.throwScores[oppStr]
        player = (opp + self.guideOffsets[guideStr])%3
        if player == 0:
            player = 3
        return player + self.getWinScore(player,opp)

    
    def calcTotalScore(self, inputList):
        total = 0
        for row in inputList:
            total += self.getScore(row[1],row[0])
        return total

    def calcTotalScore2(self, inputList):
        total = 0
        for row in inputList:
            total += self.getScore2(row[0],row[1])
        return total

        

def parseInput(path):
    inputFile = open(path, "r")
    inputList = [x.split(" ") for x in inputFile.read().split("\n")]
    inputFile.close()
    return inputList


def main():
    inputPath = "Day2Input.txt"
    inputList = parseInput(inputPath)
    rps = RPS()
    print(rps.calcTotalScore(inputList))
    print(rps.calcTotalScore2(inputList))


if __name__ == "__main__":
    main()