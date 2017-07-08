### Merge Sort - Recursive(NlogN)
# This is the only method ganuratees the NlogN on wrost case
# divide and conquer stragety - merge and quick sort.
# it continually splits a list in half.
# If the list is empty or has one item, it is sorted by definition (the base case). If the list has more than one item, we split the list and recursively invoke a merge sort on both halves. 
#

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        # line 17-38, merging two smaller sorted lists into a larger sorted list.
        # Notice that the merge operations operation places the item back into its original list one at a time by repeatedly taking the smallest item from the sorted list.
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)


## Analysis
# 1. list is split in half ---> O(logN)
# 2. merge: each item in the list will eventually be processed and placed on the sorted list. A list size of n requires n operations. ---> O(n)
# 3. it requires extra space to hold the two halves as they are extracted with the slicing operations.


