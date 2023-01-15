class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

class Traversal: 
    def preOrder(self, root):
        if root is None:
            return 
        
        print(root.value)
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if root is None:
            return
        
        self.preOrder(root.left)
        print(root.value)
        self.preOrder(root.right)

    def postOrder(self, root):
        if root is None:
            return
        
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.value)


root = TreeNode(0)
first = TreeNode(1)
second = TreeNode(2)
third = TreeNode(3)
fourth = TreeNode(4)

root.left = first 
root.right = second 
first.left = third 
second.right = fourth 

traversal = Traversal()

traversal.preOrder(root)
print('############')
traversal.inOrder(root)
print('############')
traversal.postOrder(root)

