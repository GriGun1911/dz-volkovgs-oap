import cmath
x = float(input())
y = float(input())
def ctan(x):
    return 1 / cmath.tan(x)
otv = (1 - cmath.tan(x))**ctan(x) + cmath.cos(x - y)
print(otv)