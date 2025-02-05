# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    # If both trees are empty, they are the same
    if not p and not q:
        return True
    # If one of the trees is empty, they are not the same
    if not p or not q:
        return False
    # If the values of the current nodes are different, they are not the same
    if p.val != q.val:
        return False
    # Recursively check the left and right subtrees
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# Test cases
# Tree 1
#     1
#    / \
#   2   3
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)

# Tree 2
#     1
#    / \
#   2   3
tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

# Tree 3
#     1
#    / \
#   2   4
tree3 = TreeNode(1)
tree3.left = TreeNode(2)
tree3.right = TreeNode(4)

print(isSameTree(tree1, tree2))  # True
print(isSameTree(tree1, tree3))  # False