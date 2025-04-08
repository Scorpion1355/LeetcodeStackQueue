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

class FreqStack(object):

    def __init__(self):
        self.stack = Stack()
        self.frequency_dict = {}

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.push(val)
        if val in self.frequency_dict:
            self.frequency_dict[val] += 1
        else:
            self.frequency_dict[val] = 1

    def pop(self):
        """
        :rtype: int
        """
        max_freq = max(self.frequency_dict.values())

        for i in range(self.stack.size() - 1, -1, -1):
            val = self.stack.items[i]
            if self.frequency_dict[val] == max_freq:
                self.stack.items.pop(i)
                if self.frequency_dict[val] == 1:
                    del self.frequency_dict[val]
                else:
                    self.frequency_dict[val] -= 1
                return val