class Stack:
    def __init__(self):
        self.item = []

    def push(self, i):
        self.item.append(i)
    
    def size(self):
        return len(self.item)
        
    def isEmpty(self):
        return self.size() == 0
    
    def pop(self):
        out = self.peek()
        if out != None:
            self.item.pop()
        return out

    def peek(self):
        if self.isEmpty():
            return None
        else:
            out = self.item[-1]
            return out

name = "Phumphathai"
s = Stack()
print(s.item)
for char in name:
    s.push(char)
print(s.item)
print(s.size())

while not s.isEmpty():
    print(s.peek(), s.pop())

print(s.peek(), s.pop())