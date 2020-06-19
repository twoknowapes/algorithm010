def levelOrder(self, root: 'Node') -> list[list[int]]:
    if root is None: return []

    res, queue = [], [root]
    while queue:
        child, node = [], []
        for item in queue:
            child.append(item.val)
            if item.children: node += item.children
        res.append(child)
        queue = node
    return res
