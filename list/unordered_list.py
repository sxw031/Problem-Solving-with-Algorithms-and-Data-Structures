### What is list
# The list is a powerful, yet simple, collection machanism that provies the programmer with a wide variety of operations.
# However, not all programming languages include a list collection. In this case, the notion of a list must be implemented by the programmer.

# A list is a collection of items where each item holds relative position with respect to the others. --- unordered list
# For simplicity, we can assume that lists cannot contain duplicate items.

### Abstract Data type
# List() creates a new list that is empty. It needs no parameters and returns an empty list.
# add(item) adds a new item to the list. It needs the item and returns nothing. Assume the item is not already in the list.
# remove(item) removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.
# search(item) searches for the item in the list. It needs the item and returns a boolean value.
# isEmpty() tests to see whether the list is empty. It needs no parameters and returns a boolean value.
# size() returns the number of items in the list. It needs no parameters and returns an integer.
# append(item) adds a new item to the end of the list making it the last item in the collection. It needs the item and returns nothing. Assume the item is not already in the list.
# index(item) returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.
# insert(pos,item) adds a new item to the list at position pos. It needs the item and returns nothing. Assume the item is not already in the list and there are enough existing items to have position pos.
# pop() removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.
# pop(pos) removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.

### Implementation: commonly known as linkedin list.
# It is important to note that the location of the first item of the list must be explicitly specified. 
# Once we know where the first item is, the first item can tell us where the second is, and so on. 
# The external reference is often referred to as the head of the list. Similarly, the last item needs to know that there is no next item.

## The node class
# 1. node must contain list item itself --- the data field of the node.
# 2. each node must hold a reference to the next node.

class Node:
	def __init__(self,initdata):
		self.data = initdata
		self.next = None # there is no next node; this is sometimes refers to "grounding the node"

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		return self.data = newdata

	def setNext(self, newnext):
		return self.next = newnext


class UnorderedList：
	def __init__(self):
		self.head = None #reference to the first node

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()
		return count

	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

		return found

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()

		# once the searching step of the remove has been completed, we need to remove the node from the linked list.
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

	def append(self, item):
		"""add item into the linked list from the other direction compared to add()"""
		current = self.head
		if current:
			while curren.getNext() != None:
				current = current.getNext()
			current.setNext(Node(item))
		else:
			self.head = Node(item)

	def index(self, item):
		"""get the index of an item, assume the first one(head pointing to) is 0"""
		index = 0
		current = self.head
		found = False
		while current != None:
			if current.getData == item:
				found = True
				break
			else:
				current = current.getNext()

		if not found:
			index = None
		return index

	def pop(self, index):
		self.remove(self.getData(index))

	def insert(self, index):
		"""insert an item after index item"""
		current = self.head
		for i in range(index):
			current = current.getNext()

		if current != None:
			temp = Node(item)
			temp.setNext(current.getNext())
			current.setNext(temp)
		else:
			raise("index out of range")
		










