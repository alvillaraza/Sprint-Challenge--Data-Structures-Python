class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.counter = 0


    def append(self, item):
        #while empty slots
        if len(self.data) < self.capacity:
            #insert item
            self.data.append(item)
        


        #if full
        elif len(self.data) == self.capacity:
            
            self.data.pop(self.counter)
            self.data.insert(self.counter, item)
            self.counter += 1
            pass


    def get(self):
        return self.data

