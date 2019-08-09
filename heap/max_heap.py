import math


class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        print(f"before delete\n{self.storage}")

        # Swap the first and last item in the heap
        self._swap_values_at_index(0, len(self.storage) - 1)

        # pop off the last item of the heap
        value = self.storage.pop()

        self._sift_down(0)

        return value

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while index > 0:

            parent = (index-1) // 2

            if self.storage[index] > self.storage[parent]:
                self._swap_values_at_index(index, parent)

                index = parent

            else:
                break

    def _sift_down(self, index):
        # while index is inside of storage
        while index < len(self.storage):
            left = index * 2 + 1
            right = index * 2 + 2

            # getting values because its easier to write and read
            # this -inf is used to denote that a location doesnt exist in heap
            # if a value is -inf it will never be max so this algo will always ignore that side
            heap_size = len(self.storage)
            left_val = self.storage[left] if left < heap_size else -math.inf
            right_val = self.storage[right] if right < heap_size else -math.inf
            current_val = self.storage[index]

            # if left is our biggest child and it is bigger than its parent
            if left_val >= right_val and left_val > current_val:
                # perform swap and update index
                self._swap_values_at_index(left, index)
                index = left
            # else if right is our largest child and it is bigger than its parent
            elif right_val > left_val and right_val > current_val:
                # perform swap and update index
                self._swap_values_at_index(right, index)
                index = right
            else:
                break

    def _swap_values_at_index(self, i1, i2):
        self.storage[i1], self.storage[i2] = self.storage[i2], self.storage[i1]
