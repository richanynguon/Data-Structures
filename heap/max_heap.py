from generic_heap import Heap as GenericHeap


class Heap(GenericHeap):
    def __init__(self):
        super().__init__(lambda x, y: x > y)

    def get_max(self):
        return super().get_priority()
