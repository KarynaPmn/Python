# a = (a + b) / 2
# b = P / a 
# P = 49*

# 
def NP1(x, eps):
    a = x
    b = 1
    while abs(a-b)>eps:
        a = (a+b)/2
        b = x/a
    return a

def NP2(x, n):
    a = x
    b = 1
    for i in range(n):
        a = (a+b)/2
        b = x/a
    return a

print(NP1(50, 0.001))
print(NP2(50, 5))
print(NP2(50, 6))
print(NP2(50, 7))
