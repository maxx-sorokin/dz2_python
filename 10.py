"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
Пример:
5 -> 1 0 1 1 0
2
"""

coins = input('Введите через пробел 1 (решка) или 0 (орёл): ')
count1 = 0
count0 = 0
for i in coins:
    if i == '1':
        count1 += 1
    elif i == '0':
        count0 += 1
if count1 > count0:
    print(count0)
else:
    print(count1)
