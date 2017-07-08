# balanced parentheses
# This defines a function called square that will return the square of its argument n
# Balanced parentheses means that each opening symbol has a corresponding closing symbol and the pairs of parentheses are properly nested. 

# to solve the chellenge:
# 1. the most recent opening parenthesis must match the next closing symbol
# 2. The first opening symbol processed may have to wait until the very last symbol for its match.

# Closing symbols match opening symbols in the reverse order of their appearance. -> a clue to use stack.

# The alogrithm:
# Starting with an empty stack, process the parenthesis strings from left to right. 
# If a symbol is an opening parenthesis, push it on the stack as a signal that a corresponding closing symbol needs to appear later. 
# If, on the other hand, a symbol is a closing parenthesis, pop the stack. 
# As long as it is possible to pop the stack to match every closing symbol, the parentheses remain balanced. 
# . If at any time there is no opening symbol on the stack to match a closing symbol, the string is not balanced properly. 
# At the end of the string, when all symbols have been processed, the stack should be empty. 

from pythonds.basic.stack import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(()'))


