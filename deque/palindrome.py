# A palindrome is a string that reads the same forward and backward, 
# add each character to the rear of the deque.
# The front deque will hold the first character of the string and the rear of the deque will hold the last character
# Since we can remove both of them directly, we can compare them and continue only if they match
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

def palchecker(aString):
	chardeque = Deque()

	for ch in aString:
		chardeque.addRear(ch)

	stillEqual = True
	while chardeque.size() > 1 and stillEqual:
		first = chardeque.removeFront()
		last = chardeque.removeRear()
		if first != last:
			stillEqual = False

	return stillEqual

print(palchecker("lsdkjfkgh"))
print(palchecker("radar"))