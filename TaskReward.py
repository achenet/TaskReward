class Task:
    '''This is a class to create task objects'''
    def __init__(self):        #do I need to make any of these variables non local or global?
        #will try just making them local and if needed modify them
        self.name = input("Please enter task name ")
        self.reward = input("Please enter what the reward one task completion is ")
        self.min = input("Please enter what the minimum number of tasks completed to have a reward is ")
        self.max = input("Please enter what the maximum total reward for tasks of this type can be ")







numberOfTasks = int(input("How many tasks are there? "))
taskList = []
for i in range(numberOfTasks):
    taskList.append(Task())


for i in taskList:
    print(i.name)
    print(i.reward)
    print(i.min)
    print(i.max)
