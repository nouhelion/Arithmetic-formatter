def arithmetic_arranger(problems, answer=False):
    #check the number of arithmetic problems
    #If there are too many problems supplied to the function. The limit is five.
    if len(problems) > 5:
        return "Error: Too many problems."
    #variables for problems

    first = []
    second = []
    operator = []

    #deviding the problem to see the operator and operand
    for problem in problems:
        characters = problem.split()
        first.append(characters[0])
        operator.append(characters[1])
        second.append(characters[2])

    #checking the operator
    #The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error.
    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."

    #Each number (operand) should only contain digits.
    for i in range(len(first)):
        if not (first[i].isdigit() and second[i].isdigit()):
            return "Error: Numbers must only contain digits."

    #Each operand (aka number on each side of the operator) has a max of four digits in width.
    for i in range(len(first)):
        if len(first[i]) > 4 or len(second[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    first_line = []  #first operand
    second_line = []  #second operand
    third_line = []  #line ------
    fourth_line = []  #result of the operation

    #first line
    for i in range(len(first)):
        if len(first[i]) > len(second[i]):
            first_line.append(" " * 2 + first[i])
        else:
            first_line.append(" " * (len(second[i]) - len(first[i]) + 2) +
                              first[i])

    #second line
    for i in range(len(second)):
        if len(second[i]) > len(first[i]):
            second_line.append(operator[i] + " " + second[i])
        else:
            second_line.append(operator[i] + " " *
                               (len(first[i]) - len(second[i]) + 1) +
                               second[i])

    #third line
    for i in range(len(first)):
        third_line.append("-" * (max(len(first[i]), len(second[i])) + 2))

    #fourth line
    if answer:
        for i in range(len(first)):
            if operator[i] == "+":
                ans = str(int(first[i]) + int(second[i]))
            else:
                ans = str(int(first[i]) - int(second[i]))

            if len(ans) > max(len(first[i]), len(second[i])):
                fourth_line.append(" " + ans)
            else:
                fourth_line.append(
                    " " * (max(len(first[i]), len(second[i])) - len(ans) + 2) +
                    ans)
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(
            second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(
                fourth_line)
    else:
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(
            second_line) + "\n" + "    ".join(third_line)
    return arranged_problems
