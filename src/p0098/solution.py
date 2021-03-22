# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = [[root, -2 ** 31, 2 ** 31]]

        while len(queue) > 0:

            entry = queue.pop()

            root: TreeNode = entry[0]
            min_val = entry[1]
            max_val = entry[2]

            if min_val > root.val or root.val > max_val:
                return False

            if root.left:
                queue.append([root.left, min_val, root.val - 1])

            if root.right:
                queue.append([root.right, root.val + 1, max_val])

        return True
