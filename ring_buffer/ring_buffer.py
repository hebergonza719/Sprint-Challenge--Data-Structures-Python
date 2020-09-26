class RingBuffer:
    def __init__(self, capacity=None):
        self.capacity = capacity
        self.size = 0
        self.storage = []

    def append(self, item):
        if self.size < self.capacity:
            self.storage.append(item)
        elif self.size >= self.capacity:
            self.storage.pop(self.size % self.capacity)
            self.storage.insert(self.size % self.capacity, item)
        self.size = self.size + 1


    def get(self):
        if self.size == 0:
            return []
        else:
            return self.storage


print("abc" > "b")