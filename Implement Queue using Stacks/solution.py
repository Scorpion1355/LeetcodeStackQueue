class Stack:
    """ Making class for the stack object"""
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack. Raises error if empty."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

class MyQueue(object):
    """ Main class for the Myqueue object """

    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.push(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.pop()


    def peek(self):
        """
        :rtype: int
        """
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.peek()


    def empty(self):
        """
        :rtype: bool
        """
        return self.stack_in.is_empty() and self.stack_out.is_empty()
