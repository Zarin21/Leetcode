# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

# I used a depth-first search (DFS) approach to calculate the maximum depth of the binary tree.
# Starting from the root node, I recursively traversed down to each leaf node,
# keeping track of the current depth. At each node, I compared the depths of the left
# and right subtrees and returned the maximum depth found.

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
                       
        return dfs(root, 0)

    # Time Complexity: O(n), where n is the number of nodes in the tree.
    # Space Complexity: O(h), where h is the height of the tree, due to the recursion stack.