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

def run(string):
    Popen = ['(', '{', '[']
    Pclose = [')', '}', ']']
    s = Stack()
    for char in string:
        if char in Popen:
            s.push(char)
        elif char in Pclose:
            if s.isEmpty():
                print("MISMATCH close paren. exceed")
                return
            elif Popen.index(s.peek()) == Pclose.index(char):
                s.pop()
            else:
                print("MISMATCH close paren. mismatch")
                return

    if not s.isEmpty():
        print("MISMATCH open paren. exceed")
    else:
        print("MATCH")

s1 = " ( a+b-c *[d+e]/{f*(g+h) } "
s2 = " [ ( a+b-c }*[d+e]/{f*(g+h) } "
s3 = " ( 3 + 2 ) / { 4**5 } "
s4 = " ( 3 + 2 ) / { 4**5 } } "
run(s1)
run(s2)
run(s3)
run(s4)