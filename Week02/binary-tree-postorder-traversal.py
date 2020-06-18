def postOrder(self, root) -> list[int]:
    if not root: return []

    return self.postOrder(root.left) + self.postOrder(root.right) + [root.val]


def postOrderByIteration(self, root) -> list[int]:
    if not root: return []

    res, stack = [], [root]
    while stack:
        node = stack.pop()
        if node:
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
    return res[::-1]
