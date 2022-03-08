# Давайте создадим список чисел от 0 до 100, а затем сформируем
# новый список из элементов первого списка, которые делятся на 3 и больше 15


my_list = [i for i in range(0, 101)]

new_list = [i for i in my_list if (i % 3 == 0) and (i > 15)]

print('Исходный список')
print('my_list = ')
print(my_list)
print()
print('Фильтрованный список')
print('new_list = ')
print(new_list)
