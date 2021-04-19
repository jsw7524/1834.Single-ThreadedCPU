import heapq

class Event(object):
    def __init__(self,time,index,content,description):
        self.time=time
        self.index=index
        self.content=content
        self.description=description
    def __lt__(self, nxt):
        return self.time < nxt.time

class Job(object):
    def __init__(self,processTime,index,task):
        self.processTime=processTime
        self.index=index
        self.task=task
    def __lt__(self, nxt):
        if self.processTime == nxt.processTime:
            return self.index < nxt.index
        return self.processTime < nxt.processTime

class Solution(object):
    def __init__(self):
        self.isIdle=True
        self.order = []
        self.waitingQueue = []
        self.events = None

    def processEvent(self, event):
        currentTime = event.time
        if event.description == "AvailableTask":
            heapq.heappush(self.waitingQueue,  Job(processTime=event.content[1],index=event.index,task=event.content))  # processTime index task
            while len(self.events) > 0:
                if self.events[0].time == currentTime:
                    self.processEvent(heapq.heappop(self.events))
                else:
                    break
        elif event.description == "FinishedTask":
            self.isIdle = True
            pass

        if len(self.waitingQueue) > 0 and self.isIdle == True:
            newJob = heapq.heappop(self.waitingQueue)
            self.isIdle = False
            heapq.heappush(self.events,  Event(time=currentTime + newJob.processTime, index=-1, content=None , description="FinishedTask"))
            self.order.append(newJob.index)


    def getOrder(self, tasks):
        self.events = [Event(time=task[0], index=index, content=task, description="AvailableTask") for index, task in enumerate(tasks)]
        heapq.heapify(self.events)
        while len(self.events) > 0:
            nextEvent=heapq.heappop(self.events)
            self.processEvent(nextEvent)
        return self.order


sln = Solution()
assert [0,2,3,1] == sln.getOrder(tasks=[[1, 2], [2, 4], [3, 2], [4, 1]])

sln = Solution()
assert [4,3,2,0,1] ==sln.getOrder(tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]])

sln = Solution()
assert [6,1,2,9,4,10,0,11,5,13,3,8,12,7] ==sln.getOrder(tasks = [[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]])