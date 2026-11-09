nog = 64
for kroliki in range(nog // 4 + 1):
    ostnoggus = nog - (kroliki * 4)
    if ostnoggus % 2 == 0:
        gusi = ostnoggus // 2
        print(f"Кроликов: {kroliki} гусей: {gusi:.2f}")