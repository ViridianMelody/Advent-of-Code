from aocd import data

# Rustier than I realized... Still, not too bad.

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
    lists = [sorted(list(x)) for x in zip(*[[int(x) for x in row.split()] for row in data.split('\n')])]
    result = sum([abs(int(lists[1][i])-int(lists[0][i])) for i in range(len(lists[0]))])
    print(result)
    part2(lists[0],lists[1])


if __name__ == "__main__":
    main()
