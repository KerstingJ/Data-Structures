class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class QueueList:
    """ pseudo linked list to act as inner structure of a queue """

    def __init__(self, value=None):
        self.head = None if value is None else Node(value)
        self.tail = None if value is None else Node(value)
        self.length = 0 if value is None else 1

    def remove_head(self):
        if self.head is None:
            return None
        elif self.head is self.tail:
            node = self.head
            self.head = None
            self.tail = None
        else:
            node = self.head
            self.head = self.head.next

        self.length -= 1
        return node.value

    def append(self, value):

        new_node = Node(value)

        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
