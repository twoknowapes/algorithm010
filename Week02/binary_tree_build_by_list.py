class BinaryTree:
    def binaryTree(self, root: list[int]):
        return [root, [], []]

    def insertLeft(self, root: list[int], newBranch):
        t = root.pop(1)
        if len(t) > 1:
            root.insert(1, [newBranch, t, []])
        else:
            root.insert(1, [newBranch, [], []])

    def insertRight(self, root: list[int], newBeanch):
        t = root.pop(2)
        if len(t) > 1:
            root.insert(2, [newBeanch], [], t)
        else:
            root.insert(2, [newBeanch, [], []])

    def getRootVal(self, root):
        return root[0]

    def setRootVal(self, root, newVal):
        root[0] = newVal

    def getLeftChild(self, root):
        return root[1]

    def getRightChild(self, root):
        return root[2]
