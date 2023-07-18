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

