# Описание: Кеша много путешествует и записывает в блокнотик, в каких странах и городах он побывал.
# И вот настал этот момент, когда блокнотик кончился. Кеша понимает, что мы живем в век современных
# технологий и можно автоматизировать этот процесс. Поэтому придумал программу, которая бы добавляла
# страну в посещенные вместе с городом, а если он был в этой стране, то добавлял бы город к списку
# посещенных городов. А еще по кнопочке бы она могла выводить страну, в которой Кеша посетил больше
# всего городов. Но сам он к сожалению не может сделать такую программу, давайте поможем ему с этим!
#
# Задание: Написать программу, которая будет по введенной стране и городу добавлять эти данные в
# словарь следующим образом: если такая страна уже есть, то добавлять в список городов новый город
# (если конечно же его еще нет). Если такой страны нет, то добавлять новый элемент в словарь.
# А если Кеша введет команду favorite, то программа выведет название страны, у которой количество
# посещенных городов больше всего.

book = {}
book['England'] = ['London']
book['France'] = ['Paris']
book['Germany'] = ['Munich', 'Frankfurt', 'Dresden']

# print('keys: ',book.keys())
# print('values: ', book.values())

def open(book):
    for word in book.keys():
        print('Страна: ', word)
        print('Города: ', book.get(word))
        print()

is_continue = 1

while is_continue != 0:
    print('Введите страну и город через пробел (или команду): ')
    command = input(str())
    command_list = command.split()
    country = command_list[0]
    city = command_list[len(command_list) - 1]

    if command == 'favorite':
        max_visits = 1
        for word in book.keys():
            if len(book.get(word)) > max_visits:
                max_visits = len(book.get(word))
                max_country = word
        print('Наиболее часто посещаемая страна: ', max_country)
        print('Количество посещенных в ней городов:', max_visits)
        print()
    elif command == 'open':
        open(book)
    elif command == 'exit':
        is_continue = 0
    elif book.get(country) == None:
        book[country] = [city]
    else:
        city_list = book.get(country)
        city_list.append(city)
        book[country]=city_list

print('Итоговый список стран и городов:')
open(book)