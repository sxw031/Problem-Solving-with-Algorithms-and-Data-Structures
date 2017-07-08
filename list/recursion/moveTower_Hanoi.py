## Tower of Hanoi
# At the beginning of time, the priests were given three poles and a stack of 64 gold disks, 
# each disk a little smaller than the one beneath it. 
# Their assignment was to transfer all 64 disks from one of the three poles to another, with two important constraints.

## Two constraint:
# 1. they could only move one disk at one time
# 2. they could never place a larger disk on top of a smaller one.

## High-level outline: 
# we can use it recursively, as long as we always obey the rule that the larger disks remain on the bottom of the stack.
# In addition, the steps outlined above move us toward the base case by reducing the height of the tower in steps 1 and 3.
# 1. Move a tower of height-1 to an intermediate pole, using the final pole.
# 2. Move the remaining disk to the final pole.
# 3. Move the tower of height-1 from the intermediate pole to the final pole using the original pole. 

## Base case:
# The simplest Haoni Tower Problem is a tower of one disk. In this case, we need move only a single disk to its final destination.
# The base case is detected when the tower height it 0; in this case there is nothing to do, so the moveTower function simply returns. 
# The important thing to remember about handling the base case this way is that simply returning from moveTower is what finally allows the moveDisk function to be called.

def moveTower(height, fromPole, toPole, withPole):
	if height >= 1:
		moveTower(height-1, fromPole, withPole, toPole) # recursive call, move all but the bottom disk on the initial tower to an intermediate pole.
		moveDisk(fromPole, toPole)
		moveTower(height-1, withPole, toPole, fromPole) # recursive call, move the tower from the intermediate pole to the top of the largest disk.

def moveDisk(fp,tp):
	print("moving disk from",fp,"to",tp)

moveTower(3, "A", "B", "C")

# Post discussion:
# you may be wondering why we do not have a data structure that explicitly keeps track of what disks are on what poles. 
# Here is a hint: if you were going to explicitly keep track of the disks, you would probably use three Stack objects, one for each pole. 
# The answer is that Python provides the stack that we need implicitly through the call stack.


