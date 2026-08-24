# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        currentDepth = 0

        def dfs(node) -> int:

            
            if not node:
                return 0 
            
            left_depth = dfs(node.left)
            print(left_depth)
            right_depth = dfs(node.right)

            


            return 1 + max(left_depth,right_depth)

        maxDepth = dfs(root)
        return maxDepth