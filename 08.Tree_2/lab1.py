class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left if left is not None else None
        self.right = right if right is not None else None


def addi(root, data):
    if not root:
        return node(data)
    else:
        if data < root.data:
            root.left = addi(root.left, data)
        else:
            root.right = addi(root.right, data)
        return root


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)


def add(root, data):
    if not root:
        return node(data)
    else:
        if data < root.data:
            root.left = add(root.left, data)
        else:
            root.right = add(root.right, data)
        return root


def printSideWay(root, level):
    if root:
        printSideWay(root.right, level+1)
        print('   ' * level, root.data, sep='')
        printSideWay(root.left, level+1)


def height(r):
    if not r:
        return -1
    else:
        return max(height(r.left), height(r.right)) + 1


def path(p, data, pathlist=None):
    CallRoot = False
    Found = False
    if (pathlist is None):
        CallRoot = True
        pathlist = []
    if p != None:
        if p.data == data:
            pathlist.append(p)
            Found = True
        go = None
        if p.data > data:
            go = p.left
        else:
            go = p.right
        if path(go, data, pathlist):
            pathlist.append(p)
            Found = True
    if Found:
        if CallRoot:
            pathStr = []
            for e in pathlist:
                pathStr.append(str(e.data))
            pathStr.reverse()
            pathStr = " ".join(pathStr)
            print(pathStr)
        return True
    return False


def search(p, data):
    if p != None:
        if p.data == data:
            return p
        elif p.data > data:
            return search(p.left, data)
        else:
            return search(p.right, data)
    return None


def depth(p, data):
    if p != None:
        if p.data == data:
            return 0
        elif p.data > data:
            return depth(p.left, data) + 1
        else:
            return depth(p.right, data) + 1
    return 99999


l = [14, 4, 9, 7, 15, 3, 18, 16, 20, 5, 16]
print("input: ", l)

r = None
for ele in l:
    r = addi(r, ele)

print("inorder: ", end=" ")
inOrder(r)
print()

print('printSideWay: ')
printSideWay(r, 0)

print("height of", r.data, "=", height(r))

d = 20
print("path:", d, "=", end=" ")
path(r, d)

d = 9
t = search(r, d)
print(t.data)

d = 18
print("depth of node data", d, "=", depth(r, d))
