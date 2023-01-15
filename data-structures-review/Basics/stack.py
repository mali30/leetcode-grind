from collections import deque

class Stack():
     def __init__(self):
         self.items = []

    # Average - O(N)
     def push(self, item):
         self.items.append(item)

    # Time - O(1)
     def pop(self):
         self.items.pop()

     def isEmpty(self):
         return self.items == []

     def peek(self):
         if not self.isEmpty():
             return self.items[-1]

     def getItems(self):
         return self.items


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.push(1)
my_stack.push(2)
print(my_stack.peek())
print(my_stack.getItems())
print(my_stack.isEmpty())



class anotherStack:
    def __init__(self):
        self.items = []

    def append_to_stack(self, item):
        self.items.append(item)
    
    def pop_from_stack(self):
        self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if self.items is not None:
            return self.items[-1]
    
    def get_items(self):
        return self.items

# double endede queue -> uses doubly linked list. faster than using list since it stores each node in individual block vs contingious list
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()
stack.pop()
stack.pop()
stack.append(4)
stack.append(5)
stack.append(6)

print(stack)
