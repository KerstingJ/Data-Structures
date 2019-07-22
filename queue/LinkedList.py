class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, value=None):
        self.head = None if value is None else Node(value)
        self.tail = None if value is None else Node(value)
