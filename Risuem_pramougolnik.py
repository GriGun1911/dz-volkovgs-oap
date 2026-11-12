a = int(input("Введите высоту прямоугольника: "))
b = int(input("Введите ширину прямоугольника: "))
Symbol = input("Введите символ из которого состоит фигура: ")

print(f'{Symbol}' * b)
for j in range(a - 2):
    print(Symbol, ' ' * abs(b - 2), Symbol, sep='')
print(f'{Symbol}' * b)