N = int(input())
n = 1
print()

for i in range(1, N + 1):
    for j in range(i):
        if N >= n:
            print(n, end=" ")
            n = n + 1
    if N < n:
        break
    print()
