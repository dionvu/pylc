from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.ptr = root
        self.stack = []
        self.append_left(self.ptr)

    def append_left(self, node):
        if not node:
            return 
        self.stack.append(node)
        self.append_left(node.left)

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.append_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0
