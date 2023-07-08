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

