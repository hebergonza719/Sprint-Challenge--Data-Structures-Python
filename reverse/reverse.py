class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        # self.length = 0

    def add_to_head(self, value):
        # self.lenght = self.length + 1
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if self.head is None:
            return

        cur_node = node
        pre_node = prev

        while cur_node is not None:
            next_node = cur_node.next_node
            cur_node.next_node = pre_node
            pre_node = cur_node
            cur_node = next_node

        self.head = pre_node
