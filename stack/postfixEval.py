# There are two things to note in this example. 
# First, the stack size grows, shrinks, and then grows again as the subexpressions are evaluated. 
# Second, the division operation needs to be handled carefully. 
#         Recall that the operands in the postfix expression are in their original order since postfix changes only the placement of operators. 
#         When the operands for the division are popped from the stack, they are reversed. 
#         Since division is not a commutative operator, in other words 15/515/5 is not the same as 5/155/15, we must be sure that the order of the operands is not switched.

# Assume the postfix expression is a string of tokens delimited by spaces. 
# The operators are *, /, +, and - and the operands are assumed to be single-digit integer values. The output will be an integer result.

# 1. Create an empty stack called operandStack.
# 2. Convert the string to a list by using the string method split.
# 3. Scan the token list from left to right.
#    a. If the token is an operand, convert it from a string to an integer and push the value onto the operandStack.
#    b. If the token is an operator, *, /, +, or -, it will need two operands. Pop the operandStack twice. The first pop is the second operand and the second pop is the first operand. Perform the arithmetic operation. Push the result back on the operandStack.
# 4. When the input expression has been completely processed, the result is on the stack. Pop the operandStack and return the value.

from pythonds.basic.stack import Stack

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))
