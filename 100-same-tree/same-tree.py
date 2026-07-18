# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preOrderTraversal(self, root):
        res = []

        def preOrder(node):
            if node is None:
                res.append(None)
                return
            res.append(node.val)
            preOrder(node.left)
            preOrder(node.right)
        preOrder(root)
        return res

    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        a = self.preOrderTraversal(p)
        b = self.preOrderTraversal(q)
        if a==b:
            return True
        return False
