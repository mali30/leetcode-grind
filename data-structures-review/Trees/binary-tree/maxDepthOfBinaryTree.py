# Definition for a binary tree node.
"""Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        # if we have reach a leaf node we return 0 to denote 
        if root is None:
            return 0
        
        leftMax = self.maxDepth(root.left) + 1
        rightMax = self.maxDepth(root.right) + 1

    
        return max(leftMax, rightMax)
            

root = TreeNode(3)
first = TreeNode(9)
second = TreeNode(20)
third = TreeNode(15)
fourth = TreeNode(7)

root.left = first 
root.right = second 
second.left = third
second.right = fourth 

sol = Solution()

print(sol.maxDepth(root))