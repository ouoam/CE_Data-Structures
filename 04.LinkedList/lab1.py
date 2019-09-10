from List import List
from List import node

n4 = node('D')
n3 = node('C', n4)
n2 = node('B', n3)
n1 = node('A', n2)

p = n1
while p != None:
    print(p.data, end=' ')
    p = p.next
print('')

q = node('A')
print(q)
r = node('B', q)
print(r)
print(r.next)

print('------------------')

l = List()

l.addHead('1')

print('size :', l.size())
print('isEmpty :', l.isEmpty())
print('item', l)

print('removeTail :', l.removeTail())

l.addHead('0')

print('size :', l.size())
print('isEmpty :', l.isEmpty())
print('item', l)


l.append('A')
l.append('B')
l.append('C')
l.append('D')

print('size :', l.size())
print('isEmpty :', l.isEmpty())
print('item', l)

l.addHead('Z')
l.addHead('Y')
l.addHead('X')

print('size :', l.size())
print('isEmpty :', l.isEmpty())
print('item', l)

print('isIn \'X\' :', l.isIn('X'))
print('isIn \'0\' :', l.isIn('0'))
print('isIn \'D\' :', l.isIn('D'))
print('isIn \'J\' :', l.isIn('J'))

print('before \'X\' :', l.before('X'))
print('before \'0\' :', l.before('0'))
print('before \'D\' :', l.before('D'))
print('before \'J\' :', l.before('J'))

print('remove \'X\' :', l.remove('X'))
print('remove \'0\' :', l.remove('0'))
print('remove \'D\' :', l.remove('D'))
print('remove \'J\' :', l.remove('J'))

print('size :', l.size())
print('isEmpty :', l.isEmpty())
print('item', l)

print('removeTail :', l.removeTail())
print('removeHead :', l.removeHead())

print('size :', l.size())
print('isEmpty :', l.isEmpty())
print('item', l)
