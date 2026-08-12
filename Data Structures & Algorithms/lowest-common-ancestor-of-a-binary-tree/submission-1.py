# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        current = root

        if current is None:
            return None

        if current == p or current ==q:
            return current
        
        l = self.lowestCommonAncestor(current.left, p ,q)
        r = self.lowestCommonAncestor(current.right, p ,q)
        # print(l.val,r.val,current.val)

        if l and r:
            return current
        
        return l if l else r

        