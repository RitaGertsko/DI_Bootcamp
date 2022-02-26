# Daily Challenge: Binary Search Tree
class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_value(self):
        return self.value

    def set_right(self, right):
        self.right = right

    def set_left(self, left):
        self.left = left

    def set_value(self, value):
        self.value = value

    def __str__(self):
        return f"my value is {self.value}"


class BST:
    def __init__(self, root: Node):
        self.root = root

    def add_node(self, node):
        current_node = self.root
        while True:
            if current_node.get_value() >= node.get_value():
                # checks if current node has left child
                if current_node.get_left() is None:
                    current_node.set_left(node)
                    break
                # else current node has a left child - advance pointer
                current_node = current_node.get_left()
                continue
            else:
                # checks if current node has right child
                if current_node.get_right() is None:
                    current_node.set_right(node)
                    break
                # else current node has a right child - advance pointer
                current_node = current_node.get_right()

    def search(self, value):
        current_node = self.root
        while current_node is not None:
            if current_node.value == value:
                return current_node
            elif current_node.value > value:
                current_node = current_node.get_left()
                continue
            else:
                current_node = current_node.get_right()
        return None


test_tree = BST(Node(8))
test_tree.add_node(Node(4))
test_tree.add_node(Node(11))
test_tree.add_node(Node(5))
print(test_tree.search(9))
print(test_tree.search(11))