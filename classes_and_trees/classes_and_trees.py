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

    def set_left_node(self, value):
        self.left


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


# class Tree():
#
#     def __init__(self):
#         self.root = None
#         self.items = Stack()
#
#     def has_left_node(self):
#         if self.root == None:
#             return False
#         node = self.root
#         return node.left != None



