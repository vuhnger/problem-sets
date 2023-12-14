
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None"""

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return ''

        tree = []
        queue = deque([(root, 0)]) # Putt node + indeks i kø/liste

        while queue:
            node, i = queue.popleft()
            tree.append('{}.{}'.format(i, node.val))

            if node.left:
                queue.append((node.left, (i << 1) + 1))  # Venstre indeks
            if node.right:
                queue.append((node.right, (i << 1) + 2))  # Høyre indeks

        return '\t'.join(tree) 

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None

        mapping = {
            int(pair.split('.')[0]): int(pair.split('.')[1])
            for pair in data.split('\t') if pair
        }

        def build_tree(mapping, i):
            if i not in mapping:
                return None

            node = TreeNode(mapping[i])
            node.left = build_tree(mapping, (i << 1) + 1)
            node.right = build_tree(mapping, (i << 1) + 2)
            return node

        return build_tree(mapping, 0)

# Usage
# ser = Codec()
# deser = Codec()
# tree = deser.deserialize(ser.serialize(root))
