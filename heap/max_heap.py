class Heap:
    def __init__(self):
        self.storage = []
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        self.size += 1
        value_idx = self.get_size()
        self._bubble_up(value_idx-1)

    def delete(self):
        pass

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        parent_idx = (index // 2)-1
        print(parent_idx, index, self.storage)
        if parent_idx <= 0:
            parent_idx = 0

        while parent_idx >= 0:
            if self.storage[parent_idx] < self.storage[index]:
                self.storage[parent_idx], self.storage[index] = self.storage[index], self.storage[parent_idx]
                self._bubble_up(index)
            else:
                break

    def _sift_down(self, index):
        pass
