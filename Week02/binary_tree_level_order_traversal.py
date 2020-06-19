import collections


def levelOrder(self, root) -> list[list[int]]:
    if not root: return []

    res = []
    queue = collections.deque()
    queue.append(root)
    while queue:
        levelSize, currentLevel = len(queue), []
        for _ in range(levelSize):
            node = queue.popleft()
            currentLevel.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(currentLevel)
    return res
