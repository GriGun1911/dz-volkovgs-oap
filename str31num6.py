for biki in range(10):
    for korovi in range(20):
        telyata = 100 - (biki + korovi)
        czena = ((20 * biki) + (10 * korovi) + (1 * telyata))
        if telyata >= 0 and czena == 200:
                print(f"Быков: {biki} Коров: {korovi:.2f} Телят: {telyata:.3f}")
        else:
             continue