def preOrder(self, root) -> list[int]:
    if not root: return []

    return [root.val] + self.preOrder(root.left) + self.preOrder(self.right)


def preOrderByIteration(self, root) -> list[int]:
    if not root: return []

    res, stack = [], [root]
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return res