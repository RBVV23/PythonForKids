import pandas as pd
import numpy as np


data = pd.read_csv('iris.csv')


print(data['species'].head())
print(data['sepal_length'].head())

print(data['sepal_length'].mean())
print(data['sepal_width'].mean())

print(data[data['sepal_width'] >= 3])
print(data[(data['sepal_width'] >= 3) & (data['sepal_length'] < 5)])

print(data['sepal_width'].max())
print(data['sepal_width'].min())


# Вывести средние значения у всех числовых факторов только у тех растений,
# у которых species = versicolor (то есть после факторизации 1)

num_factors = data.describe()
data['species'] = pd.factorize(data['species'])[0]

data_set = data[data['species'] == 1]
# print(data_set)

for line in num_factors:
    print(f'Среднее значение "{line}" среди растений со "species" равным единице: ')
    print(f'\t{data_set[line].mean()}')


# Какая средняя длина чашелистника (sepal_length) у растений вида setosa (после факторизации 0)

data_set = data[data['species'] == 0]
print(f'\nСреднее значение "sepal_length" у растений со "species" равным нулю:')
print(f'\t{data_set["sepal_length"].mean()}\n')


# Какая средняя длина чашелистника (sepal_length) у растений вида virginica (после факторизации 2),
# у которых ширина чашелистника (sepal_width) меньше, чем 3.8.

data_set = data[(data['species'] == 2) & (data['sepal_width'] < 3.8)]
print('\n' + 'Среднее значение "sepal_length" у растений со "species" равным 2 и "sepal_width" меньшим 3.8:')
print('\t' + str(data_set['sepal_length'].mean()) + '\n')


# Вычислить максимальную и минимальную длину чашелистника (sepal_length)
# у растений вида setosa (после факторизации 0), у которых длина чашелистника (sepal_width)
# находится в пределах между 3 и 4 (то есть больше или равна 3 и при этом меньше или равна 4)

data_set = data[(data['species'] == 0) & (data['sepal_width'] < 4) & (data['sepal_width'] > 3)]
print('\n' + 'Максимальное значение "sepal_length" у растений со "species" равным 0 и "sepal_width" между 3 и 4:')
print('\t' + str(data_set['sepal_length'].max()) + '\n')
print('\n' + 'Минимальное значение "sepal_length" у растений со "species" равным 0 и "sepal_width" между 3 и 4:')
print('\t' + str(data_set['sepal_length'].min()) + '\n')

print(data.apply(np.max))
print(data.apply(np.min))

print(data.apply(np.sum, axis=1))

print('Update')
