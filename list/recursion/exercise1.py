# Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string using recursive algorithm
def reverseStr(s):
	if len(s) == 1:
		return s
	else:
		return s[-1] + reverseStr(s[:-1])

# Write a function that takes a string as a parameter and returns True if the string is a palindrome, False otherwise.
def palindromeChecker(s):
	if len(s) == 2 and s[0] == s[1]:
		return True
	if len(s) == 1:
		return True
	else:
		return (s[0] == s[-1]) and palindromeChecker(s[1:-1])

def removeSP(s):
	newstr = ""
	for i in s:
		if s[i] >= "a" and s[i] <= "z":
			newstr += s[i]
	return newstr

print palindromeChecker(removeSP("rader".lower()))
print palindromeChecker(removeSpace("Go hang a salami; I'm a lasagna hog.".lower()))