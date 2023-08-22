class Node:
    def __init__(self, key, color, parent=None, left=None, right=None):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, 'black')
        self.root = self.NIL

    def left_rotate(self, node):
        y = node.right
        node.right = y.left
        if y.left != self.NIL:
            y.left.parent = node
        y.parent = node.parent
        if node.parent == None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def right_rotate(self, node):
        y = node.left
        node.left = y.right
        if y.right != self.NIL:
            y.right.parent = node
        y.parent = node.parent
        if node.parent == None:
            self.root = y
        elif node == node.parent.right:
            node.parent.right = y
        else:
            node.parent.left = y
        y.right = node
        node.parent = y

    def insert_fixup(self, node):
        while node.parent.color == 'red':
            if node.parent == node.parent.parent.right:
                y = node.parent.parent.left
                if y.color == 'red':
                    node.parent.color = 'black'
                    y.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.left_rotate(node.parent.parent)
            else:
                y = node.parent.parent.right
                if y.color == 'red':
                    node.parent.color = 'black'
                    y.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self.right_rotate(node.parent.parent)
        self.root.color = 'black'

    def insert(self, key):
        node = Node(key, 'red', None, self.NIL, self.NIL)
        node_parent = None
        x = self.root
        while x != self.NIL:
            node_parent = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = node_parent
        if node_parent == None:
            self.root = node
        elif node.key < node_parent.key:
            node_parent.left = node
        else:
            node_parent.right = node
        if node.parent == None:
            node.color = 'black'
            return
        if node.parent.parent == None:
            return
        self.insert_fixup(node)
