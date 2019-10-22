class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setData(self, data):
        self.data = data

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def addI(self, data):
        l = None
        p = self.root

        while p != None:
            l = p
            if p.data > data:
                p = p.left
            else:
                p = p.right

        if l == None:
            self.root = node(data)
        elif l.data > data:
            l.left = node(data)
        else:
            l.right = node(data)

    def inOrder(self):
        self._inOrder(self.root)
        print()

    @staticmethod
    def _inOrder(p):
        if p != None:
            BST._inOrder(p.left)
            print(p, end=" ")
            BST._inOrder(p.right)

    def preOrder(self):
        self._preOrder(self.root)
        print()

    @staticmethod
    def _preOrder(p):
        if p != None:
            print(p, end=" ")
            BST._preOrder(p.left)
            BST._preOrder(p.right)

    def postOrder(self):
        self._postOrder(self.root)
        print()

    @staticmethod
    def _postOrder(p):
        if p != None:
            BST._postOrder(p.left)
            BST._postOrder(p.right)
            print(p, end=" ")

    def add(self, data):
        if data is None:
            return
        if not isinstance(data, node):
            data = node(data)
        self.root = self._add(self.root, data)

    @staticmethod
    def _add(p, data):
        if p == None:
            return data
        elif p.data > data.data:
            p.left = BST._add(p.left, data)
        else:
            p.right = BST._add(p.right, data)
        return p

    def printSideway(self):
        self._printSideway(self.root, 0)
        print()

    @staticmethod
    def _printSideway(root, level):
        if root:
            BST._printSideway(root.right, level+1)
            print('   ' * level, root.data, sep='')
            BST._printSideway(root.left, level+1)

    def search(self, data):
        return self._search(self.root, data)

    @staticmethod
    def _search(p, data):
        if p != None:
            if p.data == data:
                return p
            elif p.data > data:
                return BST._search(p.left, data)
            else:
                return BST._search(p.right, data)
        return None

    def path(self, data):
        pathlist = []
        if self._path(self.root, data, pathlist):
            pathStr = []
            for e in pathlist:
                pathStr.append(str(e))
            pathStr.reverse()
            return " -> ".join(pathStr)
        else:
            return "Not Found"

    @staticmethod
    def _path(p, data, pathlist):
        if p != None:
            if p.data == data:
                pathlist.append(p)
                return True
            go = None
            if p.data > data:
                go = p.left
            else:
                go = p.right
            if BST._path(go, data, pathlist):
                pathlist.append(p)
                return True
        return False

    def delete(self, data):
        pathlist = []
        if self._path(self.root, data, pathlist):
            print(pathlist)
            if len(pathlist) == 1:
                self.root = pathlist[0].right
            elif pathlist[1].left == pathlist[0]:
                pathlist[1].left = pathlist[0].right
            else:
                pathlist[1].right = pathlist[0].right
            self.add(pathlist[0].left)
        else:
            return None


# enter = input("insert integers : ")
enter = "14 4 9 7 15 3 18 16 20 5 16"
l = [int(e) for e in enter.split()]
print(l)

t = BST()
for ele in l:
    t.addI(ele)

# t.inOrder()
# t.preOrder()
# t.postOrder()
t.printSideway()

# print("search 20", t.search(20))
# print("search 50", t.search(50))

# print("path 20", t.path(20))
# print("path 50", t.path(50))

print("delete 20", t.delete(20))
t.printSideway()
print("delete 15", t.delete(15))
t.printSideway()
print("delete 14", t.delete(14))
t.printSideway()
print("delete 18", t.delete(18))
t.printSideway()
