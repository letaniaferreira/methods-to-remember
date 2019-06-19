class Node():

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def has_left_node(self):
        if not self.left:
            return False
        else:
            return True

    def has_right_node(self):
        if self.right:
            return True
        else:
            return False

    def get_left_node(self):
        return self.left

    def get_right_node(self):
        return self.right

    def set_left_node(self, value):
        self.left = value

    def set_right_node(self, value):
        self.right = value


    def __repr__(self):
        return self.value

a = Node('A')
b = Node('B')
a.left = b

class Stack():
    def __init__(self):
        self.items = []

    def push(self, value):
        node = Node(value)
        self.items.append(node)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        if len(self.items) == 0:
            return True

    def __repr__(self):
        return self.items.__repr__()


class Tree():

    def __init__(self, value=None):
        self.root = Node(value)


    def get_root(self):
        return self.root


def navigate_tree():
    tree = Tree()
    stack = Stack()
    visited = []

    node = tree.get_root()
    stack.append(node)
    if node.has_left_node():
        stack.append(node.get_left_node())
    if node.has_right_node():
        stack.append(node.has_right_node())
    visited.append(node)
    stack.pop()



