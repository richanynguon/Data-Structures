class Heap:
    def __init__(self, comparator=lambda x, y: x > y):
        self.storage = []
        self.comparator = comparator
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        self.size += 1
        value_idx = (self.size-1)
        self._bubble_up(value_idx)

    def delete(self):
        bucket = self.storage[0]
        if self.size == 0:
            raise IndexError("No")
        self._sift_down(0)
        if self.size > 0:
            self.storage[0] = self.storage[-1]
            del self.storage[-1]
            self.size -= 1
            self._sift_down(0)
        return bucket

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        parent_idx = (index-1) // 2
        while self.comparator(self.storage[index], self.storage[parent_idx]):
            self.storage[parent_idx], self.storage[index] = self.storage[index], self.storage[parent_idx]
            index = parent_idx
            parent_idx = (index-1) // 2
            if index == 0:
                break

    def _sift_down(self, index):
        right_child_val = None
        if index < self.size:
            current_priority = self.storage[index]
            left_child_idx = (2 * index) + 1
            right_child_idx = (2 * index) + 2
        else:
            return

        if left_child_idx < self.size:
            left_child_val = self.storage[left_child_idx]
        else:
            return
        if right_child_idx < self.size:
            right_child_val = self.storage[right_child_idx]
        
        #lambda x, y: x > y

        if right_child_val and self.comparator(right_child_val, left_child_val):
            priority_child = right_child_idx
        else:
            priority_child = left_child_idx

        if self.comparator( self.storage[priority_child], current_priority):
            self.storage[priority_child], self.storage[index] = self.storage[index], self.storage[priority_child]
            
        if priority_child <= self.size:
            self._sift_down(priority_child)

        return
