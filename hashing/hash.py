### What is Hashing?
# building the data structure that can be searched in O(1) time. ---> this concept is referred to as hashing
# A hash table is a collection of items which are stored in such a way as to make it easy to find them later.
# Each position of the hash table, often called slot, can hold an item and is named by an integer value starting at 0. ---> slot named 0, slot name 1....
# hash function ---> mapping between an item and the slot where that item belongs in the hash table.
# remainder method ---> simply takes an item and divides it by the table size, returning the remainder as its hash value "h(item) = item%11"
# load factor ---> number of items / table size
# Then, we simply use the hash function to compute the slot name for the item and then check the hash table to see if it is present.
# This technique is going to work only if each item maps to a unique location in the hash table.
# A collison will happen if two or more items would need to be in the same slot.
# A perfect hash function: maps each item into a unique slot.
# one way to have a perfect hash function is to increase the size of the hash table so that each possible value in the item range can be accommodated
# 	This is practical for small numbers of items, it is not feasible when the number of possible items is large.
# Our goal is to create a hash function that minimizes the number of collisions, is easy to compute, and evenly distributes the items in the hash table. 

### Hashing Functions
# folding method:
#   1. beginning by dividing the item into equal-size pieces 
#   2. these pieces are then added together give the resulting hash value.
# mid-square method:
#   1. we first square the item
#   2. then, extract some portion of the resulting digits
#   3. and, perform the remainder

# For example, hash takes a string and a table size and returns the hash value in the range from 0 to tablesize-1
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])

    return sum%tablesize


### Collison Resolution
# systematic method for placing the second item in the hash table.
# open addressing: collison resolution process that it tries to find the next open slot or address in the hash table
# By systematically visiting each slot one at a time, we are performing an open addressing technique called linear probing.
# clustering. This means that if many collisons occur at the same hash value, a number of surrounding slots will be filled by the linear probing solutions.
## solution 1 - linear probing
# rehashing: means extend the linear probing. instead of newhashvalue = rehash(oldhashvalue) where rehash(pos) = (pos+1)%sizeoftable, the "plus 3" rehash can be defined as rehash(pos) = (pos+3)%sizeoftable
# (choose prime number for the table size to ensure all slots will be eventually be visited.)
# quadratic probing: Instead of using a constant “skip” value, we use a rehash function that increments the hash value by 1, 3, 5, 7, 9, and so on.
## solution 2 - Chaining
# allow each slot to hold a reference to a collection(or chain) of items.
# when collison happens the item is still placed in the proper slot of the hash table

### Implementing the Map Abstract Data Type
# The structure is an unordered collection of associations between a key and a data value.
# The keys in a map are all unique so that there is a one-to-one relationship between a key and a value.

## Operations
# Map() Create a new, empty map. It returns an empty map collection.
# put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.
# get(key) Given a key, return the value stored in the map or None otherwise.
# del Delete the key-value pair from the map using a statement of the form del map[key].
# len() Return the number of key-value pairs stored in the map.
# in Return True for a statement of the form key in map, if the given key is in the map, False otherwise.


class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None]*self.size
		self.data = [None]*self.size

	# The put function assumes that there will eventually be an empty slot unless the key is already present in the self.slots. 
	# It computes the original hash value and if that slot is not empty, iterates the rehash function until an empty slot occurs. 
	# If a nonempty slot already contains the key, the old data value is replaced with the new data value. 
	def put(self,key,data):
  		hashvalue = self.hashfunction(key,len(self.slots))

	  	if self.slots[hashvalue] == None:
	    	self.slots[hashvalue] = key
	    	self.data[hashvalue] = data
	  	else:
	    	if self.slots[hashvalue] == key:
	      	self.data[hashvalue] = data  #replace
	    else:
	      	nextslot = self.rehash(hashvalue,len(self.slots))
	      	while self.slots[nextslot] != None and self.slots[nextslot] != key:
	        	nextslot = self.rehash(nextslot,len(self.slots))

	      	if self.slots[nextslot] == None:
	        	self.slots[nextslot]=key
	        	self.data[nextslot]=data
	      	else:
	        	self.data[nextslot] = data #replace

	def hashfunction(self,key,size):
		"""implements the simple remainder method"""
    	return key%size

	def rehash(self,oldhash,size):
		"""the linear probing with "plus 1" rehash function"""
    	return (oldhash+1)%size

    # Likewise, the get function begins by computing the initial hash value. 
    # If the value is not in the initial slot, rehash is used to locate the next possible position. 
    # Notice that line 114 guarantees that the search will terminate by checking to make sure that we have not returned to the initial slot. 
    # If that happens, we have exhausted all possible slots and the item must not be present.
	def get(self,key):
		startslot = self.hashfunction(key,len(self.slots))

		data = None
		stop = False
		found = False
		position = startslot
		while self.slots[position] != None and  not found and not stop:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position=self.rehash(position,len(self.slots))
			if position == startslot:
			   	stop = True
		return data

	def __getitem__(self,key):
	    return self.get(key)

	def __setitem__(self,key,data):
	    self.put(key,data)

### Testing
H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"
H.slots
h.data

### Analysis
# Although the best case hashing would provide O(1), the constant search techique, due to collison, the number of comparison is not simple.
# The most important piece is the load factor, λ.
# 	a). if λ is small, there is low chance of collison
#   b). if λ is large, meaning that the table is filling up, and there are more and more collisons.
#   c). The number of comparison: 1/2(1+ 1/(1-λ)) ---> successful search, 1/2(1+(1/1-λ)^2) ---> unsuccessful search
# with chaining, increased collison means an increased number of items on each chain.
#   a). The number of comparison: 1 + λ/2 ---> successful search; λ ----> unsuccessful search





