#this formatter should convert "235 + 52" to if show_answers is false
#and it should add the answer if show_answer is true
#  235              235
# + 52      or     + 52
# ----             ----
#                   287
def arithmetic_arranger(problems, show_answers = False):
    #The limit of how many problem can be submitted as once will be 5
    solved = ''
    solution
    dashes = ''
    firstline = []
    secondline = ['\n']
    thirdline = ['\n']
    fourthline = ['\n']
    if len(problems) < 5:
        for problem in problems:
            val = 0
            num1 = ''
            num2 = ''
            operator = ''
            for char in problem:
                if char == ' ':
                    val+=1
                else:
                    if val == 0:
                        num1+=char
                    elif val == 1:
                        operator = char
                    elif val == 2:
                        num2+=char
            if (len(num1) > 4 | len(num2) > 4):
                ValueError("Error: Numbers cannot be more than four digits.")
            elif not num1.isnumeric():
                ValueError("Error: Numbers must only contain digits.")
            elif not num2.isnumeric():
                ValueError("Error: Numbers must only contain digits.")
            elif not (operator == '+' or operator == '-'):
                ValueError("Error: Operator must be '+' or '-'.")
            maxdifference = abs(len(num1)-len(num2))
            if operator == '+':
                solution = int(num1) + int(num2)
            elif operator == '-':
                solution = int(num1) - int(num2)
            if len(num1) > len(num2):
                for _ in maxdifference:
                    num2 = ' ' + num2
                for _ in len(num1) + 2:
                    dashes = '-' + dashes 
                for _ in len(num1) + 2 - len(solution):
                    solution = ' ' + solution
            elif len(num2) > len(num1):
                for _ in maxdifference:
                    num1 = ' ' + num1
                for _ in len(num2) + 2:
                    dashes = '-' + dashes 
            firstline.append('  ' + num1)
            secondline.append(operator + ' ' + num2)
            thirdline.append(dashes)
            fourthline.append(solution)


    else:
        ValueError("Error: Too many problems.")
    if show_answers:
        solved = '    '.join(firstline) + '    '.join(secondline) + '    '.join(thirdline) + '    '.join(fourthline)
        return solved
    else:
        solved = '    '.join(firstline) + '    '.join(secondline) + '    '.join(thirdline)
        return solved


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))