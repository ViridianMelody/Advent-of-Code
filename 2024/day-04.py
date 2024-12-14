from aocd import data

class wordFinder:
    def __init__(self, grid, word="XMAS"):
        self.grid = grid
        self.word = word

    def isWord(self, start, offset):
        if offset == [0,0]: return False
        indexes = []
        for i, char in enumerate(self.word):
            x = start[0] + i * offset[0]
            y = start[1] + i * offset[1]
            if x < 0 or x >= len(self.grid) or y < 0 or y >= len(self.grid): return False
            if char != self.grid[x][y]: return False
            indexes.append([x,y,self.grid[x][y]])
        print(indexes)
        return True
            
    def countWords(self):
        result = 0
        for i, row in enumerate(self.grid):
            for j, col in enumerate(self.grid):
                for y in [-1,0,1]:
                    for x in [-1,0,1]:
                        if self.isWord([i,j],[y,x]): result += 1
        return result

class xmasFinder(wordFinder):
    def __init__(self, grid, word="XMAS"):
        self.grid = grid
        self.word = word

    def isXmas(self, i, j):
        bar1 = self.grid[i+1][j+1] + self.grid[i-1][j-1]
        bar2 = self.grid[i+1][j-1] + self.grid[i-1][j+1]
        print(f"{bar1},{bar2},({i},{j})")
        # There must be a better way to check if two strings have the same characters in any order, but I'm too lazy to figure it out right now.
        return ("MS" == bar1 or "SM" == bar1) and ("MS" == bar2 or "SM" == bar2)


    def countWords(self):
        result = 0
        for i, row in enumerate(self.grid[1:-1]):
            for j, char in enumerate(row[1:-1]):
                if char == 'A' and self.isXmas(i+1,j+1): result += 1
        return result



def main():
    rows = data.split('\n')
    finder = wordFinder(rows)
    print(finder.countWords())
    finder = xmasFinder(rows)
    print(finder.countWords())



if __name__ == "__main__":
    main()
