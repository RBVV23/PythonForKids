print(round(0.5))
# >>> 0
print(round(-0.5))
# >>> 0
print(round(1.5))
# >>> 2
print(round(-1.5))
# >>> -2
print(round(2.5))
# >>> 2
print(round(-2.5))
# >>> -2


# ---------------------------------------------


# put your python code here
from math import ceil

x = int(input())
y = int(input())

print(ceil(y / x))


# ---------------------------------------------


# put your python code here

a = int(input())
b = int(input())
n = int(input())

roubles = (a * n) + (b * n) // 100
pennies = (b * n) % 100

print(roubles)
print(pennies)


# ---------------------------------------------


# put your python code here
S = int(input())
D = 1 + 8 * S
n = (D**0.5 - 1)/2

print(int(n))


# ---------------------------------------------


import time # подключим библиотеку, контролирующую параметры времени

q = 0 # текущее количество забитых мячей
s = 0 # текущая сумма забитых мячей
n = int(input()) # количество забитых мячей

start_time = time.time() # запоминаем время, в которое начинает работу цикл

while q < n: # повторять пока текущее количество забитых мячей q < n
    q += 1 # в Python эта запись равнозначна q = q + 1
    s += q # s = s + q
print(s)

print("--- %s seconds ---" % (time.time() - start_time))
# отнимаем от текущего времени время начала работы цикла