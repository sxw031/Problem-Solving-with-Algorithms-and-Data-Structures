### SUMMARY ANALYSIS
# Operation         Sorted Lists         Hash Table         Binary Search Tree          AVL Tree
#   put                 O(n)                O(1)                  O(n)                   O(logN)
#   get                 O(logN)             O(1)                  O(n)                   O(LogN)
#   in                  O(logN)             O(1)                  O(n)                   O(LogN)
#   del                 O(n)                O(1)                  O(n)                   O(logN)

### Tree Properties
# 1. Trees are hierarchical. By hierarchical, we mean that trees are structured in layers with the more general things near the top and the more specific things near the bottom. 
# 2. All of the children of one node are independent of the children of another node. 
# 3. Each leaf node is unique.

### Examples: File System, Web Page(HTML)

### Vocabulary
# 1. Node - called "key". It can also have additional information called "payload", which is critical in appications that make use of the trees.
# 2. Edge - it connects two nodes to show that there is a relationship between them
# 3. Root - the only node in the tree that has no incoming edges.
# 4. Path - an ordered list of nodes that are connected by edges.
# 5. Children - The set of nodes c that have incoming edges from the same node to are said to be the children of that node.
# 6. Parent - A node is the parent of all the nodes it connects to with outgoing edges.
# 7. Sibling - Nodes in the tree that are children of the same parent are said to be siblings.
# 8. Subtrees - is a set of nodes and edges comprised of a parent and all the descendants of that parent.
# 9. Leaf Node - A node that has no children.
# 10. Level - number of edges on the path from the root node to n.
# 11. Height - The maximum level of any node in the tree.
# 12. Binary Tree - a root node and two children.

### Definition
# 1. A tree consists of a set of nodes and a set of edges that connect pairs of nodes. A tree has the following properties:
#    a). One node of the tree is designated as the root node.
#    b). Every node n, except the root node, is connected by an edge from exactly one other node p, where p is the parent of n.
#    c). A unique path traverses from the root to each node.
#    d). If each node in the tree has a maximum of two children, we say that the tree is a binary tree.

# 2. A tree is either empty or consists of a root and zero or more subtrees, each of which is also a tree. 
#    The root of each subtree is connected to the root of the parent tree by edge.

### List of Lists Representation
# Nice property:
# 1. the structure of a list representing a subtree adheres to the structure defined for a tree; the structure itself is recursive.
# 3. It generalizes to a tree that has many subtrees.

def BinaryTree(r):
	return [r, [], []]

# we first obtain the (possibly empty) list that corresponds to the current left child. 
# We then add the new left child, installing the old left child as the left child of the new one. 
# This allows us to splice a new node into the tree at any position. 
def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

# accessing function
def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

# Test
r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
print(l)

setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))


### Nodes and References Representation
# define a class that has attributes for the root value, as well as the root value

class BinaryTree:
	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self,newNode):
	    if self.leftChild == None:
	        self.leftChild = BinaryTree(newNode)
	    else:
	        t = BinaryTree(newNode)
	        t.leftChild = self.leftChild
	        self.leftChild = t

	def insertRight(self,newNode):
    	if self.rightChild == None:
        	self.rightChild = BinaryTree(newNode)
    	else:
        	t = BinaryTree(newNode)
        	t.rightChild = self.rightChild
        	self.rightChild = t

    # accessor methods
    def getRightChild(self):
    	return self.rightChild

	def getLeftChild(self):
	    return self.leftChild

	def setRootVal(self,obj):
	    self.key = obj

	def getRootVal(self):
	    return self.key

# Test
r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())








