class Heap:
    def __init__(self, comparator=None):
        self.storage = []
        # chose a method over lambda function for its performance gains
        self.comparator = comparator or self._default_compare

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        self._swap_values_at_index(0, len(self.storage) - 1)
        value = self.storage.pop()

        self._sift_down(0)

        return value

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while index > 0:

            parent = (index - 1) // 2

            parent_val = self.storage[parent]
            index_val = self.storage[index]

            if self.comparator(index_val, parent_val):
                self._swap_values_at_index(index, parent)
                index = parent
            else:
                break

    def _sift_down(self, index):
        heap_size = len(self.storage)

        while index < len(self.storage):
            left = index * 2 + 1
            right = index * 2 + 2

            index_val = self.storage[index]

            # If we have a left and right child
            if left < heap_size and right < heap_size:
                # getting values because its easier to write and read
                left_val = self.storage[left]
                right_val = self.storage[right]

                # if left is priority child and has priority over parent
                if self.comparator(left_val, right_val) and self.comparator(left_val, index_val):
                    # perform swap and update index
                    self._swap_values_at_index(left, index)
                    index = left
                # else if right is priority child and has priority over parent
                elif not self.comparator(left_val, right_val) and self.comparator(right_val, index_val):
                    # perform swap and update index
                    self._swap_values_at_index(right, index)
                    index = right
                else:
                    break
            # if we only have a left child
            elif left < heap_size:
                left_val = self.storage[left]

                # does left child have priority over parent
                if self.comparator(left_val, index_val):
                    self._swap_values_at_index(left, index)
                    index = left
                else:
                    break
            else:
                break

    def _swap_values_at_index(self, i1, i2):
        """ Swaps values held at index 1 (i1) and index 2 (i2) """
        self.storage[i1], self.storage[i2] = self.storage[i2], self.storage[i1]

    def _default_compare(self, x, y):
        return x > y
