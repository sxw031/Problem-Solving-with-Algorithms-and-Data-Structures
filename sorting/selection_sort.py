### Selection Sort
# improvement on buble sort by making only one exchange for every pass through the list.
# look for the largest value as it makes a pass and, after completing the pass, places it in the proper location.
# it makes the same number of comparisons as the bubble sort, therefore O(n^2)

def selectionSort(alist):
	# loop from the last position to the first
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       # find the position of the largest value compares to selected value, which is sequenced from last to the first.
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)