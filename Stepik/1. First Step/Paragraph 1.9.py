for i in "abc":
    print(i)

# >>> a
# >>> b
# >>> c

for i in "123":
    print(int(i) ** 2)

# >>> 1
# >>> 4
# >>> 9

for color in 'red', 'yellow', 'green':
    print(color)

# >>> red
# >>> yellow
# >>> green

# Универсальное решение
numbers = [int(i) for i in input().split()]
print(numbers)
# введите числовой ряд, например:
# 2 33 34 25 15 23


# С использованием функции map()
message = "2 33 34 25 15 23"
numbers = list(map(int, message.split()))
print(numbers)


# варианты использования оператора split() с параметром:
message = "2,33,34,25,15,23"  # если в конце строки нет символа перевода строки \n
numbers = message.split(",")
print(numbers)  # ['2', '33', '34', '25', '15', '23']

message = "2,33,34,25,15,23\n"  # если в конце строки есть символ перевода строки \n, используем метод strip()
numbers = message.strip().split(",")
print(numbers)  # ['2', '33', '34', '25', '15', '23']

message = "2,33,34,25,      15,23"
numbers = message.strip().split(",")
print(numbers)  # ['2', '33', '34', '25', '      15', '23']

message = "2,33,     34,25,      15,23"
numbers = [int(i) for i in message.split(",")]
# лишние пробелы не влияют на преобразование
print(numbers)  # [2, 33, 34, 25, 15, 23]

message = "2.33, 34.25, 15"
numbers = [float(i) for i in message.split(",")]
print(numbers)  # [2.33, 34.25, 15.0]


# ---------------------------------------------


d = [12, 17, 45, 28, 75]
# напишите программный код, использующий цикл for

sum = 0
for i in d:
    sum += i

print(sum)


# ---------------------------------------------


d = [12, 17, 45, 28, 75, 55, 18]
# напишите программный код, использующий цикл for

max = d[0]
for i in d:
    if i >= max:
        max = i

print(max)


# ---------------------------------------------


# put your python code here

d = input()

sum = 0
for i in d:
    sum += int(i)

print(sum)


# ---------------------------------------------


n = int(input())

sum = 0
for i in range(n):
    sum += int(input())

print(sum)


# ---------------------------------------------


# put your python code here
n = int(input())
sum = 0
while True:
    r = n % 10
    sum += r
    n //= 10
    if n == 0:
        break
print(sum)


# ---------------------------------------------


n = 1
sum = 0
while n:
    n = int(input())
    if n % 2 == 0:
        sum += n

print(sum)


# ---------------------------------------------


n = int(input())
numbers = [int(i) for i in input().split()]

sum = 0
for i in range(n):
    sum += numbers[i]

print(sum)
