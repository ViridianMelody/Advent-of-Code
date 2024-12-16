from aocd import data

# Got very lost in the weeds. This is probably a lot simpler than it seems

def passesRule(update,rule):
    page2Found = None
    for i,page in enumerate(update):
        if page2Found and page == rule[0]:
            return False
        elif page==rule[1]: page2Found = i
    return True
    
def isSorted(update, rules):
    for rule in rules:
        if not passesRule(update,rule):
            return False
    return True

def findSorted(updates, rules, invert=False):
    correct = []
    incorrect = []
    for update in updates:
        if isSorted(update,rules):
            correct.append(update)
        else:
            incorrect.append(update)
    if invert: return incorrect
    return correct

def solvePart1(updates, rules):
    result = 0
    for update in findSorted(updates, rules):
        result += int(update[len(update)//2])
    return result

class Page():
    def __init__(self, num, rules):
        self.num = num
        self.rules = rules
    def __lt__(self, other):
        visited = set()
        stack = [self.num]
        while stack:
            current = stack.pop()
            if current in visited: continue
            visited.add(current)
            if other.num in self.rules[current]: return True
            if current in self.rules:
                for page in self.rules[current]:
                    stack.append(page)
        return False
    def __repr__(self):
        return self.num

def sortPages(pages):
    for i in range(len(pages)-1):
        if 

def convertRulesDict(rules):
    ruleDict = {}
    for rule in rules:
        if rule[0] in ruleDict:
            ruleDict[rule[0]].add(rule[1])
        else:
            ruleDict[rule[0]] = {rule[1]}
    return ruleDict


def solvePart2(updates, rules):
    result = 0
    ruleDict = convertRulesDict(rules)
    incorrect = findSorted(updates, rules, invert=True)
    for update in incorrect:
        print(update)
        currentUpdate = [Page(x,ruleDict) for x in update]
        
        result += int(currentUpdate[len(currentUpdate)//2].num)
    return result


def main():
    rules,updates = data.split('\n\n')
    rules = set([tuple(row.split('|')) for row in rules.splitlines()])
    updates = [row.split(',') for row in updates.splitlines()]
    print(solvePart1(updates,rules))
    print(solvePart2(updates,rules))

if __name__ == "__main__":
    main()