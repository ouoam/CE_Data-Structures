class Stack:
    maxSize = 4

    def __init__(self):
        self.item = []

    def push(self, i):
        if not self.isFull():
            self.item.append(i)
            return True
        else:
            return False
    
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

    def isFull(self):
        return self.size() >= self.maxSize

    def left(self):
        return self.maxSize - self.size()

main = Stack()
temp = Stack()

def depart(carNo):
    if main.isEmpty():
        print("car", carNo, "cannot depart: soi empty")
        return False
    elif not carNo in main.item:
        print("car", carNo, "cannot depart: No car", carNo)
        return False
    else:
        op = []
        print("car", carNo, "depart :")
        while main.peek() != carNo:
            op.append("pop " + str(main.peek()))
            temp.push(main.pop())
        op.append("pop " + str(main.peek()))
        main.pop()
        while not temp.isEmpty():
            op.append("push " + str(temp.peek()))
            main.push(temp.pop())
        print("\t" + ", ".join(op))
        print("\tspace left", main.left())
        return True

def arrive(carNo):
    if not main.isFull():
        main.push(carNo)
        print("car", carNo, "arrive\t\tspace left", main.left())
        return True
    else:
        print("car", carNo, "cannot arrive : SOI FULL")
        return False

def printSoi():
    print("print soi =", main.item)

depart(6)
arrive(1)
arrive(2)
arrive(3)
arrive(4)
arrive(5)
printSoi()
depart(7)
depart(2)
printSoi()
depart(1)
depart(4)
printSoi()
depart(9)
depart(2)
depart(3)
printSoi()
arrive(5)
arrive(6)