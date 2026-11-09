n = int(input("Введите время размножения: "))
SumAmeba = 1
Hours = 0
for i in range(1, n + 1):
    SumAmeba = SumAmeba + SumAmeba
    x = i % 3
    if x == 0:
        Hours = Hours + 3
        print(f"Кол-во амёб через {Hours} часов составляет: {SumAmeba:.2f} штук")
    else:
        continue