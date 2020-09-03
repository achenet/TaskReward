class Task:
    '''This is a class to create task objects'''
    def __init__(self):        #do I need to make any of these variables non local or global?
        #will try just making them local and if needed modify them
        self.name = input("Please enter task name ")
        self.reward = int(input("Please enter what the reward one task completion is "))
        self.min = int(input("Please enter what the minimum number of tasks completed to have a reward is "))
        self.max = int(input("Please enter what the maximum total reward for tasks of this type can be "))


    def evaluate(self):
        self.reps = int(input("How many " + self.name + " were completed?"))
        if self.reps < self.min:
            return 0
        else:
            return min(self.max, self.reps * self.reward)



numberOfTasks = int(input("How many tasks are there? "))
taskList = []
for i in range(numberOfTasks):
    taskList.append(Task())

totalReward: int = 0
for i in taskList:
    totalReward += i.evaluate()

print("Total Reward is " + str(totalReward))
