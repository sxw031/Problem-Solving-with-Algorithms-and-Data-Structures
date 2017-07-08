# The ordering is typically either ascending or descending and we assume that list items have a meaningful comparison operation that is already defined. 
# OrderedList() creates a new ordered list that is empty. It needs no parameters and returns an empty list.
# add(item) adds a new item to the list making sure that the order is preserved. It needs the item and returns nothing. Assume the item is not already in the list.
# remove(item) removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.
# search(item) searches for the item in the list. It needs the item and returns a boolean value.
# isEmpty() tests to see whether the list is empty. It needs no parameters and returns a boolean value.
# size() returns the number of items in the list. It needs no parameters and returns an integer.
# index(item) returns the position of item in the list. It needs the item and returns the index. Assume the item is in the list.
# pop() removes and returns the last item in the list. It needs nothing and returns an item. Assume the list has at least one item.
# pop(pos) removes and returns the item at position pos. It needs the position and returns the item. Assume the item is in the list.
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

class OrderedList:
	def __init__(self):
		self.head = None

	# isEmpty, size and remove works the same as unordered list since they deal only with the number of nodes in the list without regard to the actual item values.
	def isEmpty(self):
		"""O(1)"""
		return self.head == None

	def size(self):
		"""O(n)"""
		current = self.head
		count = 0
		while current != None:
			count = count + 1
			current = current.getNext()
		return count

	def remove(self, item):
		"""O(n)"""
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

	def search(self, item):
		"""O(n)"""
		current = self.item
		found = False
		stop = False
		while current != None and not found and not stop:
			if current.getData() == item:
				found = True
			else:
				if current.getData() > item:
					stop = True
				else:
					current = current.getNext()

		return found

	def add(self,item):
		"""O(n)"""
    	current = self.head
    	previous = None
    	stop = False
    	while current != None and not stop:
        	if current.getData() > item:
            	stop = True
        	else:
            	previous = current
            	current = current.getNext()

    	temp = Node(item)
    	if previous == None:
        	temp.setNext(self.head)
        	self.head = temp
    	else:
        	temp.setNext(current)
        	previous.setNext(temp)

    def index(self, item):
    	"""get the index of an item, assume the first one (head pointing to) is 0"""
        index = 0
        current = self.head
        found = False
        while current != None:
            if current.getData() == item:
                found = True
                break
            else:
                current = current.getNext()
                index += 1
        if not found:
            index = None
        return index

   	def pop(self, index):
		self.remove(self.getData(index))



