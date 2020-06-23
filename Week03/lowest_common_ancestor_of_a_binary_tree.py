def lowestCommonAncestor(self, root, p, q):
    if not root or root == p or root == q:
        return root

    leftTree = self.lowestCommonAncestor(root.left, p, q)
    rightTree = self.lowestCommonAncestor(root.right, p, q)

    if not leftTree:
        return rightTree
    if not rightTree:
        return leftTree
    return root
