# A good example problem for showing algorithms with different orders of magnitude is the classic anagram detection problem for strings. 
# One string is an anagram of another if the second is simply a rearrangement of the first. 
# For example, 'heart' and 'earth' are anagrams. The strings 'python' and 'typhon' are anagrams as well. 
# For the sake of simplicity, we will assume that the two strings in question are of equal length and that they are made up of symbols from the set of 26 lowercase alphabetic characters. 
# Our goal is to write a boolean function that will take two strings and return whether they are anagrams.

# Solution 1: checking off

# to analyze this algorithm, we need to note that each of the n characters in s1 will cause a iteration through up to n characters in the list from s2.
# Each of the n positions in the list will be visited once to match a character from s1.
# Big O: 1/2n^2 + 1/2n -> O(n^2)
def anagramSolution1(s1,s2):
    alist = list(s2) #since string in python is immutable

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

print(anagramSolution1('abcd','dcba'))

# Solution 2: sort and compare
# big O will have either O(n^2) or NlogN, depends on the sort algorithm
def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagramSolution2('abcde','edcba'))

# Solution 3: Brute Force (n! grows even faster than 2^n)
# we can simply generate a list of all possible strings using the characters from s1 and then see if s2 occurs.
# However, there is a difficulty with this approach. 
# When generating all possible strings from s1, there are n possible first characters, n−1n−1 possible characters for the second position, n−2n−2 for the third, and so on. 
# The total number of candidate strings is n∗(n−1)∗(n−2)∗...∗3∗2∗1n∗(n−1)∗(n−2)∗...∗3∗2∗1, which is n!.
# Although some of the strings may be duplicates, the program cannot know this ahead of time and so it will still generate n! different strings.

# Solution 4: Count and Compare

# Our final solution to the anagram problem takes advantage of the fact that any two anagrams will have the same number of a’s, 
# the same number of b’s, the same number of c’s, and so on. 
# In order to decide whether two strings are anagrams, we will first count the number of times each character occurs. 
# Since there are 26 possible characters, we can use a list of 26 counters, one for each possible character. 
# Each time we see a particular character, we will increment the counter at that position. 
# In the end, if the two lists of counters are identical, the strings must be anagrams.

# Unlike the first solution, none of them are nested. 
# The first two iterations used to count the characters are both based on n. 
# The third iteration, comparing the two lists of counts, always takes 26 steps since there are 26 possible characters in the strings. 
# Adding it all up gives us T(n)=2n+26T(n)=2n+26 steps. 
# That is O(n). 
# We have found a linear order of magnitude algorithm for solving this problem.

# Although this solution was able to run in linear time, it could only do so by using additional storage to keep the two lists of character counts. 
# In other words, this algorithm sacrificed space in order to gain time.
# This is a common occurrence. On many occasions you will need to make decisions between time and space trade-offs.

def anagramSolution4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

print(anagramSolution4('apple','pleap'))























