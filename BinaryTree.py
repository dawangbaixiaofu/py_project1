# 树的最大深度
class solution():
    def __int__(self):
        self.res = 0
    def max_depth(self,root,depth=1):
        if not root:
            return 0
        if not root.left and not root.right:
            self.res = max(self.res,depth)
        self.max_depth(root.left,depth+1)
        self.max_depth(root.right,depth+1)
        return self.res
if __name__ == 'main':
    pass
