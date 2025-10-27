# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


# I used a recursive approach to invert the binary tree.
# For each node, I swapped its left and right children,
# and then recursively called the same function on the left and right subtrees.
# This process continues until all nodes have been processed, effectively inverting the entire tree.

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 0
        
        temp = root.left
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
    # Time Complexity: O(n), where n is the number of nodes in the tree.
    # Space Complexity: O(h), where h is the height of the tree, due to the recursion stack.