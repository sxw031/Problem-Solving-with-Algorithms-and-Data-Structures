### Insertion Sort
# O(n^2): n-1 passes to sort n items. The iteration starts at position 1 and moves through position n-1, as there are items that need to be inserted back into the sorted lists.
# It always maintains a sorted sublist in the lower positions of the list.
# Each new item is then "insert" back into the previous sublist such that the sorted sublist is one item larger.

# Advantages:
# 1. The best case has only one comparison
# 2. shifting operations requires approximately a third of the processing work of an exchange since only one assignment is performed. 

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)