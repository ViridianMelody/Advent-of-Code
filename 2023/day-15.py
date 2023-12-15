from aocd import data

# Definitely far more code than necessary, but it works!

def hashOne(step):
    result = 0
    for char in step:
        result += ord(char)
        result *= 17
        result %= 256
    return result

def solvePart1(inputStr=data):
    steps = inputStr.split(',')
    result = 0
    for step in steps:
        result += hashOne(step)
    print(result)

def solvePart2(inputStr=data):
    steps = inputStr.split(',')
    boxes = {}
    for step in steps:
        if "=" in step:
            addLens(step,boxes)
        else:
            removeLens(step[:-1],boxes)
    print(fPower(boxes))

def addLens(step, boxes):
    lensID,fLength = step.split('=')
    fLength = int(fLength)
    box = hashOne(lensID)
    if box in boxes:
        for i,lens in enumerate(boxes[box]):
            if lens[0] == lensID:
                boxes[box][i] = (lensID, fLength)
                break
        else:
            boxes[box].append((lensID, fLength))
    else:
        boxes[box] = [(lensID,fLength)]

def removeLens(lensID,boxes):
    box = hashOne(lensID)
    if box in boxes:
        for i,lens in enumerate(boxes[box]):
            if lens[0] == lensID:
                boxes[box].pop(i)
                break

def fPower(boxes):
    result = 0
    for key, box in boxes.items():
        for slot, lens in enumerate(box):
            result += (key+1) * (slot+1) * lens[1]
    return result


def main():
    solvePart1()
    solvePart2()

if __name__ == "__main__":
    main()