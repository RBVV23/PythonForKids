# импликация
# классика
a = True
b = False
print(not(a) or b)
# >>> False
# lifehack
a = True
b = False
print(a <= b)
# >>> False


# ---------------------------------------------


a, b, c = map(int, input().split())
if a <= b <= c:
    print("YES")
else:
    print("NO")


# ---------------------------------------------


a = int(input())
b = int(input())
c = int(input())
if a <= b < c:
    print("YES")
else:
    print("NO")


# ---------------------------------------------


a = int(input())
b = int(input())
c = int(input())
if a <= c <= b:
    print("YES")
else:
    print("NO")


# ---------------------------------------------


a = int(input())
b = int(input())
c = int(input())

if a >= (c + b):
    print("NO")
elif b >= (a + c):
    print("NO")
elif c >= (a + b):
    print("NO")
else:
    print("YES")


# ---------------------------------------------


n = int(input())

if (n % 2):
    print(3 * n + 1)
else:
    print(n // 2)


# ---------------------------------------------


n = int(input())
if (n % 3 == 0) & (n % 10 == 5):
    print("YES")
else:
    print("NO")


# ---------------------------------------------


n = int(input())
if 100 <= n <= 999:
    if ((n // 10) % 10) == 7:
        print("YES")
else:
    print("NO")


# ---------------------------------------------


n = int(input())
if 100 <= n <= 999:
    sum = (n % 10) + (n // 100) + ((n // 10) % 10)
    if (sum % 2) == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")


# ---------------------------------------------


a = int(input())
b = int(input())
c = int(input())
if a <= b and a <= c:
    if b < c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b <= a and b <= c:
    if a < c:
        print(b, a, c)
    else:
        print(b, c, a)
elif c <= a and c <= b:
    if a < b:
        print(c, a, b)
    else:
        print(c, b, a)


# ---------------------------------------------


a = int(input())
b = int(input())
c = int(input())

min_num = a     #предположим что минимальное число - область памяти с именем a (неважно какое число записано в ячейке памяти с именем a)
# теперь два имени (min_num и a) ссылаются на одно число

if b < min_num:
    min_num = b # если число, на которое ссылается b, меньше числа, на которое ссылается min_num
# только при условии b <= min_num, два имени (min_num и b) будут ссылаться на одно число

if c < min_num:
    min_num = c # если число, на которое ссылается с, меньше числа, на которое ссылается min_num
# только при условии с <= min_num, два имени (min_num и с) будут ссылаться на одно число

# после исполнения данного кода, min_num будет ссылаться на ячейку памяти, в которой записано наименьшее число, переменные a, b, c сохранили связь с числами на которые изначально ссылались

print(min_num)  # выведем значение наименьшего числа


# ---------------------------------------------


a = int(input())
b = int(input())
c = int(input())
if b < a:
    a, b = b, a
if c < a:
    a, c = c, a
if c < b:
    c, b = b, c
if b < a:
    a, b = b, a
print(a, b, c)


# ---------------------------------------------


a = int(input())
b = int(input())
c = int(input())
mx = max(a, b, c)  # встроенная функция находит максимальное число
mn = min(a, b, c)  # встроенная функция находит минимальное число
av = (a + b + c) - (mx + mn)
print(mn, av, mx)


# ---------------------------------------------


a = int(input())
b = int(input())
c = int(input())

mn = min(a, b, c)
mx = max(a, b, c)
md = a + b + c - mx - mn

print(mn, md, mx, sep='\n')


# ---------------------------------------------


min = int(input())

b = int(input())
if b <= min:
    min = b

c = int(input())
if c <= min:
    min = c

d = int(input())
if d <= min:
    min = d

print(min)