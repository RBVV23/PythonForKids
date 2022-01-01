# Давайте создадим список чисел от 0 до 100, а затем сформируем
# новый список из элементов первого списка, которые делятся на 3 и больше 15

list = [i for i in range(0,101)]

newlist = [i for i in list if (i % 3==0) and (i>15) ]

print('Исходный список')
print('list = ')
print(list)
print()
print('Фильтрованный список')
print('newlist = ')
print(newlist)