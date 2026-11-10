Stp = int(input("Введите сумму ежемесячной стипендии: "))
Rsh = int(input("Введите сумму расходов за месяц: "))
Rshsumm = 0
Stpsumm = Stp * 10
for i in range(10):
    Rshsumm = Rshsumm + Rsh
    Rsh = Rsh + Rsh * 0.3
Poprs = (Rshsumm - Stpsumm)
print(f"Студенту нужно попросить {Poprs}рублей")