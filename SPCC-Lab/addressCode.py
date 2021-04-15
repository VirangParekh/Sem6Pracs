def assignmentStatement(code):
    print('\nAddress code is: \n')
    code = code.replace(" ","")
    operators = ["+","-","/","*","%"]
    rhs = code[code.index("=")+1:]    # RHS
    
    t = "T"     
    count = 1   
    current_opr = ""
    first_var = ""
    second_var = ""
    i = 0
    while i < len(rhs):
        if rhs[i] in operators:
            current_opr=rhs[i]
        elif current_opr == "":
            first_var+=rhs[i]
        else:
            while (i<len(rhs) and rhs[i] not in operators):
                second_var+=rhs[i]
                i+=1
            print(t+"{}={}{}{}".format(count,first_var,current_opr,second_var))
            first_var=t+"{}".format(count)
            count+=1
            if i<len(rhs):
                current_opr=rhs[i]
            second_var=""
        i+=1
    print(code[:code.index("=")]+"="+first_var)
    print()
    return

def booleanStatement():

    booleanOperator = input("Enter Boolean Operators: ").strip(' ')
    statement = booleanOperator.split(' ')

    operators = list()
    index = 1
    for stats in statement:
        if(index%2==0):
            operators.append(stats)
        index += 1
    for stats in statement:
        if stats in operators:
            statement.remove(stats)

    print('\nAddress code is: \n')

    line = 100
    status = True
    output = list()
    count = 1
    #for all the statments
    for stats in statement:
        
        string = str(line) +' : if ' + stats + ' goto ' + str(line+3)
        output.append(string)
        line += 1

        string = str(line) +' : t' + str(count) + ' = 0' 
        output.append(string)
        line += 1
        
        string = str(line) +' : goto ' + str(line+2)
        output.append(string)
        line += 1

        string = str(line) +' : t' + str(count) + ' = 1' 
        output.append(string)
        count += 1
        line += 1

    count2 = 1
    #for all the booleans
    for op in operators:
        string = str(line) +' : t' + str(count) + ' = t' + str(count2) + ' ' + op + ' t' + str(count2+1)
        output.append(string)
        count += 1
        count2 += 2
        line += 1

    for line in output:
        print(line)
    print()
    return

def switchStatement():
    print("Enter Switch statement: ")
    output = list()
    code = list()
    case = list()
    line = input()
    while line != '' :
        line.strip(' ')
        if line != 'switch (ch) ' and len(line) > 3  and line != '    break; ':
            code.append(line)
            case.append(line[line.find(':')-2])
        line = input()

    for i in range(len(case)):
        string = 'if ch = ' + str(case[i]) + " goto L" + str(i+1)
        output.append(string)


    count = 1
    for line in code:
        line = line.strip(' ')
        # print(line)

        string = 'L' + str(count) + ':'
        output.append(string)

        string = 'T' + str(count) + line[line.find('='):]
        output.append(string)

        string = line[line.find(':')+2] + ' = T' +str(count)
        output.append(string)
        
        output.append("goto Last")
        count+= 1

    output.append("Last: ")

    print('Address code is: \n')
    for line in output:
        print(line)
    print()
    return

switchStatement()
booleanStatement()
assignmentStatement(input("Enter Equation: "))
