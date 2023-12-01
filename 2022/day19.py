from aocd import data

class Bots:
    def __init__(self):
        self.bp = [
            (4,0,0,0),
            (2,0,0,0),
            (3,14,0,0),
            (2,0,7,0)
        ]

    def step(self, time, rocks, bots):
        for i in range(4):
            rocks[i] += bots[i]
        if time <= 1:
            return rocks[3]
        highScore = self.step(time-1,rocks,bots)
        for i in range(4):
            if bots[i] >= max([x[i] for x in self.bp]) and i != 3:
                continue
            balance = self.pay(self.bp[i],rocks)
            if balance:
                print(balance)
                newBots = bots.copy()
                newBots[i] += 1
                highScore = max(highScore, self.step(time-1,balance,newBots))
        return highScore

        
    def pay(self, cost, rocks):
        result = []
        for i in range(4):
            balance = rocks[i]-cost[i]
            if balance < 0:
                return False
            result.append(balance)
        return result

    


def main():
    bots = Bots()
    print(bots.step(16,[0,0,0,0],[1,0,0,0]))

if __name__ == "__main__":
    main()