class ListStack():

    def __init__(self, capacity):
        self.liststack = [None] * capacity * 3 
        self.capacity = capacity
        self.sizes = [0, 0, 0]

    def push(self, stack, item):
        position = (self.capacity * stack) + self.sizes[stack]
        if self.sizes[stack] >= self.capacity:
            return 'stack at capacity'
        else:
            self.liststack[position] = item
            self.sizes[stack] += 1

    def pop(self, stack):
        value = self.sizes[stack]
        index = stack * self.capacity + (value - 1)
        self.liststack[index] = None
        self.sizes[stack] -= 1

        
            


