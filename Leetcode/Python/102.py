# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        levels = []
        q = [root]
        while q:
            level = []
            N = len(q)
            for i in range(N):
                u = q.pop(0)
                if u:
                    level.append(u.val)
                    q.append(u.left)
                    q.append(u.right)
            if level:
                levels.append(level)
        return levels