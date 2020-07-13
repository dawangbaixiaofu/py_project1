class TreeNode:
    def __int__(self,x):
        self.val = x
        self.left = None
        self.right = None

class solution:
    def middleOrderTraversal(self,root:TreeNode):
        if not root:
            return []
        ans = []
        ans += self.middleOrderTraversal(root.left)
        ans.append(root.val)
        ans += self.middleOrderTraversal(root.right)
        return ans