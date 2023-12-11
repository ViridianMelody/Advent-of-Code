from aocd import data
from functools import reduce

# Relatively simple. Code's still messy anyway


def expand(universe=data):
    universe = [list(x) for x in universe.split("\n")]
    rows = set()
    for i, row in enumerate(universe):
        for char in row:
            if char == "#":
                break
        else:
            rows.add(i)
    columns = set()
    universe = list(map(list, zip(*universe)))
    for i, col in enumerate(universe):
        for char in col:
            if char == "#":
                break
        else:
            columns.add(i)
    universe = list(map(list, zip(*universe)))
    return universe, rows,columns

def catalogGalaxies(universe):
    galaxies = []
    for i,row in enumerate(universe):
        for j,char in enumerate(row):
            if char == "#":
                galaxies.append((i,j))
    return galaxies

def distanceToAllGalaxies(galaxies,rows, columns,mult):
    totalDistance = 0
    current = galaxies.pop()
    while galaxies:
        totalDistance += sum([distanceExpanded(current,x, rows,columns,mult) for x in galaxies])
        current = galaxies.pop()
    print(totalDistance)


def distance(origin,destination):
    return abs(origin[0]-destination[0]) + abs(origin[1]-destination[1])
            
def distanceExpanded(origin, destination, rows, columns, mult):
    distance = 0
    bottom = max(origin[0],destination[0])    
    top = min(origin[0],destination[0])
    for i in range(top,bottom):
        if i in rows:
            distance += mult
        else:
            distance += 1
    left = min(origin[1],destination[1]) 
    right = max(origin[1],destination[1]) 
    for i in range(left,right):
        if i in columns:
            distance += mult
        else:
            distance += 1
    
    return distance



def main():
    universe, rows, columns = expand()
    galaxies = catalogGalaxies(universe)
    mult = 2
    distanceToAllGalaxies(galaxies.copy(), rows, columns, mult)
    mult = 1000000
    distanceToAllGalaxies(galaxies.copy(), rows, columns, mult)



if __name__ == "__main__":
    main()
