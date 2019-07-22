"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if self.head is None:
            node = ListNode(value, prev=None, next=None)
            self.head = node
            self.tail = node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev

        self.length += 1

    def remove_from_head(self):
        node = self.head

        if self.length <= 1:
            self.head = None
            self.tail = None
        else:
            self.head = node.next
            node.delete()

        self.length = self.length - 1 if self.length > 0 else 0

        return node.value

    def add_to_tail(self, value):
        if self.tail is None:
            node = ListNode(value, prev=None, next=None)
            self.head = node
            self.tail = node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next

        self.length += 1

    def remove_from_tail(self):
        node = self.tail

        if self.length <= 1:
            self.head = None
            self.tail = None
        else:
            self.tail = node.prev
            self.tail.next = None

        self.length = self.length - 1 if self.length > 0 else 0

        return node.value

    def delete(self, node):
        if self.length == 1:
            self.tail = None
            self.head = None
        else:

            if node is self.head:
                self.head = node.next
            elif node is self.tail:
                self.tail = node.prev
                
            node.delete()

        self.length -= 1

    def move_to_front(self, node):

        if node is self.tail:
            self.tail = node.prev

        self.add_to_head(node.value)
        self.delete(node)

    def move_to_end(self, node):

        if node is self.head:
            self.head = node.next

        self.add_to_tail(node.value)
        self.delete(node)

    def get_max(self):
        current = self.head
        biggest = self.head.value
        while current:
            if current.value > biggest:
                biggest = current.value

            current = current.next

        return biggest
