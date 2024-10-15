def f(x):
    return x + 3

def prostokaty1(a, b, n):
    dx = (b - a) / n
    s = 0
    for i in range(n):
        s += f(a + dx / 2 + i * dx) * dx
    return s

def prostokaty2(a, b, n):
    dx = (b - a) / n
    s = 0
    for i in range(n):
        s += f(a + i * dx) * dx
    return s

print(prostokaty1(2, 6, 4)) # 28
print(prostokaty2(2, 6, 4)) # 26
