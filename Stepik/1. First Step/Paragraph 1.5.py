a = 1
b = 2
c = 3

print(a * 100 + b * 10 + c)
# >>> 123
print(str(a))
# >>> '1'
print(str(a) + str(b) + str(c))
# >>> '123'
print("{}{}{}".format(a, b, c))
# >>> '123'
print(int(str(a) + str(b) + str(c)))
# >>> 123


# ---------------------------------------------


n = int(input())
h = n // 60
print(h)


# ---------------------------------------------


n = int(input())
h = n // 60
m = n - h * 60
print(m)


# ---------------------------------------------


n = int(input())
n = n % (24 * 60)
h = n // 60
print(h)


# ---------------------------------------------


n = int(input())
n = n % (24 * 60)
h = n // 60
m = n - 60 * h
print(h, m)


# ---------------------------------------------


n = int(input())
print(n % 10)


# ---------------------------------------------


n = int(input())
h = n // 100
d = (n - h * 100) // 10
u = n % 10
ans = 100 * h + 10 * u + d
print(ans)


# ---------------------------------------------


n = int(input())
n = n % (24 * 60)
h = n // 60
h1 = h // 10
h2 = h % 10

m = n - 60 * h
m1 = m // 10
m2 = m % 10

print(f'{h1}{h2}:{m1}{m2}')


# ---------------------------------------------


n = float(input()) # функция float()преобразует строку, полученную от input(), к вещественному типу данных
print(n)
print(int(n))


# ---------------------------------------------


print(1 / 2)
# >>> 0.5
print(1 / 3)
# >>> 0.3333333333333333
import math  # подключаем библиотеку math
print(math.pi)      # выводим число pi
# >>> 3.141592653589793
print(format(math.pi, '.2f'))   # используем функцию форматирования для вывода двух цифр после точки
# >>> '3.14'
print(0.3 - 0.1 - 0.1 - 0.1)
# >>> -2.7755575615628914e-17
print(1000e-3)
# >>> 1.0


# ---------------------------------------------


n = float(input())
print(int(n))


# ---------------------------------------------

