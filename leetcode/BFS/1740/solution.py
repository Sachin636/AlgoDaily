# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        def lca(root: TreeNode, p, q) -> TreeNode:
            if not root:
                return None

            if root.val == p or root.val == q:
                return root

            a, b = lca(root.left, p, q), lca(root.right, p, q)

            if a and b:
                return root

            return a if a else b

        def distance(root, key):
            q = [[root, 0]]
            while q:
                n, d = q.pop(0)
                if n.val == key:
                    return d

                if n.left:
                    q.append([n.left, d+1])
                if n.right:
                    q.append([n.right, d+1])

            return -1

        ancestor = lca(root, p, q)
        return distance(ancestor, p) + distance(ancestor, q)
