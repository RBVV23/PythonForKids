# Описание: Сан Саныч - владелец кафе-мороженое "Веселый холодок" -
# очень добродушный и любит радовать своих клиентов. Поэтому
# частенько проводит розыгрыш одного из 101 имеющихся видов мороженого
# среди них. Делает он это так: вытягивает из шляпы цифру с номером мороженого
# и если этот номер бонусный (вытянул четное число или 0), то дарит мороженое с
# таким номером своему клиенту. А в конце дня подсчитывает, скольких людей он
# обрадовал сегодня.
#
# Небольшое замечание: Сан Саныч добрый, но его кафе не может дарить
# подарки бесконечно. Помоги ему в этом процессе!

# Задание: Написать программу, которая заполняет массив из 10 элементов
# рандомными целыми числами от 0 до 100. При этом все четные числа она должна
# вывести на экран (номера бонусного мороженого) и после вывести, сколько всего
# четных чисел было сгенерировано (скольких людей осчастливил Сан Саныч).

from random import randint

numbers = []
winners = 0
for i in range(10):
    ham = randint(0, 101)
    if (ham % 2) == 0:
        winners += 1
    numbers.append(ham)
print(f'Из шляпы вытянули номера: {numbers}')
print(f'Количество победитлей: {winners}')
