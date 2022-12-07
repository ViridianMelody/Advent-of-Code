from time import sleep
from aocd import data,submit
from functools import reduce

class fileTree:
    def __init__(self):
        self.dirs = {}
        self.currentPath = ["/"]
        self.currentContents = {}
        self.dirSizes = {}

    def parseInput(self, string):
        command = string[:4]
        if command == "$ cd":
            self.changeDir(string[5:])
        elif command == "$ ls":
            pass
        elif command == "dir ":
            self.currentContents[string[4:]] = "dir"
            dirPath = "|".join(self.currentPath) + "|" + string[4:]
            if dirPath not in self.dirs:
                self.dirs[dirPath] = {}
        else:
            newFile = string.split(" ")
            self.currentContents[newFile[1]] = int(newFile[0])
    
    def changeDir(self, newDir):
        currentPathStr = "|".join(self.currentPath)
        if currentPathStr not in self.dirs:
            self.dirs[currentPathStr] = self.currentContents
        if self.currentContents:
            self.dirs[currentPathStr] = self.currentContents
        self.currentContents = {}
        if newDir == "..":
            self.currentPath.pop()
        elif newDir == "/":
            self.currentPath = ["/"]
        else:
            self.currentPath.append(newDir)

    def getDirSize(self, dirStr):
        if dirStr in self.dirSizes:
            return self.dirSizes[dirStr]
        size = 0
        dir = self.dirs[dirStr]
        for key, dirFile in dir.items():
            if dirFile == "dir":
                size += self.getDirSize(dirStr+"|"+key)
            else:
                size += dirFile
        self.dirSizes[dirStr] = size
        return size
    
    def setAllDirSizes(self):
        for dir in self.dirs.keys():
            self.getDirSize(dir)

    def sumDirSizes(self, maxSize=100000):
        self.setAllDirSizes()
        total = 0
        for key,size in self.dirSizes.items():
            if size <= 100000:
                total += size
        return total

    def findDeleteTarget(self):
        totalSpace = 70000000
        requiredSpace = 30000000
        filledSpace = self.getDirSize("/")
        minimumDelete = requiredSpace - (totalSpace - filledSpace)
        values = list(self.dirSizes.values())
        return reduce(lambda x,y: y if x>y>minimumDelete else x, values,30000000)

def main():
    filetree = fileTree()
    for row in data.splitlines():
        filetree.parseInput(row)
    part1 = filetree.sumDirSizes()
    part2 = filetree.findDeleteTarget()
    print(part2)
    submit(part2)


if __name__ == "__main__":
    main()