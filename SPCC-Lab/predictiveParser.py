from tabulate import tabulate

variableList = list()
functionDict = dict()
firstDict = dict()
followDict = dict()
output = list()
parserDict = dict()
nonTerminalList = list()


def first(var):
    rules = functionDict[var].strip(' ').split('|')
    numberOfRules = len(rules)
    firstTemp = list()
    for rule in rules:
        i = 0
        # if we encouter a variable
        if ord(rule[i]) < ord('a'):
            childFirst = first(rule[0])
            firstTemp.extend(childFirst)
            if 'ε' in childFirst:
                # Then keep moving ahead
                while(i < len(rule)):
                    # if char is hit stop
                    if ord(rule[i]) >= ord('a'):
                        firstTemp.extend(rule[i])
                        i = len(rule)
                    #variable is hit
                    else:
                        childFirst = first(rule[i])
                        firstTemp.extend(childFirst)
                        if 'ε' in childFirst:
                            i += 1
                        else:
                            i = len(rule)
        else:
            firstTemp.extend(rule[0])
        firstTemp = list(set(firstTemp))
        firstTemp.sort()
        firstDict[var] = firstTemp
    return list(set(firstTemp))


def follow(var):
    # print(var)
    followTemp = list()
    if var == 'S':
        followTemp.extend('$')
    for variable, rule in functionDict.items():
        rules = rule.strip(" ").split("|")
        for r in rules:
            if var in r:
                i = r.find(var) + 1
                status = True
                while(status):
                    if i == len(r):
                        # follow(var)
                        if var == variable:  # B ->aB in this case $ has to be added
                            None
                            # followTemp.extend("$")
                        elif followDict[variable] == "":
                            followTemp.extend(follow(variable))
                        else:
                            # if follow is already calculated
                            followTemp.extend(followDict[variable])
                        status = False
                    elif ord(r[i]) >= ord('a'):
                        # char
                        followTemp.extend(r[i])
                        status = False
                    else:
                        temp = first(r[i])
                        # if first contains ε then go ahead
                        if 'ε' in temp:
                            temp.remove('ε')
                            i += 1
                        else:
                            status = False
                        followTemp.extend(temp)
    followTemp = list(set(followTemp))
    followTemp.sort()
    followDict[var] = followTemp
    return followTemp


def parser():

    # parser tree logic
    for variable, rule in functionDict.items():
        rules = rule.strip(" ").split("|")
        tempDict = dict()
        for r in rules:
            var = r[0]
            # if the first contains ε
            if(var == 'ε'):
                follow_variable = followDict[variable]
                for char in follow_variable:
                    tempDict[char] = variable + " -> " + r  # ie "ε"
            # if  first contains nonTerminal
            elif(ord(var) >= ord('a')):
                tempDict[var] = variable + " -> " + r
            # if first contains variable
            else:
                first_var = firstDict[var]
                # if first of variable contains ε
                if 'ε' in first_var:
                    first_var.remove('ε')
                    first_var.extend(followDict[var])
                for char in first_var:
                    tempDict[char] = variable + " -> " + r
        # for blank non-terminals
        for char in nonTerminalList:
            if char not in tempDict:
                tempDict[char] = '-'
        parserDict[variable] = tempDict
        # print(parserDict[variable])


numberOfVaribles = int(input("Number of Varibales: "))
for i in range(numberOfVaribles):
    variable = input("Enter Variable: ")
    rule = input("Enter rules: ")
    functionDict[variable] = rule
    firstDict[variable] = ''
    followDict[variable] = ''
    variableList.append(variable)
# print(functionDict)
print("\n-----FIRST & FOLLOW-----\n")
for i in range(numberOfVaribles):
    first(variableList[i])
for i in range(numberOfVaribles):
    follow(variableList[i])
for x, y in firstDict.items():
    string = x + " -> " + functionDict[x]
    output.append([string, y, followDict[x]])
print(tabulate(output, headers=['Production', 'First', 'Follow']))

for variables, rule in functionDict.items():
    rules = rule.strip(" ").split("|")
    for rule in rules:
        for char in rule:
            if(char not in variableList and char != 'ε'):
                nonTerminalList.append(char)
nonTerminalList = list(set(nonTerminalList))
nonTerminalList.sort()
nonTerminalList.append("$")

parser()
output.clear()
for x, y in functionDict.items():
    string = x
    tempList = list()
    tempList.append(string)
    for char in nonTerminalList:
        tempList.append(parserDict[x][char])
    # print(tempList)
    output.append(tempList)
nonTerminalList.insert(0, 'Production')

print("\n-----PARSER TABLE-----\n")
print(tabulate(output, headers=nonTerminalList))
