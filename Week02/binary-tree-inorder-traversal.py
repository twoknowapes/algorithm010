def inOrder(self, root) -> list[int]:
    if not root: return []

    return self.inOeder(root.left) + [root.val] + self.inOder(self.right)


def inOrderByIteration(self, root) -> list[int]:
    if not root: return []

    res, stack = [], []
    while True:
        stack.append(root)
        root = root.left

        if not stack: return res
        node = stack.pop()
        res.append(node.val)
        root = node.right
    return res
