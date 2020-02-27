
import sys
sys.path.append('../02_queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


# o(nlog n)

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    #be consistent in coding style
    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if self.value < target:
            if self.right:
                return self.right.contains(target)
            else:
                return False
        else:
            if self.left:
                return self.left.contains(target)
            else:
                return False

    # Return the maximum value found in the tree

    def get_max(self):
        max_node = self.value
        current = self
        while current:
            if current.value > max_node:
                max_node = current.value
            current = current.right
        return max_node

        # while there is still a self.right keep going until there is not and then return

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)

    # DAY 2 Project -----------------------


# BBQ
# breadth  = queue
# depth = stack
# if its a stack, you can do recursion (which is why dfs can be recusive, bfs can't_

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal


    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self)
        print(self.value)
        if self.right:
            self.right.in_order_print(self)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal # breadth  = queue
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        while queue.len() > 0:
            current = queue.dequeue()
            if current.right is not None:
                queue.enqueue(current.right)
            if current.left is not None:
                queue.enqueue(current.left)
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal # depth = stack
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.len() > 0:
            current = stack.pop()
            if current.right is not None:
                stack.push(current.right)
            if current.left is not None:
                stack.push(current.left)
            print(current.value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # be useful to copy and recreate tree
    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left is not None:
            self.pre_order_dft(node.left)
        if node.right is not None:
            self.pre_order_dft(node.right)

    # - maybe has something to do with deleting node but not sure
    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left is not None:
            self.post_order_dft(node.left)
        if node.right is not None:
            self.post_order_dft(node.right)
        print(node.value)
