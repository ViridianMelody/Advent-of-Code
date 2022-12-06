def findStart(s,length):
    i = 0
    subString = s[0:length]
    while len(set(subString)) != length:
        i += 1
        subString = s[i:i+length]
    return i+length


def main():
    path = "Day6Input.txt"
    inputFile = open(path, "r")
    inputStr = inputFile.read()
    inputFile.close()
    print(findStart(inputStr,4))
    print(findStart(inputStr,14))

if __name__ == "__main__":
    main()