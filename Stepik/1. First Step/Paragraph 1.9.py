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
