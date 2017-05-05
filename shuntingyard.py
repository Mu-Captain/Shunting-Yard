
def solvePolish(equation):
    tokens = list("")
    temp = ""
    pos = 0

    # Print the ReversePolish notation first.
    print(equation)

    # This is where we make a list from a string.
    for x in range(0,len(equation)):
        if equation[x] == " ":
            tokens.append(temp)
            temp = ""
        else:
            temp += equation[x]
    tokens.append(temp)

    # This is where we turn strings to int
    # There are precision errors, because of lack of
    # the decimal places.  But the power doesn't like
    # floats.
    for x in range(0,len(tokens)):
        if(tokens[x] == "+"):
            continue
        if(tokens[x] == "-"):
            continue
        if(tokens[x] == "*"):
            continue
        if(tokens[x] == "/"):
            continue
        if(tokens[x] == "^"):
            continue
        tokens[x]=int(tokens[x])

    # This is where we do the math for solving the problem.
    while True:
        if(1==len(tokens)):
            break
        if(tokens[pos] == "+"):
            tokens[pos-2]=tokens[pos-2]+tokens[pos-1]
            tokens.pop(pos)
            tokens.pop(pos-1)
            pos=0
        if(tokens[pos] == "-"):
            tokens[pos-2]=tokens[pos-2]-tokens[pos-1]
            tokens.pop(pos)
            tokens.pop(pos-1)
            pos=0
        if(tokens[pos] == "*"):
            tokens[pos-2]=tokens[pos-2]*tokens[pos-1]
            tokens.pop(pos)
            tokens.pop(pos-1)
            pos=0
        if(tokens[pos] == "/"):
            tokens[pos-2]=tokens[pos-2]/tokens[pos-1]
            tokens.pop(pos)
            tokens.pop(pos-1)
            pos=0
        if(tokens[pos] == "^"):
            tokens[pos-2]=tokens[pos-2]**tokens[pos-1]
            tokens.pop(pos)
            tokens.pop(pos-1)
            pos=0
        pos=pos+1

    # Print the final result!
    print(tokens[0])


def reversePolish(equation):
    tokens  = list(equation)
    operand = list("")
    operator= list("")
    pos= 0

    # This is where we check to see if they put all
    # the times signs, and if not fix it.
    # example.  2(3) should be 2*(3)
    while True:
        if(pos == len(tokens)):
            break
        if(tokens[pos] == "(" and pos != 0):
            if(tokens[pos-1] == "+" or tokens[pos-1] == "-" or tokens[pos-1] == "*" or tokens[pos-1] == "/" or tokens[pos-1] == "^" or tokens[pos-1] == "("):
                pos=pos+1
                continue
            else:
                tokens.insert(pos,"*")
        if(tokens[pos] == ")" and pos != (len(tokens)-1)):
            if(tokens[pos+1] == "+" or tokens[pos+1] == "-" or tokens[pos+1] == "*" or tokens[pos+1] == "/" or tokens[pos+1] == "^" or tokens[pos+1] == ")"):
                pos=pos+1
                continue
            else:
                tokens.insert(pos+1,"*")
        pos=pos+1

    # This is where we put everything into
    # reverse polish notation.
    while True:
        if 0==len(tokens):
            while True:
                if 0==len(operator):
                    break
                token = operator.pop()
                operand.append(" ")
                operand.append(token)
            break

        token = tokens.pop(0)
        
        if(token == "("):
            operator.append(token)
        elif(token == ")"):
            for x in range(0,len(operator)):
                if 0 != len(operator):
                    temp = operator.pop()
                    if temp == "(":
                        break
                    operand.append(" ")
                    operand.append(temp)
        elif(token == "+"):
            operand.append(" ")
            for x in range(0,len(operator)):
                if 0 != len(operator):
                    if operator[-1]=="+" or operator[-1]=="-" or operator[-1]=="*" or operator[-1]=="/" or operator[-1]=="^":
                        operand.append(operator.pop())
                        operand.append(" ")
            operator.append(token)
        elif(token == "-"):
            operand.append(" ")
            for x in range(0,len(operator)):
                if 0 != len(operator):
                    if operator[-1]=="+" or operator[-1]=="-" or operator[-1]=="*" or operator[-1]=="/" or operator[-1]=="^":
                        operand.append(operator.pop())
                        operand.append(" ")
            operator.append(token)
        elif(token == "*"):
            operand.append(" ")
            for x in range(0,len(operator)):
                if 0 != len(operator):
                    if operator[-1]=="*" or operator[-1]=="/" or operator[-1]=="^":
                        operand.append(operator.pop())
                        operand.append(" ")
            operator.append(token)
        elif(token == "/"):
            operand.append(" ")
            for x in range(0,len(operator)):
                if 0 != len(operator):
                    if operator[-1]=="*" or operator[-1]=="/" or operator[-1]=="^":
                        operand.append(operator.pop())
                        operand.append(" ")
            operator.append(token)
        elif(token == "^"):
            operand.append(" ")
            for x in range(0,len(operator)):
                if 0 != len(operator):
                    if operator[-1]=="^":
                        operand.append(operator.pop())
                        operand.append(" ")
            operator.append(token)
        else:
            operand.append(token)

    # This is pushing the list we created into
    # a string, so the next function can break it up again.
    solvePolish("".join(operand))

# This is our main loop, for our application.
while True:
    entered = raw_input("\"quit\" to quit.  What\'s your Equation?  ")
    if entered == "quit":
        break
    else:
        reversePolish(entered)