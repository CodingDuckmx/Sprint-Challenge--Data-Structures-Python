class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.last = 0 

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        
        else:
            self.storage[self.last] = item

        self.last = (self.last + 1) % self.capacity

        


    def get(self):
        
        return self.storage


if __name__ == "__main__":
    
    rb = RingBuffer(5)

    print(rb.capacity)

    rb.append('a')
    rb.append('a')
    rb.append('b')
    rb.append('c')
    rb.append('d')
    rb.append('e')
    rb.append('f')
    rb.append('g')
    rb.append('h')
    rb.append('i')


    print(rb.get())