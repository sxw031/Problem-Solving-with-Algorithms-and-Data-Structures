# a great divide and conquer strategy
# 1. A binary search starts by examining the middle item
#    a. if the item is greater than the middle item: we eliminate the lower half and the middle item
# 2. repeat the process with the upper half.
# we either split it or find it

def binarySearch(alist, item):
	first = 0
	last = len(alist) - 1
	found = False

	while first <= last and not found:
		midpoint = (first + last) // 2
		if alist[midpoint] == item:
			found = True
		else:
			if item < alist[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	return found

# solve it by recrusive function
def binarySearch(alist, item):
	if len(list) == 0:
		return False
	else:
		midpoint = len(alist)/2
		if alist[midpoint] == item:
			return True
		else:
			if item < alist[midpoint]:
				return binarySearch(alist[:midpoint], item)
			else:
				return binarySearch(alist[midpoint+1:], item)

### Analysis
# 1. The number of comparison is i where n/(2^i) = 1; 1 here means either we find it or it is not. => solving i=logn
# 2. Also, [:] - "the slice operator" in python takes O(k), so the performance is not exact logN
# 3. Even though a binary search is generally better than a sequential search, it is important to note that for small value n, the additional cost of sorting is probably not worth it.
#    In fact, we should always consider whether it is cost effective to take on the extra work of sorting to gain search benefits.
#    If we can sort once and then search many times, the cost of the sort is not expensive.
#    If, for large lists however, sorting once can be so expensive that simply performing a sequential search from the start may be the best. 