#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right     

from collections import deque
class Solution:
    def isSymetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def isSymetric(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return isSymetric(left.left, right.right) and isSymetric(left.right, right.left)
        return isSymetric(root.left, root.right)