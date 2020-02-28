# INITIAL_CAPACITY = 11
#      # initial capacity should be prime to reduce collision
#         self.capacity = INITIAL_CAPACITY


class Node:
    def __init(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return "(%s, %s)" % (self.key, self.value)


class HashTable:
    def ___init__(self, limit):
        self.capacity = limit
        self.size = 0
        # sets amounts of intial buckets with none
        self.buckets = [None] * self.capacity

    # hash function takes char and creates a hash key
    def hash(self, key):
        hash_sum = 0
        for idx, char in enumerate(key):
            hash_sum += (idx + len(key)) ** ord(char)
            # prevents creating table too large
            hash_sum = hash_sum % self.capacity
        return hash_sum

    def insert(self, key, value):
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def find(self, key):
        # when returning a value but be counted as
        # most recently used
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                node = None
            else:
                prev.next = prev.next.next

            return result


        
            
