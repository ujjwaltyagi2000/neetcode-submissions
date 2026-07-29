class DynamicArray:
    
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than 0")
        self.capacity = capacity
        self.size = 0
        self.array = [None] * capacity

    def get(self, i):
        if 0 <= i < self.size:
            return self.array[i]
        else:
            raise IndexError("Index out of bounds")

    def set(self, i, n):
        if 0 <= i < self.size:
            self.array[i] = n
        else:
            raise IndexError("Index out of bounds")

    def pushback(self, n):
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self):
        if self.size == 0:
            raise IndexError("Pop from empty array")
        value = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        return value

    def resize(self):
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.capacity