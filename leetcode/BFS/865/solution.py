# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def lca(root: TreeNode, p: int, q: int) -> TreeNode:
            if not root:
                return None

            if root.val == p or root.val == q:
                return root

            a, b = lca(root.left, p, q), lca(root.right, p, q)

            if a and b:
                return root

            return a if a else b

        levels = {}
        deep = 0
        queue = [[root, 0]]

        while queue:

            node, level = queue.pop(0)
            if level > deep:
                deep = level
            if level not in levels:
                levels[level] = [node]
            else:
                levels[level].append(node)

            if node.left:
                queue.append([node.left, level+1])
            if node.right:
                queue.append([node.right, level+1])

        if levels[deep] == 1:
            return levels[deep][0]
        else:
            p = levels[deep][0].val
            q = levels[deep][-1].val
            return lca(root, p, q)
