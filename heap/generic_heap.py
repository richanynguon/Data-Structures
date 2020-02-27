class Heap:
    def __init__(self, comparator):
        self.storage = []
        self.comparator = comparator
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        self.size += 1
        value_idx = (self.size-1)
        print(self.storage)
        self._bubble_up(value_idx)

    def delete(self):
        pass

    def get_priority(self):
        pass

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        parent_idx = index // 2
        if parent_idx == 0:
            return parent_idx, index
        print(parent_idx, index)
        # while self.storage[parent_idx] < self.storage[index]:
        #     self.storage[parent_idx], self.storage[index] = self.storage[index], self.storage[parent_idx]

    def _sift_down(self, index):
        pass
