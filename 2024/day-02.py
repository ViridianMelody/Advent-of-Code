from aocd import data

# Mostly brute force part 2. Only checks unsafe rows, and stops once a safe configuration is found.
# Could be made more efficient for larger rows, but the input has a maximum of 8 values per row.

def isRelativelySafe(row):
    i = 1
    if len(row) <= 2: return True
    while i < len(row):
        testRow = row[0:i-1]+row[i:]
        if isSafe( testRow ): return True
        i += 1
    testRow = row[:-1]
    return isSafe(testRow)


def isSafe(row):
    i = 1
    diff1 = row[i] - row[i-1]
    while i < len(row):
        diff = row[i] - row[i-1]
        if 1 > abs(diff) or abs(diff) > 3: return False
        elif diff1 * diff < 0: return False
        i += 1
    return True

def countSafeRows(rows, dampener=False):
    result = 0
    for row in rows:
        if isSafe(row):
            result += 1
        elif dampener and isRelativelySafe(row):
            result += 1
    return result
    
def main():
    rows = [list(map(int,row.split())) for row in data.split('\n')]
    print( countSafeRows(rows) )
    print( countSafeRows(rows, dampener=True) )


if __name__ == "__main__":
    main()