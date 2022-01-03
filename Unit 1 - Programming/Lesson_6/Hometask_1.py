#1. Указать сколько есть признаков и информация о скольких пассажирах представлена в датасете
#2. Указать в каких столбцах пропущены данные и сколько
#3. Вывести статистику по числовым факторам, а также по категориальным
#4. Показать на примере столбца alive, что сумма абсолютных частот равна количеству строк в таблице
#5. Показать на примере столбца class, что сумма относительных частот равна 1
#6. Факторизовать все категориальные признаки
#7. Отсортировать данные по возрастанию классу кают (pclass)
#8. Отсортировать данные по возрастанию класса кают (pclass) и при этом по убыванию возраста пассажиров (age)P

import pandas as pd

data = pd.read_csv('titanic.csv')

pd.set_option('display.width', 150)

pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 20)
# print(data)
print(data.head())


#1 Указать сколько есть признаков и информация о скольких пассажирах представлена в датасете
print('Файл содержит информацию о '+ str(data.shape[0]) + ' пассажирах по ' + str(data.shape[1]) + ' признакам.')

#2. Указать в каких столбцах пропущены данные и сколько
columns=data.columns

del_sum=0
del_info={}
for word in columns:
    inf = data[word].value_counts()
    print('Признак "' + word + '" принимает '  + str(len(inf)) +  ' значения(-й): ')
    print(data[word].value_counts() )
    num_del=data.shape[0] - sum(inf)
    if num_del != 0:
        del_info[word]=num_del
    del_sum+=num_del
    print( 'Содержит информацию о ' + str(sum(inf)) + ' пассажирах' + ' из ' + str(data.shape[0]) + '.' )
    print( 'Пропущенных значений: ' + str(num_del) + ' из ' + str(data.shape[0]) + '.' )
    print()

print('Всего не хватает ' + str(del_sum) + ' значений из ' + str(data.shape[0]*data.shape[1]) + ' (' + str(round(100*del_sum/(data.shape[0]*data.shape[1]), 1)) + ' %)')
print('Отсутствующие значения по признакам: ')
print(del_info)