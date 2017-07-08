### Priority Queues: The logical order of items inside a queue is determined by their priority.
#                    The highest priority items are at the front of the queue and lowest priority items are at the back
#                    Thus when you enqueue an item on a priority queue, the new item may move all the way to the front.

### binary heap data structure: 
# this will allow us both enqueue and dequeue items in O(logN), instead of traditional insert O(n) and sort(NlogN)
## This is interesting because:
# 1. we diagram the heap like a tree, but use only a single list as an internal representation when we implement it.
## The two common variations:
#  min heap - the smallest key is always at the front
#  max heap - the largest key is always at the front

### Operations:
# BinaryHeap() creates a new, empty, binary heap.
# insert(k) adds a new item to the heap.
# findMin() returns the item with the minimum key value, leaving item in the heap.
# delMin() returns the item with the minimum key value, removing the item from the heap.
# isEmpty() returns true if the heap is empty, false otherwise.
# size() returns the number of items in the heap.
# buildHeap(list) builds a new heap from a list of keys.

### Implementation
# Balanced Binary Tree - the same number of nodes in the left and right subtrees of the root
# Complete binary Tree - each level has all of its nodes, except the bottom level of the tree.
#                        we can represent it using a single list.

class BinHeap:
    def __init__(self):
    	# Since the entire binary heap can be represented by a single list, 
    	# all the constructor will do is initialize the list and an attribute currentSize to keep track of the current size of the heap
        self.heapList = [0]
        self.currentSize = 0

    ################# insert method ####################
    # swap the value until to maintain the heap properly
    def percUp(self,i):
	    while i // 2 > 0:
	      if self.heapList[i] < self.heapList[i // 2]:
	         tmp = self.heapList[i // 2]
	         self.heapList[i // 2] = self.heapList[i]
	         self.heapList[i] = tmp
	      i = i // 2

	# append the item to the end of the list
	# this may violate the heap structure property - so we need percolate the item up to restoring the heap properly.
	def insert(self,k):
    	self.heapList.append(k)
    	self.currentSize = self.currentSize + 1
    	self.percUp(self.currentSize)

    ################# delete the minimum ####################
    # since the heap property requires that the root of the tree be the smallest item in the tree, finding the minimum item is easy.
    # The hard part is restoring full compliance with the heap structure and heap order properties
    # First, we will restore the root item by taking the last item in the list and moving it to the root position.
    # Second, we restore the heap order property by pushing the new root node down the tree to its proper position. ---> serveral swaps is needed. 
    #         we need to do is swap the root with its smallest child less than the root.
    #         repeat the the swapping process with a node and its children until the node is swapped into a position on the tree where it is already less than both children.

    def percDown(self,i):
    	"""ensures the largest child is always moved down the tree"""
    	while (i * 2) <= self.currentSize:
        	mc = self.minChild(i)
        	if self.heapList[i] > self.heapList[mc]:
            	tmp = self.heapList[i]
            	self.heapList[i] = self.heapList[mc]
            	self.heapList[mc] = tmp
        	i = mc

	def minChild(self,i):
    	if i * 2 + 1 > self.currentSize:
        	return i * 2
    	else:
        	if self.heapList[i*2] < self.heapList[i*2+1]:
            	return i * 2
        	else:
            	return i * 2 + 1

    def delMin(self):
    	retval = self.heapList[1]
    	self.heapList[1] = self.heapList[self.currentSize]
    	self.currentSize = self.currentSize - 1
    	self.heapList.pop()
    	self.percDown(1)
    	return retval

    ################### build an entire heap from a list ####################
    # we could easily build a heap by inserting each key one at a time
    # Since we start with a list of one item, the list is sorted and we could use binary search to find the right position to insert the next key at a cost of logN operations
    # However, remember that inserting an item in the middle of the list may require O(N) to shift the rest of the list over to make room for the new key.
    # Therefore, insert n keys to the heap would require a total O(NlogN) operations
    # We can start an entire list then we can build the whole heap in O(N) operations
    def buildHeap(self,alist):
    	i = len(alist) // 2
    	self.currentSize = len(alist)
    	self.heapList = [0] + alist[:]
    	while (i > 0):
        	self.percDown(i)
        	i = i - 1