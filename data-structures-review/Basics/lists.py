# class List():
#     def __init__(self):
#         self.lst = []

#     # Time - O(N)
#     def app(self, item):
#         self.lst.append(item)

#     # Time - O(N)
#     def insert(self, index, item):
#         self.lst.insert(index, item)

#     # Time - O(N)
#     def pop(self):
#         return self.lst.pop()

#     def ext(self, arr):
#         self.lst.extend(arr)

#     def getLst(self):
#         return self.lst


# my_lst = List()
# my_lst.app(1)
# my_lst.app(2)
# my_lst.app(3)
# my_lst.app(4)
# print(my_lst.getLst())
# my_lst.insert(0, 5)
# print(my_lst.getLst())
# my_lst.pop()
# print(my_lst.getLst())
# my_lst.ext(['mohamed'])
# print(my_lst.getLst())

# my_list = [1, 2, 3]

# my_list.append(4)
# my_list.insert(3, "mohamed ali")
# my_list.extend([6, 7, 8])
# my_list.append(8)
# print(my_list.count(8))
# print(my_list.clear())

# # for num in my_list:
# #     print(num)

# if 'timmy' in my_list:
#     my_list.remove('timmy')
# else:
#     print('not here')


# num1 = 5
# num2 = 10
# num1, num2 = num2, num1

# print(num1, num2)


# my_list = []
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# print('slice', my_list[:])
# # gives you index position of value
# print(my_list.index(1))
# my_list.extend([4, 5, 6])
# my_list.extend("hello")
# print("count", my_list.count('l'))
# my_list.remove(6)
# print(my_list)
# my_list.reverse()
# print('reversed list', my_list)

# class MyList:
#     def __init__(self):
#         self.ll = []
    
#     def append(self, item):
#         self.ll.append(item)
    
#     def remove(self, item):
#         if item is None or item not in self.ll:
#             print('not here')
#         else:
#             self.ll.remove(item)
    
#     def remove_last(self):
#         self.ll.pop()
    
#     def check_existence(self, value):
#         if value in self.ll:
#             return True
#         return False
    
#     def check_empty(self):
#         return self.ll == []
    
#     def print_list(self):
#         print(self.ll)
    

# my_list = MyList()
# my_list.append(1)
# my_list.remove(1)
# print(my_list.check_empty())
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# print(my_list.check_existence(4))
# my_list.remove_last()
# my_list.print_list()

# first_list = [1, 2, 3]
# second_list = [4,5,6]
# print('first list', first_list)
# print('second list', second_list)
# print('combined list', first_list + second_list)

# print(['a'] * 26)

# another_list = [1, 3, 2]
# del another_list[0]
# another_list.sort()
# print(another_list)


# class List:
#     def __init__(self):
#         self.llist = []
    
#     def add(self, item):
#         self.llist.append(item)
    
#     def remove(self, item_remove):
#         if item_remove is not None:
#             self.llist.remove(item_remove)
    
#     def is_empty(self):
#         return self.llist == []
    
#     def contains(self, item):
#         return item in self.llist 
    
#     def remove_last(self):
#         if self.llist is not None:
#             llist.pop()
    
#     def insert(self, position, item):
#         if item is not None:
#             self.llist.insert(position, item)
    
#     def print_me(self):
#         for item in self.llist:
#             print(item)


# my_list = List()
# my_list.add(1)
# my_list.add(2)
# my_list.add(3)

# my_list.print_me()


# class List:
#     def __init__(self):
#         self.list = []
    
#     def append(item):
#         self.list.append(item)
    
#     def remove(item):
#         self.list.remove(item)
    
#     def contains(item):
#         if item in self.list:
#             return True 
#         return False 
    
#     def peek():
#         if self.list:
#             return self.list[-1]
    
#     def is_empty():
#         return self.list == [] 
    
#     def remove_last():
#         if self.list:
#             self.list.pop()


# add, pop, remove isEmpty removeFirst removeLast

class MyList:
    def __init__(self):
        self.arr = []
    
    def add(self, item):
        if item:
            self.arr.append(item)
    
    def pop(self):
        self.arr.pop()
    
    def remove(self, itemToRemove):
        if itemToRemove:
            self.arr.remove(itemToRemove)
    
    def isEmpty(self):
        return self.arr == []
    
    def isPopulated(self):
        return len(self.arr) > 0

    def removeFirst(self):
        if self.isPopulated():
            self.arr.remove(self.arr[0])
    
    def removeLast(self):
        if self.isPopulated():
            self.arr.pop()
    
    def print(self):
        for item in self.arr:
            print(item)
    
myList = MyList();
myList.add(1)
myList.add(2)
myList.add(3)
myList.add(4)
print(myList.isEmpty())
myList.pop()
myList.remove(3)
myList.removeFirst()

myList.print()


myList = []
myList.append(1)
myList.remove(1)
print(myList == [])
myList.extend([1,2,3,4,5])
myList.pop()

# sorted can sort lists, dictionary, tuples, and sets
sortedListReverse = sorted(myList, reverse=True)
sortedList = sorted(myList)
print('sortedListReverse', sortedListReverse)
print('sortedList', sortedList)

# sort only sorts lists
myList.sort()
myList.sort(reverse=True)
print('list', myList)