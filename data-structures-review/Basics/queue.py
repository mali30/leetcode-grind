from collections import deque

# using list
class Queue():
    def __init__(self):
        self.q = []

    # Time - O(N)
    def enque(self, item):
        self.q.insert(0, item)

    # Time - O(1)
    def deque(self):
        self.q.pop()

    # Time -O(1)
    def size(self):
        return len(self.q)

    def getItems(self):
        for i in self.q:
            print(i)


# myQ = Queue()
# myQ.enque(1)
# myQ.enque(2)
# myQ.enque(3)
# # myQ.getItems()
# myQ.deque()
# myQ.getItems()



# using deque 
class usingDeque:
    def __init__(self):
        self.queue = deque()

    # adds to end of queue
    def append(self, item):
        self.queue.append(item)
    
    # add to front of queue
    def appendLeft(self, item):
        self.queue.appendleft(item)
    
    # removes from end of queue
    def pop(self):
        self.queue.pop()
    
    # removes from front of queue
    def popFromLeft(self):
        self.queue.popleft()
    
    def getQ(self):
        return self.queue


my_fast_que = usingDeque()
my_fast_que.append(1)
my_fast_que.append(2)
my_fast_que.append(3)
print(my_fast_que.getQ())
