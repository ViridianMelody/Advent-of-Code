from aocd import data

# Rustier than I realized... Still, not too bad.
# Relying on list comprehensions more than I should. Need to brush up on map/filter
# Rewrote things to be a bit more readable, but there's definitely simpler ways to do this.

def part2(left, right):
    i = 0
    j = 0
    result = 0
    while i<len(left) and j<len(right):
        currentValue = left[i]
        if currentValue < right[j]: i += 1
        elif currentValue == right[j]:
            result += currentValue
            j += 1
        else: j += 1
    print(result)

def main():
    rows = [list(map(int,row.split())) for row in data.split('\n')]
    lists = [sorted(list(x)) for x in zip(*rows)]
    result = sum([abs(lists[1][i]-lists[0][i]) for i in range(len(lists[0]))])
    print(result)
    part2(lists[0],lists[1])


if __name__ == "__main__":
    main()
