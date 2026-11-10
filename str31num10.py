for x in range(29):
    f = 2 * x ** 2 + 29
    for i in range(1, f + 1):
        D = f % i
        if D != 0:
            break
    print(f"Простое число: {f}")