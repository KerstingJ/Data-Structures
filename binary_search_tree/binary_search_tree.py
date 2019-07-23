class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # TODO: Refactor to iterative method
    def insert(self, value):
        # insert right if larger or equal
        if value >= self.value:

            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

        # insert left if smaller
        elif value < self.value:

            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    # TODO: Refactor to iterative method
    def contains(self, target):
        if self.value == target:
            return True

        right_contains = False
        if self.right:
            right_contains = self.right.contains(target)

        left_contains = False
        if self.left:
            left_contains = self.left.contains(target)

        return right_contains or left_contains

    # TODO: Refactor to iterative method
    def get_max(self):
        self_max = self.value

        if self.right:
            right_max = self.right.get_max()
            self_max = self_max if self_max > right_max else right_max

        if self.left:
            left_max = self.left.get_max()
            self_max = self_max if self_max > left_max else left_max

        return self_max

    # TODO: Refactor to iterative method
    def for_each(self, cb):
        cb(self.value)

        if self.right:
            self.right.for_each(cb)

        if self.left:
            self.left.for_each(cb)
