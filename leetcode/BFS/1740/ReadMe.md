Given the root of a binary tree and two integers p and q, return the distance between the nodes of value p and value q in the tree.

The distance between two nodes is the number of edges on the path from one to the other.

Constraints:

- The number of nodes in the tree is in the range [1, 104].
- 0 <= Node.val <= 109
- All Node.val are unique.
- p and q are values in the tree.

Idea:

Find the LCA and add the distance between p and q between lca.
