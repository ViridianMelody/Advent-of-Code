class Stacks:
    def __init__(self):
        self.stacks = {}

    def parseInitialState(self, inputRows):
        rows = inputRows[::-1]
        for i in range(9):
            col = 1 + i * 4
            stack = []
            for row in rows:
                if row[col] != " ":
                    stack.append(row[col])
            self.stacks[i+1] = stack
    
    def moveItems1(self,src,dest,quantity=1):
        for i in range(quantity):
            self.stacks[dest].append(self.stacks[src].pop())
    
    def moveItems2(self,src,dest,quantity=1):
        tempStack = []
        for i in range(quantity):
            tempStack.append(self.stacks[src].pop())
        while tempStack:
            self.stacks[dest].append(tempStack.pop())

    def parseStep(self,step):
        step = step.split(" ")
        quantity = int(step[1])
        src = int(step[3])
        dest = int(step[5])
        return src,dest,quantity
    
    def solvePart1(self,steps):
        for step in steps:
            src,dest,quantity = self.parseStep(step)
            self.moveItems1(src,dest,quantity)
        result = ""
        for i in range(1,10):
            result += self.stacks[i].pop()
        return result
    
    def solvePart2(self,steps):
        for step in steps:
            src,dest,quantity = self.parseStep(step)
            self.moveItems2(src,dest,quantity)
        result = ""
        for i in range(1,10):
            result += self.stacks[i].pop()
        return result


def splitFile(path):
    inputFile = open(path, "r")
    inputRows = inputFile.read().split("\n")
    initialStacks = inputRows[:8]
    moves = inputRows[10:]
    return initialStacks,moves



def main():
    path = "Day5Input.txt"
    initialStacks,moves = splitFile(path)
    stacks = Stacks()
    stacks.parseInitialState(initialStacks)
    print(stacks.solvePart1(moves))
    stacks = Stacks()
    stacks.parseInitialState(initialStacks)
    print(stacks.solvePart2(moves))

if __name__ == "__main__":
    main()