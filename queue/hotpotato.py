#### Queue
# FIFO, first-in, first-out OR first-come, first-serve
# "rear" and "front"
# example: check-out line at grocery store, wait in cafeteria line, printing task, control processes within a computer, the scheduling of keystrokes

# Queue() creates a new queue that is empty. It needs no parameters and returns an empty queue.
# enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing.
# dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified.
# isEmpty() tests to see whether the queue is empty. It needs no parameters and returns a boolean value.
# size() returns the number of items in the queue. It needs no parameters and returns an integer.

# Implement a Quenue, it assumes that the rear is at position 0 in the list. 
# This allows us to use the insert function on lists to add new elements to the rear of the queue. 
# The pop operation can be used to remove the front element (the last element of the list). 
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

## Example
# This game is a modern-day equivalent of the famous Josephus problem. 
# Based on a legend about the famous first-century historian Flavius Josephus, the story is told that in the Jewish revolt against Rome, 
# Josephus and 39 of his comrades held out against the Romans in a cave. With defeat imminent, they decided that they would rather die than be slaves to the Romans. 
# They arranged themselves in a circle. One man was designated as number one, and proceeding clockwise they killed every seventh man. 
# Josephus, according to the legend, was among other things an accomplished mathematician. 
# He instantly figured out where he ought to sit in order to be the last to go. 
# When the time came, instead of killing himself, he joined the Roman side. 
# You can find many different versions of this story. Some count every third man and some allow the last man to escape on a horse. 
# In any case, the idea is the same.

# Our program will input a list of names and a constant num to be used for counting.
# the simulation will simply dequeue and then immediately enqueue that child, putting her at the front of the line.
# She will then wait until all the others have been at the front before it will be her turn again.
# After num(countings) of dequeue/enqueue operations, the child at the front will be removed permanently and another cycle will begin.
# This process will continue until only once name remains.

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))


# Notice the value of the counting number is greater than the number of names
# Also notice the list is loaded into the queue such that the first name on the list will at the front of the queue.
# we can modify the code to implement for a random counter.



