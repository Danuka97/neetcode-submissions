# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        
        res = []

        q = deque([root])

        while q:
            levl = []

            for i in range(len(q)):
                node = q.popleft()
                levl.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(levl)
        
        return res
                



        #      # Remove from front
        # q.append(node.left)     # Add to back
        # q.append(node.right) 