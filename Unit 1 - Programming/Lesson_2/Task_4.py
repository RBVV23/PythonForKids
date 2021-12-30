# Нужно сгенерировать два рандомных числа от 10 до 100, вывести их на
# экран. Возвести первое в степень второго (операция **). Вычислить
# остаток от деления большего числа на меньшее, посчитать
# квадратный корень из меньшего числа.

import math as M
from random import randint

print("Генерируем 2 случайных число от 10 до 100...")
A=randint(10,100)
B=randint(10,100)
flag=1
while A==B or flag==1:
    flag=0
    A = randint(10, 100)
    B = randint(10, 100)
    if A<B:
        A = A + B
        B = A - 2 * B
        A = (A - B) // 2
        B = A + B

print('A =',A)
print('B =',B)
print('A > B')

print('A^B = ',A**B)
print('Остаток от деления A на B = ',A%B)
print('Корень из B = ',M.sqrt(B))

