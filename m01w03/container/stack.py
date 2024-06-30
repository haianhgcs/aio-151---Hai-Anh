class MyStack:
    """
    MyStack class.
    """

    def __init__(self, capacity):
        """
        Init stack with capacity.
        """
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        """
        Check whether the stack is empty or not.
        """
        return len(self.stack) == 0

    def is_full(self):
        """
        Check whether the stack is full or not..
        """
        return len(self.stack) == self.capacity

    def pop(self):
        """
        Return item in top and remove.
        """
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()

    def push(self, value):
        """
        Add a value into stack.
        """
        if self.is_full():
            raise OverflowError("Push to a full stack")
        self.stack.append(value)

    def top(self):
        """
        Get the item on top but does not remove it from stack.
        """
        if self.is_empty():
            raise IndexError("Top from an empty stack")
        return self.stack[-1]
