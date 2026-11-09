import math
h = float(input("Введите шаг y в метрах: "))
y1 = 2
y2 = 3
x = float(input("Введите х в метрах: "))
while y1 <= y2 + 1e-9:
    if y1 > x:
        print("при заданном х треугольник не сущевствует")
    else:
        A = math.acos(y1 / x)
        a = math.degrees(A)
        print(f"угол а при х = {x} и y = {y1:.2f} равен: {a:.3f}")
    y1 = y1 + h