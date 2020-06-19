def preorder(self, root: 'Node') -> list[int]:
    if not root: return None

    res, stack = [], [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.children:
            for child in node.children[::-1]:
                stack.append(child)
    return res
