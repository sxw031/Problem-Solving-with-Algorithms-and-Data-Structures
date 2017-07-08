import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'
## Assumptions:
# our maze is divided up into "squares". Each square of the maze is either open or occupied by a section of wall.
# The turtle can only pass through the open squares of the maze.
# If the turtle bumps into a wall it must try a different direction.

## Procedures:
# 1. From our starting position we will first try going North one square and then recursively try our procedure from there
# 2. If we are not successful by trying a Northern path as the first step then we will take a step to the South and recursively repeat our procedure.
# 3. If South does not work then we will try a step to the West as our first step and recursively apply our procedure.
# 4. If North, South, and West have not been successful then apply the procedure recursively from a position one step to our East.
# 5. If none of these directions works then there is no way to get out of the maze and we fail.

## Detail:(backing up)
# we must also have a stragety to remember where we have been, otherwise the turtle can trap in a infinite loop like going from original to north and take a south to the orginal if there is a wall in second move.
# In this case, we assume that we have a bag of bread crumbs we can drop along our way. 
# If we take a step in a certain direction and find that we have a bag of bread crumbs already on that square, we know that we should immediately back up and try the next direction in our procedure. 
# backing up is as simple as returning from a recursive function call.

## Four base cases:
# 1. The turtle has run into a wall. Since the square is occupied by a wall no further exploration can take place.
# 2. The turtle has found a square that has already been explored. We do not want to continue exploring from this position or we will get into a loop.
# 3. We have found an outside edge, not occupied by a wall. In other words we have found an exit from the maze.
# 4. We have explored a square unsuccessfully in all four directions.

## represent the Maze:
# Maze class: 
# use the turtle module to draw and explore our maze so we can watch this algorithm in action.
class Maze:
	# The __init__ method takes the name of a file as its only parameter.
	# This file is a text file that represents maze by using "+" characters for wall, " " for open squares, "S" to indicate the starting position
    def __init__(self,mazeFileName):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        mazeFile = open(mazeFileName,'r')
        rowsInMaze = 0
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col = col + 1
            rowsInMaze = rowsInMaze + 1
            self.mazelist.append(rowList)
            columnsInMaze = len(rowList)

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze/2
        self.yTranslate = rowsInMaze/2
        self.t = Turtle(shape='turtle')
        setup(width=600,height=600)
        setworldcoordinates(-(columnsInMaze-1)/2-.5,
                            -(rowsInMaze-1)/2-.5,
                            (columnsInMaze-1)/2+.5,
                            (rowsInMaze-1)/2+.5)

    # uses this internal representation to draw the initial view of the maze on the screen.
	def drawMaze(self):
	    for y in range(self.rowsInMaze):
	        for x in range(self.columnsInMaze):
	            if self.mazelist[y][x] == OBSTACLE:
	                self.drawCenteredBox(x+self.xTranslate,
	                                     -y+self.yTranslate,
	                                     'tan')
	    self.t.color('black','blue')

	def drawCenteredBox(self,x,y,color):
	    tracer(0)
	    self.t.up()
	    self.t.goto(x-.5,y-.5)
	    self.t.color('black',color)
	    self.t.setheading(90)
	    self.t.down()
	    self.t.begin_fill()
	    for i in range(4):
	        self.t.forward(1)
	        self.t.right(90)
	    self.t.end_fill()
	    update()
	    tracer(1)

	# helper function for updatePosition method to update the view on the screen
	def moveTurtle(self,x,y):
	    self.t.up()
	    self.t.setheading(self.t.towards(x+self.xTranslate,
	                                     -y+self.yTranslate))
	    self.t.goto(x+self.xTranslate,-y+self.yTranslate)

	# helper function for updatePosition method to update the view on the screen
	def dropBreadcrumb(self,color):
	    self.t.dot(color)

	# uses the same representation to see if the turtle has run into a wall
	# it also updates the representation with a "."  or "-" to indicate that the turtle has visited a particular square of if the square is part of a dead end.
	def updatePosition(self,row,col,val=None):
	    if val:
	        self.mazelist[row][col] = val
	    self.moveTurtle(col,row)

	    if val == PART_OF_PATH:
	        color = 'green'
	    elif val == OBSTACLE:
	        color = 'red'
	    elif val == TRIED:
	        color = 'black'
	    elif val == DEAD_END:
	        color = 'red'
	    else:
	        color = None

	    if color:
	        self.dropBreadcrumb(color)

	def isExit(self,row,col):
    	return (row == 0 or
            row == self.rowsInMaze-1 or
            col == 0 or
            col == self.columnsInMaze-1)

	def __getitem__(self,idx):
    	return self.mazelist[idx]

def searchFrom(maze, startRow, startColumn):
	# first step to update the position, this is simply to help you visuallize the algorithm
    maze.updatePosition(startRow, startColumn)
   #  Check for base cases:
   #  1. We have run into an obstacle(wall), return false
   if maze[startRow][startColumn] == OBSTACLE :
        return False
    #  2. Has the turtle circled back to a square already explored?
    if maze[startRow][startColumn] == TRIED:
        return False
    # 3. Success, Has the turtle found an exit
    if maze.isExit(startRow,startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True
    maze.updatePosition(startRow, startColumn, TRIED)

    # Otherwise, we continue to search use logical short circuiting to try each
    # direction in turn (if needed),  
    # If there is not a good path leading out of the maze to the North then the next recursive call is tried, this one to the South. If South fails then try West, and finally East.
    found = searchFrom(maze, startRow-1, startColumn) or \
            searchFrom(maze, startRow+1, startColumn) or \
            searchFrom(maze, startRow, startColumn-1) or \
            searchFrom(maze, startRow, startColumn+1)
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)
    return found

myMaze = Maze('maze2.txt')
myMaze.drawMaze()
myMaze.updatePosition(myMaze.startRow,myMaze.startCol)

searchFrom(myMaze, myMaze.startRow, myMaze.startCol)


# Post work: Self Check
# Modify the maze search program so that the calls to searchFrom are in a different order. 
# Watch the program run. Can you explain why the behavior is different? 
# Can you predict what path the turtle will follow for a given change in order?


