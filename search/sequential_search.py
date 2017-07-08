# (If item is present)      vs (Item is not present)
# Best Case: 1;                 Best Case: n
# Wrost Case: n                 Wrost Case: n
# Average Case: n/2				Average Case: n

# the items in the list is unsorted
def sequentialSearch(alist, item):
	pos = 0
	found = False

	while pos < len(alist) and not found:
		if alist[pos] == item:
			found = True
		else:
			pos = pos + 1

	return found

# (If item is present)      vs (Item is not present)
# Best Case: 1;                 Best Case: n
# Wrost Case: n                 Wrost Case: n
# Average Case: n/2				Average Case: n/2

# the item in the list is sorted in an ascending order
# The advantage is when the item is not present in the list, we don't have to compare the entire list.
def orderedSequentialSearch(alist, item):
	pos = 0
	found = False
	stop = False
	while pos < len(alist) and not found and not stop:
		if alist[pos] == item:
			found = True
		else:
			if alist[pos] > item:
				stop = True
			else:
				pos = pos + 1
	return found