# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # Using recursion to check if two binary trees are the same
        # Two binary trees are considered the same if they are structurally identical

        if p == None and q == None:
            return True
        if (p == None and q != None) or (p != None and q == None):
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False
        # Time complexity: O(min(m,n)) where m and n are the number of nodes in the two trees
        # Space complexity: O(h) where h is the height of the tree due to the
