a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(d - (a + b + c))  # допишите программный код...


# ---------------------------------------------


# так как числа вещественные, используем функцию float()
a = float(input())
b = float(input())
c = float(input())

p = (a + b + c) / 2  # продолжите программный код
S = (p * (p - a) * (p - b) * (p - c))**0.5
print(round(S, 3))


# ---------------------------------------------


# put your python code here

a = int(input())
S = 3 * a**2 + a**2 * 3**0.5 / 4
print(round(S, 3))