# chanllege: whether the printer is capable of handling a certin amount of work


### Simulation Steps:
# 1. create a queue of print tasks. Each task will be given a timestamp upon its arrival. The queue is empty to start.
# 2. For each second:
#    a. Does a new print task get created? if so, add it to the queue with the currentSecond as the the timestamp
#    b. If the printer is not busy and if a task is waiting:
#       i. Remove the next task from the print queue and assign it to the print
#       ii. Substract the timestamp from the currentSecond to compute the waiting time for that task.
#       iii. Append the waiting time for that task to a list for later processing.
#       iv. Based on the number of pages in the print task, figure out how much time will be required.
#    c. The printer now does one second of printing if necessary. It also substracts one second from the time required for that task.
#    d. If the task has been completed, in other words the time required has reached zero, the printer is no longer busy.
# 3. After the simulation is complete, compute the average waiting time from the list of waiting times generated.

### Implementation
import random
# create three classes for the three real-world objects: Printer, Task, PrintQueue.

class Printer:
	def __init__(self, ppm):
		self.pagerate = ppm
		self.currentTask = None
		self.timeRemaining = 0

	def tick(self):
		"""decrements the internal timer and sets the printer to idle if the task is completed"""
		if self.currentTask != None:
			self.timeRemaining = self.timeRemaining - 1
			if self.timeRemaining <= 0:
				self.currentTask = None

	def busy(self):
		if self.currentTask != None:
			return True
		else:
			return False

	def startNext(self, newtask):
		self.currentTask = newtask
		self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task:
	def __init__(self, time):
		self.timestamp = time
		self.pages = random.randrange(1,21)

	def getStamp(self):
		return self.timestamp

	def getPages(self):
		return self.pages

	def waitTime(self, currenttime):
		return currenttime - self.timestamp

class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self):
		self.items.insert(0, items)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

### main implementation
# The printQueue object is an instance of our existing queue ADT.
# newPrintTask decides whether a new printing task has been created.
# print task arrive once every 180 second. By arbitrarily choosing 180 from the range of ranfom integers, we can simulate this random event.
# the simulation function allows us to set the total time and the pages per minute for the printer.
# pagesPerMinute represent the printing rate of the printer
# numSeconds represent the number of seconds we are trying to simulate.


def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

      if newPrintTask():
         task = Task(currentSecond)
         printQueue.enqueue(task)

      if (not labprinter.busy()) and (not printQueue.isEmpty()):
        nexttask = printQueue.dequeue()
        waitingtimes.append(nexttask.waitTime(currentSecond))
        labprinter.startNext(nexttask)

      labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

# If there are 10 students in the lab and each prints twice, then there are 20 print tasks per hour on average.
# given it in second, it is one task per 180 seconds.
def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5)


## Post work
# We were trying to answer a question about whether the current printer could handle the task load if it were set to print with a better quality but slower page rate. 
# The approach we took was to write a simulation that modeled the printing tasks as random events of various lengths and arrival times.

# The output above shows that with 5 pages per minute printing, the average waiting time varied from a low of 17 seconds to a high of 376 seconds (about 6 minutes). 
# With a faster printing rate, the low value was 1 second with a high of only 28. 
# In addition, in 8 out of 10 runs at 5 pages per minute there were print tasks still waiting in the queue at the end of the hour.

# Therefore, we are perhaps persuaded that slowing the printer down to get better quality may not be a good idea. 
# Students cannot afford to wait that long for their papers, especially when they need to be getting on to their next class. 
# A six-minute wait would simply be too long.

# This type of simulation analysis allows us to answer many questions, commonly known as “what if” questions. 
# All we need to do is vary the parameters used by the simulation and we can simulate any number of interesting behaviors. For example,

# What if enrollment goes up and the average number of students increases by 20?
# What if it is Saturday and students are not needing to get to class? Can they afford to wait?
# What if the size of the average print task decreases since Python is such a powerful language and programs tend to be much shorter?
# These questions could all be answered by modifying the above simulation. However, it is important to remember that the simulation is only as good as the assumptions that are used to build it. 
# Real data about the number of print tasks per hour and the number of students per hour was necessary to construct a robust simulation.

## Self Check
# How would you modify the printer simulation to reflect a larger number of students? 
# Suppose that the number of students was doubled. 
# You make need to make some reasonable assumptions about how this simulation was put together but what would you change? 
# Modify the code. Also suppose that the length of the average print task was cut in half. Change the code to reflect that change.
# Finally How would you parametertize the number of students, rather than changing the code we would like to make the number of students a parameter of the simulation.





