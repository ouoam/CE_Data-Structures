def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#for i in range(1, 20):
#    print(i, '! = ', factorial(i))

def multiples_of_3_and_5(n):
    sum = 0
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

#for i in range(1, 20):
#    print(i, ' = ', multiples_of_3_and_5(i))

def integer_right_triangles(p):
    out = []
    for a in range(1, p // 2 + 1):
        for b in range(a, p // 2 + 1):
            c = p - a - b
            if c ** 2 == a ** 2 + b ** 2:
                out.append((a, b, c))
    return out

#print(integer_right_triangles(60))
#print(integer_right_triangles(180))
#print(integer_right_triangles(840))


def gen_pattern(chars):
    lens = len(chars)
    out = []
    for i in range(-lens + 1, lens):
        split = list(chars[abs(i):])
        reverse = split[1:]
        reverse.reverse()
        mix = '.'.join(reverse + split)
        out.append(mix.center(lens * 4 - 3, '.'))
    return '\n'.join(out)

print(gen_pattern('WXYZ'))