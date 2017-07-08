### Tree Traversals
# preorder: we visit the root first, then recursively do a preorder traversal of the left subtree, followed by a recursive preorder traversal of the right subtree.
# inorder: we recursively do an inorder traversal on the left subtree, visit the root node, and finally do a recursive inorder traversal of the right subtree
# postorder: we recursively do a postorder traversal of the left subtree and the right subtree followed by a visit to the root node

#################################### preorder ########################################
### Which one is better? - The Preorder external vs. internal
# An external function of preorder that takes a binary tree as a parameter. 
# It is elegant because our base case is simply to check if the tree exists, if the tree parameter is None, then the function returns without taking any action.
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

# An method of the BinaryTree Class:
def preorder(self):
    print(self.key)
    if self.leftChild:
        self.leftChild.preorder()
    if self.rightChild:
        self.rightChild.preorder()

# Since you rarely use traverse, the external function is better

#################################### postorder ########################################
# external
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

# Internal
def postordereval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()

#################################### inorder ########################################
# external
def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())

# internal
def printexp(tree):
  sVal = ""
  if tree:
      sVal = '(' + printexp(tree.getLeftChild())
      sVal = sVal + str(tree.getRootVal())
      sVal = sVal + printexp(tree.getRightChild())+')'
  return sVal




