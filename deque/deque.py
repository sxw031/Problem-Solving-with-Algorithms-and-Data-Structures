### What is deque?
# a deque, also known as double-ended queue.
# it has two ends, a front and a rear.
# unstrictive nature of adding and removing items. New items can be added or removed at either the front or the rear.
# This hybrid linear structure provides all capabilities of stacks and queues in a single data structure.
# up to us to decide LIFO or FIFO.
# It is very important to keep track of the front and the rear as you move items in and out of the collection as things can get a bit confusing.
# adding and removing items from the Front is O(1), whereas adding and removing from the Rear is O(n)


### Structure and Operations
# Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.
# addFront(item) adds a new item to the front of the deque. It needs the item and returns nothing.
# addRear(item) adds a new item to the rear of the deque. It needs the item and returns nothing.
# removeFront() removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
# removeRear() removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
# isEmpty() tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
# size() returns the number of items in the deque. It needs no parameters and returns an integer.

### Implementation
class Deque:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def addFront(self, item):
		self.items.append(item)

	def addRear(self, item):
		self.items.insert(0,item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)




