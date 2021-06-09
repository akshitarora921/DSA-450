class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key


def printPreorder(root):
    if root:
        printPreorder(root.left)
        print(root.val)
        printPreorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

printPreorder(root)
