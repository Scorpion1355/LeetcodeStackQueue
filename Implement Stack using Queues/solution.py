class Queue:
    """Simple Queue class using a list and front pointer."""
    def __init__(self):
        self.items = []
        self.front_index = 0

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self.items[self.front_index]
        self.front_index += 1
        return item

    def peek(self):
        """Return the item at the front without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[self.front_index]

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front_index >= len(self.items)

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items) - self.front_index


class MyStack(object):
    """ Main Mystack class """
    def __init__(self):
        self.stack = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.enqueue(x)
        for _ in range(self.stack.size() - 1):
            self.stack.enqueue(self.stack.dequeue())

    def pop(self):
        """
        :rtype: int
        """
        if self.stack.is_empty():
            raise IndexError("Pop from empty stack")
        return self.stack.dequeue()

    def top(self):
        """
        :rtype: int
        """
        if self.stack.is_empty():
            raise IndexError("Peek from empty stack")
        return self.stack.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack.is_empty()
