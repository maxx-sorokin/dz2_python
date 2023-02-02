"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа
вида 2^k), не превосходящие числа N.
Пример:
10 -> 1 2 4 8
"""

n = int(input('Введите число N: '))
for i in range(n):
    degree = 2**i
    if degree < n:
        print(degree, end=' ')
    else:
        break        
