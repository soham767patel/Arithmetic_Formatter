#this formatter should convert "235 + 52" to if show_answers is false
#and it should add the answer if show_answer is true
#  235              235
# + 52      or     + 52
# ----             ----
#                   287
def arithmetic_arranger(problems, show_answers = False):
    #The limit of how many problem can be submitted as once will be 5
    solved = ''
    firstline = []
    secondline = []
    thirdline = []
    fourthline = []
    if len(problems) < 5:
        for problem in problems:
            val = 0
            num1 = ''
            num2 = ''
            operator = ''
            dashes = ''
            solutionStr = ''
            solution = 0
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
            if (len(num1) > 4 or len(num2) > 4):
                return "Error: Numbers cannot be more than four digits."
            elif not num1.isnumeric():
                return "Error: Numbers must only contain digits."
            elif not num2.isnumeric():
                return "Error: Numbers must only contain digits."
            elif not (operator == '+' or operator == '-'):
                return "Error: Operator must be '+' or '-'."
            maxdifference = abs(len(num1)-len(num2))
            if operator == '+':
                solution = int(num1) + int(num2)
                solutionStr = str(solution)
            elif operator == '-':
                solution = int(num1) - int(num2)
                solutionStr = str(solution)
            if len(num1) > len(num2):
                for _ in range(maxdifference):
                    num2 = ' ' + num2
                for _ in range(len(num1) + 2):
                    dashes = '-' + dashes 
                for _ in range(len(num1) + 2 - len(solutionStr)):
                    solutionStr = ' ' + solutionStr
            elif len(num2) > len(num1):
                for _ in range(maxdifference):
                    num1 = ' ' + num1
                for _ in range(len(num2) + 2):
                    dashes = '-' + dashes 
                for _ in range(len(num2) + 2 - len(solutionStr)):
                    solutionStr = ' ' + solutionStr 
            else:
                for _ in range(maxdifference):
                    num1 = ' ' + num1
                for _ in range(len(num2) + 2):
                    dashes = '-' + dashes 
                for _ in range(len(num2) + 2 - len(solutionStr)):
                    solutionStr = ' ' + solutionStr 
            firstline.append('  ' + num1 + '    ')
            secondline.append(operator + ' ' + num2 + '    ')
            thirdline.append(dashes + '    ')
            fourthline.append(solutionStr + '    ')


    else:
        return "Error: Too many problems."
    first = ''.join(firstline)
    second = ''.join(secondline)
    third = ''.join(thirdline)
    fourth =  ''.join(fourthline)
    if show_answers:
        solved = first + '\n' +  second + '\n' +  third.rstrip() + '\n' + fourth.rstrip()
        return solved
    else:
        solved = first + '\n' +  second + '\n' +  third.rstrip()
        return solved

print(repr(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}'))

# expected output
print(repr('3801      123\n-    2    +  49\n------    -----'))

