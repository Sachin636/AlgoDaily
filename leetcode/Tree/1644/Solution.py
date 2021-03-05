# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.find = 0

        def lca(root, p, q):
            if not root:
                return None

            a, b = lca(root.left, p, q), lca(root.right, p, q)

            if root.val == p.val or root.val == q.val:
                self.find += 1
                return root

            if a and b:
                return root

            return a if a else b

        ans = lca(root, p, q)
        if self.find < 2:
            return None
        else:
            return ans
