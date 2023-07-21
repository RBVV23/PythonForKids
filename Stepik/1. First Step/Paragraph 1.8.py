a = ["a", "b", "c"]
print(a[0])
# >>> 'a'
print(a[1])
# >>> 'b'
print(a[-1])  # выбор первого справа элемента, как бы краткая запись a[ len(a) - 1 ]
# >>> 'c'
print(len(a))  # функция, которая выводит количество элементов списка
# >>> 3


d = [1, 2, 3, 4]
print(d[0] + d[1] + d[2] + d[3])
# >>> 10
print(sum(d))
# >>> 10

print("one two three".split())
# >>> ['one', 'two', 'three']
s = "one two three"
print(s.split())
# >>> ['one', 'two', 'three']


a, b, c = "1 2 3".split()
print(a)
# >>> '1'
print(int(a))
# >>> 1
print(b)
# >>> '2'
print(int(b))
# >>> 2
print(c)
# >>> '3'
print(int(c))
# >>> 3


# Дана строка (три числа, разделенные пробелом)
# 1 2 3
a, b, c = input('Введите: "1 2 3"\n').split()
a = int(a)
b = int(b)
c = int(c)
print(a + b + c)


s = "abc"  # итерируемый объект
print(s[0])  # взятие первого элемента итерируемого объекта
# >>> 'a'
d = ['a', 'b', 'c']  # итерируемый объект
print(d[0])  # взятие первого элемента итерируемого объекта
# >>> 'a'
d = [1, 2, 3]  # итерируемый объект
print(d[0])  # взятие первого элемента итерируемого объекта
# >>> 1


s = "3 5 7"
print(s)
# >>> '3 5 7'
print(s.split())
# >>> ['3', '5', '7']
x = map(int, s.split())  # каждый элемент таблицы s преобразуется к целому int типу
print(x)
# >>> <map object at 0x03F64570>  # переменная x связана с ссылкой на объект map
a, b, c = x  # связывание трёх переменных с тремя элементами объекта map
print(a)
# >>> 3
print(b)
# >>> 5
print(c)
# >>> 7


print(list("element"))
# >>> ['e', 'l', 'e', 'm', 'e', 'n', 't']
print(list(range(5)))  # функция range(star, finish, step) - создает числовой ряд (подробности на уроке про циклы)
# >>> [0, 1, 2, 3, 4]
print(list(map(int, "1 2 3 4 5".split())))
# >>> [1, 2, 3, 4, 5]


# Дана строка (три числа, разделенные пробелом)
# 5 7 10
a, b, c = map(int, input('Введите: "5 7 10"\n').split())  # этот пример уже был
n = list(map(int, input('Введите: "5 7 10"\n').split()))  # создается список (таблица)
a, b, c = n = list(map(int, input('Введите: "5 7 10"\n').split()))  # две предыдущие строки в Python можно объединить
print(n)  # [5, 7, 10]
print(n[0])  # 5
print(n[1])  # 7
print(n[2])  # 10
print(a)  # 5
print(b)  # 7
print(c)  # 10


# ---------------------------------------------


a, b = map(int, input().split())
print(a + b)


# ---------------------------------------------


x1, y1, x2, y2 = map(int, input().split())
if (x1 == x2) or (y1 == y2):
    print('YES')
else:
    print('NO')


# ---------------------------------------------


a, b, c = map(int, input().split())
if (a + b > c) and (a + c > b) and (b + c > a):
    print('YES')
else:
    print('NO')


# ---------------------------------------------


A, B = map(int, input().split())
C, D = map(int, input().split())
if (A <= C <= B) or (A <= D <= B):
    print('YES')
else:
    print('NO')


# ---------------------------------------------


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
if (x1 * x2 <= 0) or (y1 * y2 <= 0):
    print('YES')
else:
    print('NO')


# ---------------------------------------------


x1, y1, x2, y2 = map(int, input().split())
if (abs(x1 - x2) + abs(y1 - y2) == 3) and (abs(x1 - x2)*abs(y1 - y2) == 2):
    print('YES')
else:
    print('NO')


# ---------------------------------------------


a, b, c = map(int, input().split())
if (a + b > c) and (a + c > b) and (b + c > a):
    hypotenuse = max(a, b, c)
    leg_1 = min(a, b, c)
    leg_2 = (a + b + c) - hypotenuse - leg_1
    if leg_1**2 + leg_2**2 == hypotenuse**2:
        print('right')
    elif leg_1**2 + leg_2**2 > hypotenuse**2:
        print('acute')
    else:
        print('obtuse')
else:
    print('impossible')