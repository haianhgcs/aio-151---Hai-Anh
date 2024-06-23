class MyQueue:
    """
    Queue class.
    """

    def __init__(self, capacity):
        """
        Init queue specified capacity.
        """
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        """
        Check whether the queue is empty or not.
        """
        return len(self.queue) == 0

    def is_full(self):
        """
        Check whether the queue is full or not.
        """
        return len(self.queue) == self.capacity

    def dequeue(self):
        """
        Remove and return the item at head.
        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)

    def enqueue(self, value):
        """
        Add value to queue.
        """
        if self.is_full():
            raise OverflowError("Enqueue to a full queue")
        self.queue.append(value)

    def front(self):
        """
        Return value at head but not remove it from queue.
        """
        if self.is_empty():
            raise IndexError("Front from an empty queue")
        return self.queue[0]
