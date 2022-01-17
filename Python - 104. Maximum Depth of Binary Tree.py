# Python - 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
            
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        else:
            maxLeft = self.maxDepth(root.left)
            maxRight = self.maxDepth(root.right)
            
            if maxLeft > maxRight:
                return maxLeft  + 1
            else:
                return maxRight + 1
