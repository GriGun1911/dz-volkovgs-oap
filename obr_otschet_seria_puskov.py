Kol_vo_puskov = int(input())

for i in range(1, Kol_vo_puskov + 1):
    for j in range(i - 1, -1, -1):
        print(f"Осталось секунд: {j}")
    print(f'Пуск: {i}')