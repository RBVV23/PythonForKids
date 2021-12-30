# Описание: наверное все знают про фильм Сплит. Так вот все программисты
# тоже знают такое слово, правда оно означает немного другое.
# Его применяют, когда хотят разделить строку на составляющие по какому-то
# набору символов-разделителей. И вот робот-механик с планеты Q регулярно такую использует,
# только вот незадача, сломалась их встроенная такая вещь. Мы ведь поможем ему?

# Задание: Написать функцию сплит, которая бы по заданной строке и разделителям
# возвращалась бы массив строк - полученным путем разделения исходной строки.


print('Введите строку для разделения: ')
#string='mum-dud sa'
string=input()
print('Введенная строка: ',string)

print('Введите разделители сплошным текстом: ')
#separators_user=[' ',',','-']
separators_user=input()

separators=[]
for i in range(len(separators_user)):
    separators.append(separators_user[i])

print('Введенные разделители: ',separators)

def split(string, separators):
    word=""
    result=[]
    for symbol in string:
        if symbol in separators and word != "":
            result.append(word)
            word=""
        else:
            word+=symbol
    if word != "":
        result.append(word)
    return result


print("Результат разделения: ", split(string, separators))


