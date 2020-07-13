from preOrderTraversal import TreeNode
from preOrderTraversal import solution
class solution(solution):
    def postOrderTraversal(self,root:TreeNode):
        if not root:
            return []
        ans = []
        ans += self.postOrderTraversal(root.left)
        ans += self.postOrderTraversal(root.right)
        ans.append(root.val)
        return ans
