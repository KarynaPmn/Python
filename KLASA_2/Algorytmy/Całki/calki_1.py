import numpy as np # py -m pip install numpy --> 

from matplotlib import pyplot  # py -m pip install Matplotlib --> 

def f(x):
    return np.sqrt(x) + 2

x = np.linspace(0, 160)

pyplot.plot(x, f(x), color="blue")
pyplot.show()

def calka(a, b, n):
    h = (b - a) / n
    suma = 0
    for i in range(n):
        suma += f(a + i * h + h / 2) * h
    return suma

print(calka(0, 16,1000))
