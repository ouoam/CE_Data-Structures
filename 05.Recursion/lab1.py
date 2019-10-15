def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)


def sum1ToN(n):
    if n == 1:
        return 1
    return n + sum1ToN(n - 1)


def printNto1(n):
    if n == 0:
        print()
        return
    print(n, end=' ')
    printNto1(n - 1)


def print1toN(n):
    if n == 0:
        return
    print1toN(n - 1)
    print(n, end=' ')


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def binarySearch(lo, hi, x, l):
    mid = (hi - lo) // 2 + lo
    if l[mid] == x:
        return mid
    elif lo == hi:
        return None
    elif l[mid] > x:
        return binarySearch(lo, mid - 1, x, l)
    else:
        return binarySearch(mid + 1, hi, x, l)


def move(n, fr, to):
    help = chr(ord('A') + ord('B') + ord('C') - ord(fr) - ord(to))
    if n > 1:
        move(n - 1, fr, help)
    print("move disk", n, "from", fr, "to", to)
    if n > 1:
        move(n - 1, help, to)


def sum1(n, l):
    if n == 0:
        return 0
    return sum1(n - 1, l) + l[n - 1]


def sum2(i, l):
    if i >= len(l):
        return 0
    return l[i] + sum2(i + 1, l)


def sum3(l):
    if len(l) == 0:
        return 0
    return l[0] + sum3(l[1:])


def printlistForw(l, i=0):
    if i == len(l):
        return
    print("index", i, ":", l[i])
    printlistForw(l, i + 1)


def printlistBkw(l, i=0):
    if i == len(l):
        return
    printlistBkw(l, i + 1)
    print("index", i, ":", l[i])


def app(n=1, l=[]):
    if n == 0:
        return
    app(n - 1, l)
    l.append(n)
    return l


def appB(n=1, l=[]):
    if n == 0:
        return
    l.append(n)
    appB(n - 1, l)
    return l


class node():
    def __init__(self, d, nxt=None):
        self.data = d
        if nxt is None:
            self.next = None
        else:
            self.next = nxt


def printList(h):
    if h == None:
        return
    print(" ->", h.data, end="")
    printList(h.next)


def createLLL(n, l, ll=None):
    if n != 0:
        ll = node(l[n - 1], ll)
        ll = createLLL(n - 1, l, ll)
    return ll


def createLL(n, ll=None):
    if n != 0:
        ll = node(n, ll)
        ll = createLL(n - 1, ll)
    return ll


print('fac(9) :', fac(9))

print('sum1ToN(9) :', sum1ToN(9))

print('printNto1(9) :', end=' ')
printNto1(9)

print('print1toN(9) :', end=' ')
print1toN(9)
print()

print('fib(9) :', fib(9))

l = list(range(10))
print('binarySearch(0, 9, 9, l) :', binarySearch(0, 9, 9, l))
print('binarySearch(0, 9, 5, l) :', binarySearch(0, 9, 5, l))
print('binarySearch(0, 5, 9, l) :', binarySearch(0, 5, 9, l))
print('binarySearch(0, 9, 20, l) :', binarySearch(0, 9, 20, l))

move(4, 'A', 'C')

print('sum1(5, [1, 2, 3, 4, 5]) :', sum1(5, [1, 2, 3, 4, 5]))
print('sum1(4, [1, 2, 3, 4, 5]) :', sum1(4, [1, 2, 3, 4, 5]))

print('sum2(0, [1, 2, 3, 4, 5]) :', sum2(0, [1, 2, 3, 4, 5]))
print('sum2(1, [1, 2, 3, 4, 5]) :', sum2(1, [1, 2, 3, 4, 5]))

print('sum3([1, 2, 3, 4, 5]) :', sum3([1, 2, 3, 4, 5]))
print('sum3([1, 2, 4, 5]) :', sum3([1, 2, 4, 5]))

printlistForw([1, 2, 3, 4, 5])
printlistBkw([1, 2, 3, 4, 5])

print(app(5))
print(appB(5))

head = node('A', node('B', node('C', node('D', node('E')))))
print("head", end="")
printList(head)
print()

lll = createLLL(5, ['A', 'B', 'C', 'D', 'E'])
print("lll", end="")
printList(lll)
print()

ll = createLL(5)
print("ll", end="")
printList(ll)
print()
