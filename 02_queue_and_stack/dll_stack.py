from doubly_linked_list import DoublyLinkedList
# last in first out
class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size+=1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size <1:
            return
        self.size -=1
        pop_value = self.storage.remove_from_head()
        return pop_value

    def len(self):
        return self.size
