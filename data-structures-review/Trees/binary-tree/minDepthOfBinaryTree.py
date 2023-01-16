"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # if the tree is empty
        if not root:
            return 0
        
        # if we are at a leaf node then we return 1
        if not root.left and not root.right:
            return 1
        # recurse left side until its null
        leftSide = float('inf') if root.left is None else self.minDepth(root.left)
        # recurse right side until its null
        rightSide = float('inf') if root.right is None else self.minDepth(root.right)
        
        result = min(leftSide, rightSide)
        
        return result + 1
        