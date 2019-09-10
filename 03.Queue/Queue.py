class Queue:
    def __init__(self):
        self.item = []

    def enQueue(self, i):
        self.item.append(i)

    def size(self):
        return len(self.item)
    
    def isEmpty(self):
        return self.size() == 0
    
    def deQueue(self):
        return self.item.pop(0)

    def front(self):
        return self.item[0]