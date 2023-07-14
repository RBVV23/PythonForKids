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


# ---------------------------------------------


# put your python code here
a = int(input())
S = 6 * (a**2 + a**2 * 3**0.5 / 4)
print(round(S, 3))


# ---------------------------------------------


# put your python code here
n = int(input())
answer = 2 * n + 2 + (n - 1)
print(answer)


# ---------------------------------------------


# put your python code here
m = int(input())
n = int(input())

board = 2 * m + 2 * n
hor_rails = (m - 1) * n
ver_rails = (n - 1) * m
result = board + hor_rails + ver_rails
print(result)
