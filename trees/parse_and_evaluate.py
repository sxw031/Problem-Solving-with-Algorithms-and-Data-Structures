# Parse trees can be used to represent real-world constructions like sentences or mathematical expressions.
# In mathematical expressions, the hierarchy of the tree helps us understand the order of evaluation for the whole expression.
# For example, take (3 + (4*5)) as the input, parse it into ['(', '3', '+', '(', '4', '*', '5' ,')',')'], as the representation of the parsed tree data structure.

## first step:
# building a parse tree is to break up the experssion string into a list of tokens.(left parentheses, operators)

## Rules:
# 1. If the current token is "(", and new node as the left child of the current node, and descend to the left child.
# 2. If the current token is [+,-,/,*], set the root value of the current node to the operator represented by the current node. And new node as the right child of the current node and descend to the right child.
# 3. If the current token is number, set the root value of the current node to the number and return to the parent.
# 4. If the current token is a ")", go to the parent of the current node.

# it is clear that we need to keep track of the current node as well as the parent of the current node. 
# we can use getLeftChild() and getLeftChild() to track the children of the node.
# how about the parent of the node? ---> use stack: 
#     Whenever we want to descend to a child of the current node, we first push the current node on the stack;
#     When we want to return to the parent of the curent node, we pop the parent off the stack


from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
pt.postorder()  #defined and explained in the next section


# take parsed the tree and return the numerical value of the expression as the output
#  - recursive algorihtm: 
# base case: check for a leaf node. Since numerical objects like integers and floating points require no further interpretation, the evaluate function can simply return the value stored in the leaf node. 
# recursive function: evaluate both left and right children of the current node.
# To put the results of the two recursive calls together, we can simply apply the operator stored in the parent node to the results returned from evaulating from children.

def evaluate(parseTree):
    # the keys are the operates; the values are the functions from python's operator module
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    # get the references to the left and the right children of the current node.
    # If both the left and right Child is none, we kown the current node is already the leaf node.
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

