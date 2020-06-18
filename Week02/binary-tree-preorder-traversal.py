def preOrder(self, root: TreeNode) -> List[int]:
    if not root: return []

    return [root.val] + self.preOrder(root.left) + self.preOrder(self.right)
