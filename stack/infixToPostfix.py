# fully parentheses: This type of expression uses one pair of parentheses for each operator. 
# The parentheses dictate the order of operations; there is no ambiguity. There is also no need to remember any precedence rules.
# 1. infix：the operator is in between the two operands that it is working on.
# 2. prefix: Prefix expression notation requires that all operators precede the two operands that they work on. 
# 3. post fix: Postfix, on the other hand, requires that its operators come after the corresponding operands。

# In order to convert an expression, no matter how complex, to either prefix or postfix notation, 
# fully parenthesize the expression using the order of operations. 
# Then move the enclosed operator to the position of either the left or the right parenthesis depending on whether you want prefix or postfix notation.

#### General Infix to Postfix Conversion
# As we process the expression, the operators have to be saved somewhere since their corresponding right operands are not seen yet. 
# Also, the order of these saved operators may need to be reversed due to their precedence. 
# This is the case with the addition and the multiplication in this example. 
# Since the addition operator comes before the multiplication operator and has lower precedence, 
# it needs to appear after the multiplication operator is used. Because of this reversal of order, 
# it makes sense to consider using a stack to keep the operators until they are needed.

# Assume the infix expression is a string of tokens delimited by spaces. 
# The operator tokens are *, /, +, and -, along with the left and right parentheses, ( and ). 
# The operand tokens are the single-character identifiers A, B, C, and so on. 
# The following steps will produce a string of tokens in postfix order.

# 1. Create an empty stack called opstack for keeping operators. Create an empty list for output.
# 2. Convert the input infix string to a list by using the string method split.
# 3. Scan the token list from left to right.
#    a. If the token is an operand, append it to the end of the output list.
#    b. If the token is a left parenthesis, push it on the opstack.
#    c. If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed. 
#       Append each operator to the end of the output list.
#    d. If the token is an operator, *, /, +, or -, push it on the opstack. 
#       However, first remove any operators already on the opstack that have higher or equal precedence and append them to the output list.
# 8. When the input expression has been completely processed, check the opstack. Any operators still on the stack can be removed and appended to the end of the output list.


from pythonds.basic.stack import Stack

def infixToPostfix(infixexpr):
	# we will use a dictionary called prec to hold the precedence values for the operators. 
	# This dictionary will map each operator to an integer that can be compared against the precedence levels of other operators (we have arbitrarily used the integers 3, 2, and 1). 
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
    	# defines the operands to be any upper-case character or digit. 
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))
print(infixToPostfix("( A + B ) * ( C + D )"))
print(infixToPostfix("( A + B ) * C"))
print(infixToPostfix("A + B * C"))
print(infixToPostfix("5 * 3 ^ ( 4 - 2 )"))
