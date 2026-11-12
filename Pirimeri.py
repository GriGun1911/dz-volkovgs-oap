n = int(input())
k = int(input())
Sh = int(input())
for i in range(n, k+1, Sh):
    for j in range(n, k+1, Sh):
        print(f"{i} + {j} = {i + j}", end="\t")
    print()