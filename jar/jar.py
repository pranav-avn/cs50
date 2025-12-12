class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Wrong Capacity")
        else:
            self._capacity = capacity
            self._size = 0

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        if n > self.capacity or (n+self.size) > self.capacity:
            raise ValueError("Too many cookies")
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies")
        self._size -= n #nom nom nom hehe

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
