# Создайте список из случайных чисел. Найдите максимальное
# количество его одинаковых элементов

from random import randint
ton = list(range(30))
trek = list(range(30))
m = 0
n = 0
for i in range(len(ton)):
    ton[i] = randint(1, 30)
print(ton)
for i in range(len(ton)):
    m = ton[i]
    for j in range(len(ton)):
        if ton[j] == m:
            n += 1
    trek[i] = n
    n = 0
print(trek)
trek.sort()
print(trek)
print(trek[len(trek)-1])



