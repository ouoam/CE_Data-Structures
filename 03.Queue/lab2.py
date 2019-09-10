from Queue import Queue

def cipher(string, series, mode = 1):
    q = Queue()
    outs = ""

    for num in series:
        q.enQueue(num)

    for char in string:
        l = 0
        out = ord(char)
        if 'a' <= char <= 'z':
            l = ord('a')
        elif 'A' <= char <= 'Z':
            l = ord('A')
        if l > 0:
            ch = q.deQueue()
            q.enQueue(ch)
            if mode == -1:
                ch = 26 - ch
            out += ch - l
            out %= 26
            out += l
        outs += chr(out)
    return outs

def encode(string, series):
    return cipher(string, series, 1)

def decode(string, series):
    return cipher(string, series, -1)

input = "I love Python"
caesar = [2, 5, 6, 1, 8, 3]

en = encode(input, caesar)
print(en)
print(decode(en, caesar))