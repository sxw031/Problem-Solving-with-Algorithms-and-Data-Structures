import turtle

######## Example 1 ##########
myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,100)
myWin.exitonclick()

####### Example 2 #########
# The definition of a fractal is that when you look at it the fractal has the same basic shape no matter how much magnify it.
# Some example are: coastlines, continents, snowflakes, mountains, trees or shrubs.
# with this idea, we can say that a tree is a trunk, with a smaller tree going off to the right and another smaller tree going off to the left.
# notice that each time we make a recursive call to tree we substract some amount from the branchLen parameter; this is to make sure that the recursive trees get smaller and smaller.

def tree(branchLen, t):
	## a check for the base case
	if branchLen > 5:
		t.forward(branchLen)
		t.right(20)
		# recursive call right after the turtle turns to the right by 20 degrees; this is the right tree mentioned above.
		tree(branchLen-15,t)
		t.left(40)
		# another recursive call, this time turning left by 40 degrees.
		tree(branchLen-15,t)
		t.right(20)
		t.backward(branchLen)

def main():
	t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

######## modification #######
# Modify the recursive tree program using one or all of the following ideas:
# Modify the thickness of the branches so that as the branchLen gets smaller, the line gets thinner.
# Modify the color of the branches so that as the branchLen gets very short it is colored like a leaf.
# Modify the angle used in turning the turtle so that at each branch point the angle is selected at random in some range. For example choose the angle between 15 and 45 degrees. Play around to see what looks good.
# Modify the branchLen recursively so that instead of always subtracting the same amount you subtract a random amount in some range.

def tree(branchLen,t):
    if branchLen > 5:
        if branchLen < 20:
            t.color("red")
        angle = random.randint(15,45)
        shorter = random.randint(5,20)
        t.forward(branchLen)
        t.right(angle)
        tree(branchLen-shorter,t)
        t.left(2*angle)
        tree(branchLen-shorter,t)
        t.right(angle)
        t.backward(branchLen)
        t.color("green")
