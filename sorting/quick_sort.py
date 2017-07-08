### Quick Sort
# The second divide and conquer method, while not using additional storage.
# As a trade-off, it is possible that the list may not be divided in half. -> when this happens, the performance is diminished.

## Procedure
# 1. select a value, called pivot value to assist with spliting the list. (we can choose the first one)
# 2. partition begins with two position markers - leftmark and rightmark
# 3. increment leftmark until we find a value that is greater than the pivot value; decrement the rightmarker until we find a value that less than the pivot value
# 4. exchange this two items
# 5. keep moving leftmarker and rightmarker repeatly as step 3 until we found the split point
# 6. exchange the split point with the selected value. ---> all the items to the left of the split point are less than the pivot value, and all the items to the right of the split point are greater than the pivot value. 
# 7. now quick sort can invoked recursively on the two halves.

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

# quickSortHelper begins with the same base case as the merge sort. 
# If the length of the list is less than or equal to one, it is already sorted. 
# If it is greater, then it can be partitioned and recursively sorted. 
def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)


### Analysis
# LogN divisions + each n items needed to be checked against the pivot value ---> NlogN + no need for additional memory as in the merge sort process.
# In the worst case, the split point may not be in the middle and can be skewed to the left or the right. ---> O(n^2) recursion requires
# we can use median of three to choose pivot value to alleviate some of the potential for an uneven division: pickest the middle value from the [0, middle, -1] index of values
