#this formatter should convert "235 + 52" to if show_answers is false
#and it should add the answer if show_answer is true
#  235              235
# + 52      or     + 52
# ----             ----
#                   287
def arithmetic_arranger(problems, show_answers = False):
    #The limit of how many problem can be submitted as once will be 5
    if problems.len() > 5:
        pass
    else:
        ValueError("Error: Too many problems.")
    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')