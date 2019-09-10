from Queue import Queue

name = "Phumphathai"
q = Queue()
for char in name:
    q.enQueue(char)
    print(char, q.size())

print(q.item)

while not q.isEmpty():
    print(q.deQueue())