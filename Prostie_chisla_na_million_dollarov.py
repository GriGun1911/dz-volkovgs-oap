f = int(input())
for i in range(f):
    for j in range(2, i):
        D = i % j
        print
        if D != 0:
            print(f"Простое число: {i}")
            break
        else:
            break