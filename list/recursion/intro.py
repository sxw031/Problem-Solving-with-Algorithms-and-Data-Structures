### What is recursion?
# Recursion is a method of solving problems that involves breaking a problem down into smaller and smaller subproblems 
# until you get to a small enough problem that it can be solved trivially.

### The first example: sum
def thesum1(numlist):
	theSum = 0
	for i in numList:
		thesum = theSum + i
	return theSum

# using recursion
def thesum2(numlist):
	# our crucial check and is our escape clause from the function
	if len(numlist) == 1:
		return numlist[0]
	else:
		return numlist[0] + thesum(numlist[1:])


### The three laws of recursion
# 1. A recursive algorithm must have a base case. It allows the algorithm to stop recursing.
# 2. A recursive algorithm must change its state and move toward the base case
# 3. A recursive algorithm must call itself, recursively. The logic is not circular at all; the logic of recursion is an elegant expression of solving a problem by breaking it down into a smaller and easier problems.

### The second example: Converting an integer to a String in any base
def toStr(n, base):
	convertString = "0123456789ABCDEF"
	if n < base:
		return convertString[n]
	else:
		return toStr(n//base, base) + convertString[n%base]

print(toStr(1543, 16))