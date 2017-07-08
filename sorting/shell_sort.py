### Shell Sort - diminishing increment sort/ improve on insertion sort
# choose increment i to break the original list into sublists of contiguous items
# using insertion to sort each sublist ---> we have moved the items closer to where they actually belong.
# The unique way that these sublists are chosen is the key to the shell sort. 
# Instead of breaking the list into sublists of contiguous items, the shell sort uses an increment i, sometimes called the gap, to create a sublist by choosing all items that are i items apart.
# finally, use standard insertion sort to show the final result
# This reduced the total number of shifting operations necessary to put the list in its final order. 
# the way in which the increments are chosen is the unique feature of the shell sort. 
# O() between n and n^2. around n^(3/2), because the list is pre-sorted for the last step of insetion sort

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)
