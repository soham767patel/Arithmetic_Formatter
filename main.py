#this formatter should convert "235 + 52" to if show_answers is false
#and it should add the answer if show_answer is true
#  235              235
# + 52      or     + 52
# ----             ----
#                   287
def arithmetic_arranger(problems, show_answers = False):
    #The limit of how many problem can be submitted as once will be 5
    solved_problems = []
    if len(problems) < 5:
        for problem in problems:
            val = 0 #number of additon or subtraction signs found
            num1 = ''
            num2 = ''
            operand = ''
            for char in problem:
                if char == ' ':
                    val+=1
                else:
                    if val == 0:
                        num1+=char
                    elif val == 1:
                        operand = char
                    elif val == 2:
                        num2+=char
            #if either number is greater than four digits throw an error
            if (len(num1) > 4 | len(num2) > 4):
                ValueError("Error: Numbers cannot be more than four digits.")
            elif not num1.isnumeric():
                ValueError("Error: Numbers must only contain digits.")
            elif not num2.isnumeric():
                ValueError("Error: Numbers must only contain digits.")
            elif not (operand == '+' or operand == '-'):
                ValueError("Error: Operator must be '+' or '-'.")
            #the problem is valid
            if show_answers:
               max_len = max(len(num1), len(num1))
               if len(num1) < max_len:
                    for _ in range(max_len-len(num1)):
                        num1 = ' ' + num1
               elif len(num2) < max_len:
                    for _ in range(max_len-len(num2)):
                        num2 = ' ' + num2
               curr_problem = f'{num1}\n{operand} {num2}\n'
               solved_problems.append(curr_problem)
               dash = ''
               for _ in range(max_len+1):
                    dash = '-' + dash 
               curr_problem += dash
               solved_problems.append(curr_problem)
            else:
                
                max_len = max(len(num1), len(num2))
                if  len(num1) < max_len:
                    for _ in range(max_len-len(num1)):
                        num1 = ' ' + num1
                elif len(num2) < max_len:
                    for _ in range(max_len-len(num2)):
                        num2 = ' ' + num2
                curr_problem = f'{num1}\n{operand} {num2}\n'
                dash = ''
                for _ in range(max_len+1):
                    dash = '-' + dash 
                curr_problem += dash
                solved_problems.append(curr_problem)
    else:
        ValueError("Error: Too many problems.")
    return solved_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))