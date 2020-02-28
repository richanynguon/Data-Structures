# find the middle of a single linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)
        
    def find_middle(self):
        middle = self
        end = self
        while end != None:
          end = end.next
          if end:
              end = end.next
              middle = middle.next
          print("Middle is: " + str(middle.value))
# reverse a linked list


class Node2:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node2(value)

    def reverse(self):
        cur = self
        new = cur.next
        cur.next = None  # This is the new tail
        while new is not None:
            prev = cur  # temp variable for shuffle
            cur = new
            new = cur.next
            cur.next = prev
        return cur
