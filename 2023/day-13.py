from aocd import data
from time import perf_counter
# Surprisingly easy after the nightmare of day 12.
# Excessively optimized it to under a millisecond.

def findMirrors(zone:str):
    rows = zone.split("\n")
    lenRows = len(rows)
    for i in range(1,lenRows):
        j = 0
        smudge = 0
        while i > j and i+j <lenRows:
            if smudge > 1: break
            if rows[i-j-1] != rows[i+j]:
                left = rows[i-j-1]
                right = rows[i+j]
                for k in range(len(left)):
                    if left[k] != right[k]:
                        if smudge: 
                            smudge = 2
                            break
                        smudge = 1
            j += 1
        else:
            if smudge == 1: 
                return i
            

def solve():
    zones = data.split("\n\n")
    result = 0
    for zone in zones:
        hMirrors = findMirrors(zone)
        if hMirrors: 
            result += hMirrors*100
            continue
        zone = "\n".join(["".join(x) for x in zip(*zone.split("\n"))])
        vMirrors = findMirrors(zone)
        result += vMirrors
    return result

def main():
    start = perf_counter()
    result = solve()
    end = perf_counter()
    print(end-start)
    print(f"{result}")


if __name__ == "__main__":
    main()