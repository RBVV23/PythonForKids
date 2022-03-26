# 1. Указать сколько есть признаков и информация о скольких пассажирах представлена в датасете
# 2. Указать в каких столбцах пропущены данные и сколько
# 3. Вывести статистику по числовым факторам, а также по категориальным
# 4. Показать на примере столбца alive, что сумма абсолютных частот равна количеству строк в таблице
# 5. Показать на примере столбца class, что сумма относительных частот равна 1
# 6. Факторизовать все категориальные признаки
# 7. Отсортировать данные по возрастанию классу кают (pclass)
# 8. Отсортировать данные по возрастанию класса кают (pclass) и при этом по убыванию возраста пассажиров (age)P

import pandas as pd


pd.set_option('display.width', 150)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 20)

data = pd.read_csv('titanic.csv')
# print(data)
print(data.head())


# 1 Указать сколько есть признаков и информация о скольких пассажирах представлена в датасете
print(f'Файл содержит информацию о {data.shape[0]} пассажирах по {data.shape[1]} признакам.')


# 2. Указать в каких столбцах пропущены данные и сколько
columns = data.columns

del_sum = 0
del_info = {}
for word in columns:
    inf = data[word].value_counts()
    print(f'Признак {word} принимает {len(inf)} значения(-й): ')
    print(data[word].value_counts())
    num_del = data.shape[0] - sum(inf)
    if num_del != 0:
        del_info[word] = num_del
    del_sum += num_del
    print(f'Содержит информацию о {sum(inf)} пассажирах из {data.shape[0]}.')
    print(f'Пропущенных значений: {num_del} из {data.shape[0]}.')
    print()

print(f'Всего не хватает {del_sum} значений из {data.shape[0] * data.shape[1]} ({round(100*del_sum/(data.shape[0]*data.shape[1]), 1)}%)')
print('Отсутствующие значения по признакам: ')
print(del_info)


# 3. Вывести статистику по числовым факторам, а также по категориальным

numbers = data.describe()
print('ЧИСЛОВЫЕ ФАКТОРЫ')
for line in numbers:
    print(f'Статистика по признаку {line}:')
    print(f'\tСреднее значение: {numbers[line][1]}')
    print(f'\tСКО: {numbers[line][2]}')
    print(f'\tМинимальное значение: {numbers[line][3]}')
    print(f'\tМаксимальное значение: {numbers[line][7]}')

print('КАТЕГОРИАЛЬНЫЕ ФАКТОРЫ')
print(data.describe(include=['object', 'bool']))
categories = data.describe(include=['object', 'bool'])

for line in categories:
    print(line)
    print(f'Статистика по признаку {line}:')
    print(f'\tУникальных значений: {categories[line][1]}')
    print(f'\tНаиболее частое значение: {categories[line]}')
    print(f'\tМаксимальная частота встречаемости: {categories[line][3]}\n')


# 4. Показать на примере столбца alive, что сумма абсолютных частот равна количеству строк в таблице
factor = 'alive'
alives = data[factor].value_counts()
alives_sum = sum(alives)
if alives_sum == data.shape[0]:
    print('Сумма абсолютных частот "' + str(factor) + '" (' + str(alives_sum) + ') ' +
          'равна количеству строк в таблице (' + str(data.shape[0]) + ').' + '\n')
else:
    print('Сумма абсолютных частот "' + str(factor) + '" (' + str(alives_sum) + ') ' +
          'НЕ равна количеству строк в таблице (' + str(data.shape[0]) + ').')
    print('Разность составила ' + str(data.shape[0] - alives_sum) + ' единиц.' + '\n')


# 5. Показать на примере столбца class, что сумма относительных частот равна 1
factor = 'class'
classes = data[factor].value_counts(normalize=True)
classes_sum = sum(classes)
if classes_sum == 1:
    # print(f'Сумма относительных частот {str(factor)} "{str(classes_sum}" + '" (' + str(classes_sum) + ') ' +
    #       'отнормирована на единицу.' + '\n)
    print('Сумма относительных частот "' + str(factor) + '" (' + str(classes_sum) + ') ' +
          'отнормирована на единицу.' + '\n')
else:
    print('Сумма относительных частот "' + str(factor) + '" (' + str(classes_sum) + ') ' +
           'НЕ отнормирована на единицу.' + '\n')
    print('Разность составила ' + str(1 - classes_sum) + '.' + '\n')


# 6. Факторизовать все категориальные признаки
data['deck'] = pd.factorize(data['deck'])[0]
categories = data.describe(include=['object', 'bool'])
for line in categories:
    data[line] = pd.factorize(data[line])[0]
print(data.head())


# 7. Отсортировать данные по возрастанию классу кают (pclass)
print(data.sort_values(by='pclass'))


# 8. Отсортировать данные по возрастанию класса кают (pclass) и при этом по убыванию возраста пассажиров (age)
print(data.sort_values(by=['pclass', 'age'], ascending=[True, False]))
