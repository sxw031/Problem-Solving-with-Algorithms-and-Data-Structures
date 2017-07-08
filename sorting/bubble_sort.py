### bubble sort - most inefficient sorting method, but an advantange in that it will recognize the sorted list and stop.
# As with a bubble sort, after the first pass, the largest item is in the correct place. After the second pass, the next largest is in place. 
# It compares adjacent items and exchanges those that are out of order. 
# If there are n items in the list, then there are n−1 pairs of items that need to be compared on the first pass.
# The total comparison is n-1 + n-2 + ...1  =====> O(): (1/2n^2 - 1/2n) ====> O(n^2)
# swap i and j: 
#    temp = alist[i]
#    alist[i] = alist[j]
#    alist[j] = temp
# python can do swap in simultaneous assignment a,b = b,a

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)

# 
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort(alist)
print(alist)