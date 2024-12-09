from aocd import data

from math import prod
import re

#regex wizardry go!

def parseMul(s):
    return prod(map(int, s.strip('mul()').split(',')))

def solvePart1():
    pattern = re.compile("mul\(\d+,\d*\)")
    mulStrings = re.findall(pattern, data)
    print(sum(map(parseMul, mulStrings)))

def solvePart2():
    pattern = re.compile("mul\(\d+,\d*\)|do\(\)|don't\(\)")
    funcStrings = re.findall(pattern, data)
    active = True
    result = 0
    for s in funcStrings:
        if s == "don't()": active = False
        elif s == "do()": active = True
        elif active: result += parseMul(s)
    print(result)

def main():
    solvePart1()
    solvePart2()

if __name__ == "__main__":
    main()