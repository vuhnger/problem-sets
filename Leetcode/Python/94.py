# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        tree = []

        def _inorder(node):
            if not node:
                return
            _inorder(node.left)
            tree.append(node.val)
            _inorder(node.right)

        _inorder(root)
        return tree