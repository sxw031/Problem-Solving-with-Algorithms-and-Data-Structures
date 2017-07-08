### What is AVL Tree?
# A binary search tree that automatically makes sure that the tree remains balanced at all times.
# the Map ADT is the same as BST, but to impelement it, we need to keep track of a balance factor for each node in the tree.
# balanceFactor(BF) = height(leftSubTree) - height(rightSubTree)
# BF > 0: left-heavy
# BF < 0: right-heavy
# BF = 0: perfectly balanced
# If BF = 1, 0 or -1: tree is balanced
# Once the tree is unbalanced: we need to have a procedure to bring the tree back into balance.

### AVL Performance
# from the most unbalanced left-heavy tree, we see Fibonacci number of nodes according to each heights
# An important machematical result is that as the numbers of the Fibonacci sequence get larger and larger F(n)/F(n-1) = (1 + 5^1/2)/2
# derivation proofs h = 1.44logN, that is a big performance improvement.

### AVL implementation

## 1. put - how we will agument the procedure to insert a new key into the tree?
#           a). since all new keys are inserted into the tree as lead nodes and we know that the balance factor for a new leaf is zero, we just insert it
# 			b). Once new lead is added, we must update the balance factor rescursively to the root.
#               i. If the new node is a right child, BF-1
# 				ii. If the new node is a left child, BF+1

# implement the AVL tree as a subclass of BinarySearchTree.
# To begin, we will override the _put method and write a new updateBalance helper method.
def _put(self,key,val,currentNode):
    if key < currentNode.key:
        if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
        else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.leftChild)
    else:
        if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
        else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.rightChild)

# Resursive function to update the BF
# 1. check to see if the current node is out of balance (> 1 or <-1), this is the case the rebalancing is done and no further updating to parents is required.
# 2. If the current node not require rebalancing then the balance factor of the parent is adjusted.
# 3. If the balance factor is not zero, the algorithm continues to work its way up the tree toward the root by recursively calling updateBalace
def updateBalance(self,node):
	# 
    if node.balanceFactor > 1 or node.balanceFactor < -1:
        self.rebalance(node)
        return
    if node.parent != None:
        if node.isLeftChild():
                node.parent.balanceFactor += 1
        elif node.isRightChild():
                node.parent.balanceFactor -= 1
        # 
        if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

# The efficient rebalancing is rorations.
def rebalance(self,node):
	# If a subtree needs a left rotation to bring it into balance, first check the balance factor of the right child.
	# If the child is left heavy do a right rotation on right child, followed by the original left rotation.
	if node.balanceFactor < 0:
	     if node.rightChild.balanceFactor > 0:
	        self.rotateRight(node.rightChild)
	        self.rotateLeft(node)
	     else:
	        self.rotateLeft(node)
	# If a subtree needs a right rotation to bring it into balance, first check the balance factor of the left child.
	# If the left child is right heavy then do a left rotation on the left child, followed by the orginal left rotation.
	elif node.balanceFactor > 0:
	     if node.leftChild.balanceFactor < 0:
	        self.rotateLeft(node.leftChild)
	        self.rotateRight(node)
	     else:
	        self.rotateRight(node)

# To perform a left rotation we essentially do the following:
# 1. Promote the right child (B) to be the root of the subtree.
# 2. Move the old root (A) to be the left child of the new root.
# 3. If new root (B) already had a left child then make it the right child of the new left child (A). 
#    Note: Since the new root (B) was the right child of A the right child of A is guaranteed to be empty at this point. 
#          This allows us to add a new node as the right child without any further consideration.
def rotateLeft(self,rotRoot):
	# temporary variable to keep track of the new root of the subtree, which is the right child of the previous Root
    newRoot = rotRoot.rightChild
    # we replace the right child of the old root with the left child of the new
    rotRoot.rightChild = newRoot.leftChild
    # if the new Root has left child
    if newRoot.leftChild != None:
    	# the new parent of the left child becomes the old root
        newRoot.leftChild.parent = rotRoot
    newRoot.parent = rotRoot.parent
    # If the old root was the root of the entire tree then we must set the root of the tree to point the new root
    if rotRoot.isRoot():
        self.root = newRoot
    # otherwise
    else:
    	# we change the parent of the right child to point to the new root
        if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
        else:
            rotRoot.parent.rightChild = newRoot
    # finally, we set the parent of the old root to be the new root
    newRoot.leftChild = rotRoot
    rotRoot.parent = newRoot
    # we update the balance factors of the old and the new root
    rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
    newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

# symmetric as rotateLeft
def rotateRight(self,rotRoot):
    newRoot = rotRoot.leftChild
    rotRoot.leftChild = newRoot.rightChild
    if newRoot.rightChild != None:
        newRoot.rightChild.parent = rotRoot
    newRoot.parent = rotRoot.parent
    if rotRoot.isRoot():
        self.root = newRoot
    else:
        if rotRoot.isRightChild():
                rotRoot.parent.rightChild = newRoot
        else:
            rotRoot.parent.leftChild = newRoot
    newRoot.rightChild = rotRoot
    rotRoot.parent = newRoot
    rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
    newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

# to be implemented
def delete(self,key):

### Analysis
# get --- LogN. By keeping the tree in balance at all times, we can ensure that the get method will run in order O(logN)
# put --- LogN. Since a new node is inserted as a lead, updating the balance factors of all parents will require a maximum of LogN operations, one for each level of the tree.
#               If a subtree is found to be out of balance, a maximum of two rotations are required to bring the tree track into balance.
#               But each rotation works in O(1) times.
