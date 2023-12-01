from aocd import data
from operator import add,mul

class KeepAway:
    def __init__(self):
        self.monkeys = []
        self.generateMonkeys()

    def generateMonkeys(self):
        monkeyStrs = data.split("\n\n")
        i = 0
        for monkeyStr in monkeyStrs:
            self.monkeys.append(Monkey(monkeyStr))
            itemLine = monkeyStr.splitlines()[1]
            itemWorries = list(map(int, itemLine.split(": ")[1].split(", ")))
            for worry in itemWorries:
                item = Item(i,worry)
                self.monkeys[-1].catchItem(item)
                i += 1

    def playRounds(self, rounds):
        for i in range(rounds):
            self.playRound()
    
    def playRound(self):
        for monkey in self.monkeys:
            thrownItems = monkey.inspectItems()
            for item in thrownItems:
                self.monkeys[item[0]].catchItem(item[1])
    
    def findMonkeyBusiness(self):
        top = [(i,m.inspections) for i,m in enumerate(self.monkeys)]
        top.sort(key=lambda x: x[1], reverse=True)
        return top[0][1]*top[1][1]

monkeymod = 9699690
class Item:
    def __init__(self,index,worry):
        self.index = index
        self.worry = worry % monkeymod
        
    def add(self, x):
        self.worry = (self.worry + x)%monkeymod
    
    def multiply(self, x):
        self.worry = (self.worry * x)%monkeymod
    
    def check(self,x):
        return self.worry%x == 0
    




class Monkey:
    def __init__(self, inputStr):
        lines = inputStr.splitlines()
        self.items = []
        self.parseOp(lines[2])
        self.test = int(lines[3].split("by ")[1])
        self.truePass = int(lines[4][-1])
        self.falsePass = int(lines[5][-1])
        self.inspections = 0

    def parseOp(self,line):
        opStrs = line.split("= ")[1].split(" ")
        self.operands = [opStrs[0],opStrs[2]]
        self.op = opStrs[1]
        
    def inspectItems(self):
        thrownItems = []
        while self.items:
            self.inspections += 1
            item = self.items.pop(0)
            if self.operands[1] == "old":
                item.multiply(item.worry)
            elif self.op == "+":
                item.add(int(self.operands[1]))
            else:
                item.multiply(int(self.operands[1]))
            if item.check(self.test):
                thrownItems.append((self.truePass,item))
            else:
                thrownItems.append((self.falsePass,item))
        return thrownItems
    
    def catchItem(self,item):
        self.items.append(item)

    def getOperands(self,currentItem):
        result = []
        for operand in self.operands:
            if operand == "old":
                result.append(currentItem)
            else:
                result.append(int(operand))
        return result


def main():
    keepAway = KeepAway()
    keepAway.playRounds(10000)
    print(keepAway.findMonkeyBusiness())
    

if __name__ == "__main__":
    main()