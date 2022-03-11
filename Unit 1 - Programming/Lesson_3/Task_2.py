# Описание: Миша любит собирать друзей на разные мероприятия, например, на квесты.
# Он может добавить кого-то в список командой: add имя. А также удалить
# кого-то, написав: remove имя. Если участник с таким именем уже есть, то добавлять
# второй раз Миша его не будет. А если Миша захочет удалить участника, которого нет,
# то компьютер должен на него поругаться и сказать, что так делать нельзя. А по команде
# team программа должна выводить текущий список участников на экран.
# Поможем ему автоматизировать процесс?
#
# Задание: Написать программу, которая будет помогать Мише составлять списки для участников квеста

team_list = []


def add(name, team_list):
    try:
        index = team_list.index(name)
        print(name, ' уже есть в списке под номером ', index)
    except ValueError:
        team_list.append(name)
        print(name, ' успешно добавлен(-а) в список')
    return team_list


def remove(name, team_list):
    try:
        team_list.remove(name)
        print(name, ' успешно удален(-а) из списка')
    except ValueError:
        print(name, ' и так не был(-а) в списках')
    return team_list


print('Привет, я бот, который поможет тебе составить список гостей на мероприятие!')

exit = 0
while exit != 1:
    print('Введи команду и имя: ')
    command = input(str())
    my_command = command.split(' ')
    func = my_command[0]

    if func == 'add':
        arg = my_command[1]
        team_list = add(arg, team_list)
    elif func == 'remove':
        arg = my_command[1]
        team_list = remove(arg, team_list)
    elif func == 'team':
        print('Текущий список гостей: ')
        print(team_list)
    elif func == 'exit':
        exit = 1
    else:
        print('Прости, но я не знаю такой команды')


print('Окончательный список:')
print(team_list)

