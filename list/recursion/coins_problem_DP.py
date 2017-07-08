### Background
# What is the smallest number of coins you can use to make change?
# we can solve it by greedy method, assume we have 1,5,10,25 cent coins which we use in US
# but imagine we also have 21 cent coins, like the vending machine in Lower Elbonia

### Solve it by recursive function
# If we are trying to make change for the same amount as the value of one of our coins, the answer is one coin.
# If the amount does not match we have several options. 
# What we want is the minimum of a penny(or a nickel, or a dime and so on) plus the number of coins needed to make change for the original amount minus a penny
def recMC(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]: # we filter the list of coins to those less than the current value of change using a list comprehension.
         numCoins = 1 + recMC(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins

print(recMC([1,5,10,25],63))

### Analysis the problem - improving with memoization
# it is extrememely inefficient: we are re-doing too many calculations
# For example to calculate the change for 26 cents, we recalculate the change for 15 cents at least three times, and each of these computation to find the optimal number of coins of 15 cents itself takes 52 function calls.
# A simple solution is to store the result for the minimum number of coins in a table when we find them.
# This is not dynamic programming, but memoization or "caching"

def recDC(coinValueList,change,knownResults):
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   return minCoins

print(recDC([1,5,10,25],63,[0]*64))

### Dynamic Programming
# a more systematic approach to the problem.
# start with making change for one cent and systematically work its way up to the amount of change we require
# This guarantees us that at each step of the algorithm we already known the minimum number of coins needed to make change for any smaller amount.
## Example for 11 cents
# starting from 1 cents to 11 cents, and 1-4 cents are easy.
# at 5 cents, we have two options five pennies or one nickel.
# we consult the table and see that the number of coins needed to make change for four coins is four, plus one more to make five; 
# or we can look at 0 cents plus one nickel to make five. since the minimum of (1 and 5) is 1, we store 1 here at table
# at 11 cents, we have three conditions:
# 11 - 1 = 10 cents (1); 11 - 5  = 6 cents(2); 11 - 10 = 1 cent(1)

# Note that deMakeChange is not a recursive function, even though we started with a recursive solution to the problem.
# It is important to realize that just because you can write a recursive solution to a problem does not mean it is the best or most efficicent solution.

def dpMakeChange(coinValueList,change,minCoins):
   for cents in range(change+1):
      coinCount = cents
      for j in [c for c in coinValueList if c <= cents]: # the bulk of the work, we consider using all possible coins to make change for the amount specified by cents
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
      minCoins[cents] = coinCount # remember the minimum value and store it in our minCoins list.
   return minCoins[change]

### Even better
# Although our making change algorithm does a good job of configuring out the minimum number of coins, it does not help us make change since we do not keep track of the coins we use.
# We can easily extend the function above to keep track of the coins used by simply remembering the last coin we add for each entry in the minCoins table
# If we know the last coin added, we can simply substract the value of the coin to find a previous entry in the table that tells us the last coin we added to make that amount.
# we can keep tracking back through the table until we get to the beginning.

def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()






