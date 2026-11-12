n = int(input())
x = 0
y = 0
z = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        for j in range(2, i + 1, 2):
            y = y + j
        x = x + i ** y
        y = 0
    else:
        for l in range(1, i + 1, 2):
            z = z + l
        x = x + i ** z
        z = 0
print(x)