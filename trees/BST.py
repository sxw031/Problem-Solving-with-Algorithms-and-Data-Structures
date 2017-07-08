### Binary Search Tree: another way to map key and value
# In this case, we are interested in using the binary tree structure to provide for efficient searching, not exact placement of items in the tree.

### Search Tree Operation:
# Map() Create a new, empty map.
# put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.
# get(key) Given a key, return the value stored in the map or None otherwise.
# del Delete the key-value pair from the map using a statement of the form del map[key].
# len() Return the number of key-value pairs stored in the map.
# in Return True for a statement of the form key in map, if the given key is in the map.

### Search Tree Implementation

## BST property: 
# keys are less than the parent are found in the left subtree;
# keys are greater than the parent are found in the right subtree;
# The first key insert into the tree is the root.

## nodes and reference approach using two classes.
# Because we must be able create and work with a binary search tree that is empty, 
# The first class we will call BinarySearchTree, and the second class we will call TreeNode. 
# The BinarySearchTree class has a reference to the TreeNode that is the root of the binary search tree.
# In most cases the external methods defined in the outer class simply check to see if the tree is empty.

### PART I

# define constructor + helper functions for BinarySearchTree
# 1. helper functions help to classify a node according to its own position as a child, and the kind of children the node has.
# 2. The TreeNode also keep track of the parent as an attribute of each node.
# 3. we use Python's optional parameters to make easy for us to create a TreeNode under different circumstances: TreeNode already has both a parent and a child; A TreeNode with key value only; 
class TreeNode:
   def __init__(self,key,val,left=None,right=None,
                                       parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

# It is the shell
class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    ### PART II. start build the binary search tree.
    def put(self,key,val):
    	"""This method will check to see if the tree already has a root. 
    	If there is not a root then put will create a new TreeNode and install it as the root of the tree."""
    	if self.root:
    		self._put(key,val,self.root)
    	else:
    		self.root = TreeNode(key,val)
    	self.size = self.size + 1

    # If a root node is already in place then put calls the private, recursive, helper function _put to search the tree according to the following algorithm:
    # 1. Starting at the root of the tree, search the binary tree comparing the new key to the key in the current node. If the new key is less than the current node, search the left subtree. If the new key is greater than the current node, search the right subtree.
	# 2. When there is no left (or right) child to search, we have found the position in the tree where the new node should be installed.
	# 3. To add a node to the tree, create a new TreeNode object and insert the object at the point discovered in the previous step.
	# recursively 1-3

	## (There is a problem with this impementation (exercise to fix the bug)
	#  As our tree is implemented a duplicate key will create a new node with the same key value in the right subtree of the node having the original key.
	#  The result of this is that the node with the new key will never be found during in search
	#  A better way the insertion of a duplicate key is for the value associated with the new key to replace the old value.)
	def _put(self,key,val,currentNode):
	    if key < currentNode.key:
	        if currentNode.hasLeftChild():
	               self._put(key,val,currentNode.leftChild)
	        else:
	               currentNode.leftChild = TreeNode(key,val,parent=currentNode)
	    else:
	        if currentNode.hasRightChild():
	               self._put(key,val,currentNode.rightChild)
	        else:
	               currentNode.rightChild = TreeNode(key,val,parent=currentNode)

	# this allows Python statement myZipTree['Plymouth'] = 55446, just like a Python dictionary              
	def __setitem__(self,k,v):
		self.put(k,v)

	### PART III
	# once the tree is constructed, the next task is to implement the retrieval of a value for a given way.

	# get method simply searches the tree recursively until it gets a non-matching lead node for finds a matching key.
	# when a matching key is found, the value stored in the payload of the node is returned.
	def get(self,key):
    if self.root:
        res = self._get(key,self.root)
        if res:
               return res.payload
        else:
               return None
    else:
        return None

    # use the same logic for choosing the left or right child as the _put method
    # _get return the TreeNode to get, this allow _get to used as flexible helper method.
	def _get(self,key,currentNode):
	    if not currentNode:
	        return None
	    elif currentNode.key == key:
	        return currentNode
	    elif key < currentNode.key:
	        return self._get(key,currentNode.leftChild)
	    else:
	        return self._get(key,currentNode.rightChild)

	# we can write Python statement that looks just like we are accessing a dictionary
	# As you can see, all the __getitem__ method does is call get
	def __getitem__(self,key):
	    return self.get(key)

	# overloads the in operator using get method, simply return True if get returns a value
	def __contains__(self,key):
    	if self._get(key,self.root):
        	return True
    	else:
        	return False

    ### PART IV - deletion (most challenge)
    # Step 1. find the node to delete by searching the tree
    #     a). if the tree has more than one node ---> we use _get to find the TreeNode that needs to be removed.
    #     b). if the tree has a single node, that means we remove the root of the tree. (but we still must check to make sure key of root matches the key that is to be deleted)
    #     c). else if the key is not found, the del operator raises an error.
    def delete(self,key):
   		if self.size > 1:
    		nodeToRemove = self._get(key,self.root)
      		if nodeToRemove:
        		self.remove(nodeToRemove)
          		self.size = self.size - 1
      		else:
        		raise KeyError('Error, key not in tree')
    	elif self.size == 1 and self.root.key == key:
    		self.root = None
    		self.size = self.size - 1
    	else:
    		raise KeyError('Error, key not in tree')

	def __delitem__(self,key):
		self.delete(key)

	# Step 2. Once we've found the node containing the key we want to delete, there are three cases that we must consider:
	# 1. The node to be deleted has no children.
	# 2. The node to be deleted has only one child.
	# 3. The node to be deleted has two child.
    def remove(self,currentNode):
    	# The first case: if the current node has no children ---> delete the node and remove the reference to this node in the parent.
    	if currentNode.isLeaf(): # leaf
    		if currentNode == currentNode.parent.leftChild:
            	currentNode.parent.leftChild = None
           	else:
           		currentNode.parent.rightChild = None

        elif currentNode.hasBothChildren(): #interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else: # The second case: this node has one child. we can simply promote the child to take the place of its parent.
        	# there are six cases to consider, and the cases are symmetric with respect to either having left or right child.
           	if currentNode.hasLeftChild():
           		# if the current node is a left child:
           		# we update the parent reference of the left child to point to the parent of the current node, 
           		# and update the left child reference of the parent to point to the current node's left node
             	if currentNode.isLeftChild():
                 	currentNode.leftChild.parent = currentNode.parent
                 	currentNode.parent.leftChild = currentNode.leftChild
             	elif currentNode.isRightChild():
                 	currentNode.leftChild.parent = currentNode.parent
                 	currentNode.parent.rightChild = currentNode.leftChild
             	# if the current node has no parent, it must be the root, we must replace the key, payload, leftchild, right child.
             	else:
                 	currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
           	else:
             	if currentNode.isLeftChild():
                 	currentNode.rightChild.parent = currentNode.parent
                 	currentNode.parent.leftChild = currentNode.rightChild
             	elif currentNode.isRightChild():
                 	currentNode.rightChild.parent = currentNode.parent
                 	currentNode.parent.rightChild = currentNode.rightChild
             	else:
                 	currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)

        # The third case: if node has two children.
        # we search the tree for a node that can be used to replace the one scheduled for deletion.
        # after the target node, we find the next-largest key in the tree from both left and right subtrees, call it successor
        # heler functions findSuccessor and findMin to find the successor
        elif currentNode.hasBothChildren(): #interior
        	# find successor
        	succ = currentNode.findSuccessor()
        	# remove the successor, 
        	# we could call delete recursively, but we don't want waste time re-searching for the key node.
        	succ.spliceOut()
        	currentNode.key = succ.key
        	currentNode.payload = succ.payload

    def findSuccessor(self):
		succ = None
		# case 1: if the node has a right child, the successor is the smallest key in the subtree
		if self.hasRightChild():
    		succ = self.rightChild.findMin()
    	# no right child
		else:
	    	if self.parent:
	    		# case 2: current node is the left child of its parent ---> the succ is its parent
	           	if self.isLeftChild():
	               	succ = self.parent
	            # case 3: current node is the right child of its parent ---> the successor to this node is the successor of its parent, excluding this node.
	           	else:
	               	self.parent.rightChild = None
	               	succ = self.parent.findSuccessor()
	               	self.parent.rightChild = self
		return succ

	# the leftmost child of the tree
	def findMin(self):
    	current = self
    	while current.hasLeftChild():
        	current = current.leftChild
    	return current

	def spliceOut(self):
	    if self.isLeaf():
	        if self.isLeftChild():
	               self.parent.leftChild = None
	        else:
	               self.parent.rightChild = None
	    elif self.hasAnyChildren():
	        if self.hasLeftChild():
	               	if self.isLeftChild():
	                  	self.parent.leftChild = self.leftChild
	               	else:
	                  	self.parent.rightChild = self.leftChild
	               	self.leftChild.parent = self.parent
	        else:
	               	if self.isLeftChild():
	                  	self.parent.leftChild = self.rightChild
	               	else:
	                  	self.parent.rightChild = self.rightChild
	               	self.rightChild.parent = self.parent

	# Python provides us with a very powerful function to use when creating an iterator. 
	# The function is called yield. yield is similar to return in that it returns a value to the caller. 
	# However, yield also takes the additional step of freezing the state of the function so that the next time the function is called it continues executing from the exact point it left off earlier. 
	# Functions that create objects that can be iterated are called generator functions.
	# __iter__ overrides "for x in" operation for iteration, so it really is recursive!
	def __iter__(self):
		if self:
			if self.hasLeftChild():
				for elem in self.leftChild:
					yield elem
			yield self.key
			if self.hasRightChild():
				for elem in self.rightChild:
					yield elem

mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])


### PART V - Analysis
## PUT method: the limitation is the height of the tree. we need to do at most one comparison at each level of the tree.
#              1. LogN. If keys are added in a random order: the height of the tree: logN, n is the number of nodes in the tree, because about half of them will be less than the root and half will be greater than the root.
#              # the number of nodes =2^d, where d is the depth of the tree
#              2. LogN If a perfectly balanced tree where has same number of nodes in the left subtree as right subtree. the worst-case performance of put is O(logN), where N is the number of nodes.
#              Therefore logN gives us height of the tree, and represent the max number of comparison that put will need to do as it researches for the proper place to insert a new node.
#              3. O(N). If keys are inserted in sorted order: put has O(N)
# get,in method: worst case is search tree all the way to the bottom -> O(N)
# del method: the worst-case to find the successor is also just a height of the tree -> 2*O(N) ---> O(N)

# put get has O(N) when the tree is unbalanced.



