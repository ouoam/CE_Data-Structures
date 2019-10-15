class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        out = 'output : '
        out += self.data
        return out

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next


class List:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        item = ''
        count = 0
        p = self.head
        while p != None:
            item += ' ' + p.data
            count = count + 1
            p = p.next
        out = 'output :  size ' + str(count) + ' :' + item
        return out

    def size(self):
        count = 0
        p = self.head
        while p != None:
            count = count + 1
            p = p.next
        return count

    def isEmpty(self):
        return self.head == None

    def append(self, data):
        data = data if isinstance(data, node) else node(data)
        data.setNext(None)
        if self.head == None:
            self.head = data
        else:
            p = self.head
            while p.next != None:
                p = p.next
            p.next = data

    def addHead(self, data):
        data = data if isinstance(data, node) else node(data)
        data.setNext(self.head)
        self.head = data

    def isIn(self, data):
        p = self.head
        while p != None:
            if p.data == data:
                return True
            p = p.next
        return False

    def before(self, data):
        last = None
        p = self.head
        while p != None:
            if p.data == data:
                return last
            last = p
            p = p.next
        return False

    def remove(self, data):
        be = self.before(data)
        if be == False:
            return False
        elif be == None:
            re = self.head
            self.head = self.head.next
            return re
        else:
            re = be.next  # pylint: disable=no-member
            be.next = re.next
            return re

    def removeTail(self):
        if self.head == None:
            return False
        elif self.head.next == None:
            return self.removeHead()
        else:
            last = None
            p = self.head
            while p.next != None:
                last = p
                p = p.next
            last.next = None
            return p

    def removeHead(self):
        if self.head == None:
            return False
        else:
            re = self.head
            self.head = self.head.next
            return re
