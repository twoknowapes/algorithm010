class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    idx = inorder.index(root.val)
    root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
    root.right = self.buildTree(preorder[1 + idx:], inorder[1 + idx:])
    return root
