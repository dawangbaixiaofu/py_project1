class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class solution:
    def preOrderTraversal(self,root:TreeNode):
        if not root:
            return []
        ans = []
        ans.append(root.val)
        ans+=self.preOrderTraversal(root.left)
        ans+=self.preOrderTraversal(root.right)
        return ans
