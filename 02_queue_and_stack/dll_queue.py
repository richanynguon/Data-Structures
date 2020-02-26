
from doubly_linked_list import DoublyLinkedList

# https://stackoverflow.com/questions/393556/when-to-use-a-linked-list-over-an-array-array-list
# 
# queue is FIFO

'''
 [h]>[]>[]>[]>[]->none
'''

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size+=1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size < 1:
            return
        self.size-=1
        dequeued_value = self.storage.remove_from_head()
        return dequeued_value

    def len(self):
        return self.size
