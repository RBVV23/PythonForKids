# Описание: На планете W один ленивый программист решил написать себе бота-помощника,
# который будет выполнять за него некоторые не очень сложные действия. Этот бот запускается и
# работает, пока программист его не остановит командой 'q'. Он умеет делать следующее:
# Формировать запрос в google по введенной фразе по команде google. Например, если пользователь введет
# 'как стать программистом', то бот выведет на экран строку:
# https://www.google.ru/search?q=как%20стать%20программистом.
# Умеет считать и запоминать результат (правда только складывать и вычитать). Если пользователь введет
# add 5, то бот прибавляет 5 к текущему результату (изначально результат равен 0), если же пользователь введет
# sub 10, то бот вычтет 10 из текущего результата
# Умеет выводить текущий результат на экран по команде res
# А также умеет выводить справку по командам, которые умеет выполнять по команде help

# Задание: Создаем бота, который умеет исполнять команды, описанные выше.

command_list = [
                'google',
                'add X',
                'sub X',
                'res',
                'help',
                'q'
                ]

help_list = [
            'создает запрос для поисковика',
            'увеличивает число на заданную величину X',
            'уменьшает число на заданную величину X',
            'выводит промежуточный результат',
            'выводит справку по командам',
            'завершает работу бота'
            ]


def google():
    print('Введи, пожалуйста свой поисковый запрос:')
    string = input(str())
    words = string.split(' ')
    result = 'https://www.google.ru/search?q='
    for i in range(len(words)):
        result = result + words[i] + '%20'
    print('Ваш поисковый запрос: ' + result)


def add(inpt, number):
    result = number + inpt
    print(f'add {inpt} =  {result}')
    return result


def sub(entering, number):
    result = number - entering
    print(f'sub {entering} = {result}')
    return result


def res(inpt):
    result = inpt
    print(f'Промежуочный результат: {result}')


def help():
    print('Бот умеет выполнять следующие команды:')
    for i in range(len(command_list)):
        print(f'"{command_list[i]}" - {help_list[i]}')
    print()
    print('*команды вводятся без кавычек')
    print()
    print()


help()
google('как стать программистом')

print('Привет! Я бот, который умеет выполнять различные команды!')
flag = 1
number = 0
while flag != 0:
    print('Введи, пожалуйста команду:')
    command = input(str())
    if command == 'help':
        help()
    elif command == 'google':
        google()
    elif command[0:3] == 'add':
        if len(command) > 4:
            ham = command[4:len(command)]
            arg = int(ham)
        else:
            print(f'Вы не ввели аргумент для функции {command[0:3]}, введите число:')
            arg = int(input())
        number = add(arg, number)
    elif command[0:3] == 'sub':
        if len(command) > 4:
            ham = command[4:len(command)]
            arg = int(ham)
        else:
            print(f'Вы не ввели аргумент для функции {command[0:3]}, введите число:')
            arg = int(input())
        number = sub(arg, number)
    elif command == 'res':
        res(number)
    elif command == 'q':
        flag = 0
    else:
        print(f'Прости, но я не знаю такой команды "{command}"')
print('Заверешние работы бота')
