
"""Function definition
def FunctionName(Input):
    Action  
    return Output """

#Example
def addOne(Number):
    Output = Number + 1
    return Output

Var = 0
print(Var)

Var2 = addOne(Var)
print(Var2)

Var3 = addOne(Var2)
print(Var3)

# Example 2 (Takes two inputs)
def addOneAddTwo(Number1, Number2):
    Output = Number1 + 1
    Output += Number2 + 2
