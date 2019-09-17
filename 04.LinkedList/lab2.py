from List import List

l = List()


def bottomUp(percent):
    topItem = percent * l.size() // 100

    for _ in range(topItem):
        l.append(l.removeHead())


def deBottomUp(percent):
    topItem = percent * l.size() // 100

    for _ in range(topItem):
        l.addHead(l.removeTail())


def riffle(percent):
    topItem = percent * l.size() // 100

    p2l = None
    p2 = l.head
    for _ in range(topItem):
        p2l = p2
        p2 = p2.next

    if p2l == None:
        return

    p2l.next = None
    p1 = l.head

    while p1 != None and p2 != None:
        p1n = p1.next
        p2n = p2.next

        p1.next = p2
        if p1n != None:
            p2.next = p1n

        p1 = p1n
        p2 = p2n


def deRiffle(percent):
    topItem = percent * l.size() // 100
    buttomItem = l.size() - topItem
    if topItem == 0 or buttomItem == 0:
        return
    p1 = l.head
    p2 = l.head.next
    topItem = topItem - 1
    buttomItem = buttomItem - 1
    p1n = p1
    p2n = p2

    while topItem > 0 and buttomItem > 0:
        p1n.next = p1n.next.next
        p2n.next = p2n.next.next

        p1n = p1n.next
        p2n = p2n.next

        topItem = topItem - 1
        buttomItem = buttomItem - 1

    if topItem != 0:
        p1n.next = p1n.next.next
        p2n.next = None
        while p1n.next != None:
            p1n = p1n.next
    p1n.next = p2


st = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
for ch in st:
    l.append(ch)

print(l)
bottomUp(30)
print(l)

riffle(60)
print(l)

deRiffle(60)
print(l)

deBottomUp(30)
print(l)
