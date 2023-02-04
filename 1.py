"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
"""

# number = input('Введите вещественное число: ')
# summa = 0
# for i in number:
#     # if i != '.' and i != ',' and i != '-':
#     #     summa += int(i)
#     if i.isdigit(): # if i in "0123456789":
#         summa += int(i)
# print(summa)

print(sum(map(int, list(str(input('Введите число: ')).replace('.','')))))