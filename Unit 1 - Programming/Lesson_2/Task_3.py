# Описание: наверное все знают про фильм Сплит. Так вот все программисты
# тоже знают такое слово, правда оно означает немного другое.
# Его применяют, когда хотят разделить строку на составляющие по какому-то
# набору символов-разделителей. И вот робот-механик с планеты Q регулярно такую использует,
# только вот незадача, сломалась их встроенная такая вещь. Мы ведь поможем ему?

# Задание: Написать функцию сплит, которая бы по заданной строке и разделителям
# возвращалась бы массив строк - полученным путем разделения исходной строки.


def my_split(string, separators):
    word = ""
    result = []
    for symbol in string:
        if symbol in separators and word != "":
            result.append(word)
            word = ""
        else:
            word += symbol
    if word != "":
        result.append(word)
    return result


print('Введите строку для разделения: ')
my_string = input()
print(f'Введенная строка: {my_string}')

print('Введите разделители сплошным текстом: ')
separators_user = input()

my_separators = []
for i in range(len(separators_user)):
    my_separators.append(separators_user[i])

print(f'Введенные разделители: {my_separators}')
print(f'Результат разделения: {my_split(my_string, my_separators)}')
