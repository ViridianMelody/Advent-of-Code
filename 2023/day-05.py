from aocd import data

#Overlapping ranges are a pain. There's definitely an easier way to do this, but the runtime is good at least.

def parseData(inputStr=data):
    sections = [[y.split(" ") for y in x.split("\n")] for x in data.split("\n\n")]
    seeds = [int(x) for x in sections[0][0][1:]]
    maps = []
    for i in range(1,len(sections)):
        newSection = [[int(y) for y in x] for x in sections[i][1:]]
        newSection = sorted(newSection, key=lambda x: x[1])
        maps.append(newSection)
    return seeds, maps

def convertPart1(nums, destMap):
    result = []
    for num in nums:
        newNum = None
        for dest in destMap:
            if dest[1] <= num < dest[1]+dest[2] :
                newNum = num + dest[0] - dest[1]
                break
        if newNum is None:
            newNum = num
        result.append(newNum)
    return result


def findAllPathsPart1(seeds, maps):
    paths = [seeds]
    for destMap in maps:
        paths.append(convertPart1(paths[-1],destMap))
    return paths

def mergeMaps(map1, map2):
    result = []
    for originalMap in map1:
        sourceMaps = [originalMap]
        while sourceMaps:
            sourceMap = sourceMaps.pop()
            for destMap in map2:
                newMap , remaining = findOverlap(sourceMap,destMap)
                if remaining:
                    sourceMaps += remaining
                if newMap:
                    result.append(newMap)
                    break
            else:
                result.append(sourceMap)
    return result

def findOverlap(map1, map2):
    min1 = map1[0]
    range1 = map1[2]
    max1 = min1 + range1
    min2 = map2[1]
    range2 = map2[2]
    max2 = min2 + range2
    middleMin = max(min1, min2)
    middleMax = min(max1, max2)
    destMin = map2[0] + (middleMin-min2)
    sourceMin = map1[1] + (middleMin-min1)
    if middleMin >= middleMax:
        return False,False
    middleRange = middleMax - middleMin
    newMap = [destMin,sourceMin,middleRange]
    remaining = []
    if middleRange < range1:
        leftRange = middleMin-min1
        rightRange = max1-middleMax
        if leftRange:
            remainingLeft = [min1, map1[1], leftRange]
            remaining.append(remainingLeft)
        if rightRange:
            offset = leftRange + middleRange
            remainingRight = [min1 + offset, map1[1]+offset,rightRange]
            remaining.append(remainingRight)
    return newMap, remaining

def mergeAllMaps(maps):
    finalMap = maps[0]
    for i in range(1,len(maps)):
        finalMap = mergeMaps(finalMap,maps[i])
    return finalMap

def solvePart2(seeds,maps):
    seedMap = []
    for i in range(0,len(seeds),2):
        seedRange = [seeds[i],seeds[i],seeds[i+1]]
        seedMap.append(seedRange)
    maps.insert(0,seedMap)
    finalMap = mergeAllMaps(maps)
    minLocation = min(finalMap, key=lambda x: x[0])
    print(minLocation)
        







def main():
    seeds,maps = parseData()
    paths = findAllPathsPart1(seeds,maps)
    print(f"Part 1: {min(paths[-1])}")
    #testMerge = mergeMaps([[0,20,50]],[[50,49,20]])
    #print(testMerge)
    solvePart2(seeds,maps)




if __name__ == "__main__":
    main()