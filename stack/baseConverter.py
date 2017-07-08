# But how can we easily convert integer values into binary numbers? 
# The answer is an algorithm called “Divide by 2” that uses a stack to keep track of the digits for the binary result.

# The Divide by 2 algorithm assumes that we start with an integer greater than 0. 
# A simple iteration then continually divides the decimal number by 2 and keeps track of the remainder. 
# The first division by 2 gives information as to whether the value is even or odd. 
# An even value will have a remainder of 0. It will have the digit 0 in the ones place. 
# An odd value will have a remainder of 1 and will have the digit 1 in the ones place. 
# We think about building our binary number as a sequence of digits; the first remainder we compute will actually be the last digit in the sequence. 

from pythonds.basic.stack import Stack

def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

print(divideBy2(42))

# The algorithm for binary conversion can easily be extended to perform the conversion for any base. 
# The most common of these are binary, octal (base 8), and hexadecimal (base 16).

def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(25,2))
print(baseConverter(25,16))