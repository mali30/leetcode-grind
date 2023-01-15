# class Node(object):
#     def __init__(self,data=None,next_node=None):
#         self.data = data
#         self.next_node = next_node

#     def getData(self):
#         return self.data
    
#     def getNextNode(self):
#         return self.next_node

#     def setNextNode(self, new_node):
#         self.next_node = new_node


# class LinkList(object):
#     def __init__(self,head = None):
#         self.head = head
    
#     # Time : O(1)
#     def insert(self,data):
#         # first create a new node
#         new_node = Node(data)
#         # set that nodes next to the current head 
#         new_node.setNextNode(self.head)
#         # set new_node as the head 
#         self.head = new_node
#     # Time - O(N)
#     def size(self):
#         current = self.head
#         count = 0
#         while current:
#             count+=1
#             current = current.getNextNode()
#         return count
    
#     # Time - O(N)
#     def search(self,data):
#         current = self.head
#         found = False
#         while current and found:
#             if current.getData() == data:
#                 found = True
#             else:
#                 current = current.getNextNode()
#             if current is None:    
#                 raise ValueError("Data not in list")
#         return current

#     # Time - O(N)
#     def delete(self, target):
#         current = self.head
#         previous = None
#         while current and current.getData() != target:
#             previous = current
#             current = current.getNextNode()
#         if current == target:
#              previous = current.getNextNode()
#         if current is None:
#             raise ValueError("Data not in list")
#         if previous is None:
#             self.head = current.getNextNode()
#         else:
#             previous.setNextNode(current.getNextNode())
#             current = current.getNextNode()
    
#     # Time - O(N)
#     def iterItems(self):
#         my_list = []
#         current = self.head
#         while current:
#             my_list.append(current.getData())
#             current =current.getNextNode()
#         print(my_list)





                


# # ll = LinkList()
# # ll.insert(1)
# # ll.insert(2)
# # ll.insert(3)
# # ll.insert(4)
# # ll.insert(5)
# # ll.delete(5)

# # ll.iterItems()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# class Node():
#     def __init__(self , data=None):
#         self.next = None
#         self.data = data 
    
    
#     # def setNewData(self, created_node):
#     #     self.next_node = created_node
    
#     # def getData(self):
#     #     return self.data
    
#     # def getNextNode(self):
#     #     return self.next_node


# class LinkListClass():

#     def __init__(self):
#         self.head = None

#     def addLink(self, createdNode):
#         # if their is no no node in the list
#         my_node = Node(createdNode)

#         if self.head is None:
#             self.head =  my_node
#             return

#         current_node = self.head 
#         while current_node.next:
#             current_node = current_node.next
#         current_node.next = my_node
#         # if there are already nodes


#     def getLengthOfLink(self):
#         value = 0
#         current = self.head 
#         while current:
#             value += 1
#             current = current.next
#         return value 

#     def search(self,value_search):
#         head = self.head 
#         not_found = False 
#         while head and not_found:
#             if head.data == value_search:
#                 not_found = True 
#             else:
#                 head = head.next
#         if head is None:
#             return "Error getting Node"
#         elif head is not_found:
#             print("Looks like its here not here buddy")
#         return head.data

#     # two cases - if head is node you want to delete
#             #   - if head is not which is all other nodes
#     def deleteLink(self , target):

#         current = self.head
#         if current is None:
#             return 

#         if current and current.data == target:
#             self.head = current.next
#             current = None 
#             return 
        
#         previous_node = None
#         current = self.head  
          
#         while current and current.data != target:
#             previous_node = current
#             current = current.next
#         previous_node = current.next
#         current = None 
    
#     def printList(self):
#         current = self.head 
#         while current:
#             print(current.data)
#             current = current.next


# ll = LinkListClass()
# ll.addLink(1)
# ll.addLink(2)
# ll.addLink(3)
# ll.addLink(4)
# ll.addLink(5)
# # print(ll.getLengthOfLink())
# print(ll.search(20))
# ll.printList()
# ll.deleteLink(3)
# ll.deleteLink(2)

# print(ll.getLengthOfLink())

    


# anotherLinkList

# class Node:
#     def __init__(self, data, next_node):
#         self.data = data
#         self.next_node = next_node
#         self.size = 0
    
#     def getNextNode(self):
#         return self.next_node
    
#     def setNextNode(self, item):
#         self.next_node = item
    
#     def getData(self):
#         self.data
    
#     def setData(self, item):
#         self.data = item
        
#     def returnSize(self):
#         return self.size


# class LinkList:
#     def __init__(self, head = None):
#         self.head = head
#         self.size = 0
    
#     def createNode(self, item):
#         new_node = Node(item , self.head)
#         self.head = new_node
#         self.size+=1
    
#     def printList(self):
#         current = self.head
#         while current:
#             print(current.data)
#             current = current.getNextNode()

#     def getSize(self):
#         return self.size
    


# my_link = LinkList()
# my_link.createNode(1)
# my_link.createNode(2)
# my_link.createNode(3)
# my_link.createNode(4)
# my_link.printList()
# print(my_link.getSize())





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkList:
    def __init__(self, head):
        self.head = head
    
    def append_node(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            self.next = item
    
        