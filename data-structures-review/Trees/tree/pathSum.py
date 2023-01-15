# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):

        return self.helper(root, targetSum)

    def helper(self, node, targetSum):
        if not node:
            return False

        # if we are at a leaf node we wanna check if we have our two sums matching
        if not node.left and not node.right and node.val == targetSum:
            return True

     
        targetSum -= node.val
        # in recursion we pass by value and not reference so each call in stack is independent
        # that means L21 will have an independent targetSum instead of subtracting from original
        return (self.helper(node.left, targetSum) or
         self.helper(node.right, targetSum))

root = TreeNode(5)
first = TreeNode(4)
second = TreeNode(8)
third = TreeNode(11)
fourth = TreeNode(13)
fifth = TreeNode(4)
sixth = TreeNode(7)
seventh = TreeNode(2)
eight = TreeNode(1)
ninth = TreeNode(4)

root.left = first 
root.right = second 
first.left = third
third.left = sixth 
third.right = seventh 
second.left = fourth
second.right = ninth
ninth.right =  eight

sol = Solution()

print(sol.hasPathSum(root, 22))