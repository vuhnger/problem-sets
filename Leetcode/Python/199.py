# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        level = []
        q = [root]

        while q:
            N = len(q)
            for i in range(N):
                u = q.pop(0)
                if i == N-1:
                    level.append(u.val)

                if u.left:
                    q.append(u.left)
                if u.right:
                    q.append(u.right)
        return level