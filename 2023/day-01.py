from aocd import data
import re

# I probably overcomplicated part two, but it works.

def getCalibrationValues1(lines):
    result = []
    for line in lines:
        digits = list(filter(lambda x: x.isdigit(), line))
        result.append(int(digits[0]+digits[-1]))
    return result

digitDict = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

def getCalibrationValues2(lines):
    result = 0
    firstPattern = re.compile(".*?(one|two|three|four|five|six|seven|eight|nine|\d)")
    lastPattern = re.compile(".*(one|two|three|four|five|six|seven|eight|nine|\d)")
    for line in lines:
        firstDigit = firstPattern.match(line).group(1)
        lastDigit = lastPattern.match(line).group(1)
        print(firstDigit)
        print(lastDigit)
        if firstDigit.isdigit():
            result += int(firstDigit) * 10
        else:
            result += digitDict[firstDigit]*10
        if lastDigit.isdigit():
            result += int(lastDigit)
        else:
            result += digitDict[lastDigit]
    return result




def main():
    lines = data.split("\n")
    calibrationValues = getCalibrationValues1(lines)
    print(sum(calibrationValues))
    print(getCalibrationValues2(lines))


if __name__ == "__main__":
    main()