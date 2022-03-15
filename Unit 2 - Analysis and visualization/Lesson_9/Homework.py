
# 1. Сгруппировать данные по классу кают (pclass) и построить обычный график для среднего
#       возраста (age) в каждом классе и средним расходам (fare)
# 2. Построить столбчатую диаграмму по данным из предыдущего пункта
# 3. Построить столбчатую диаграмму по данным из предыдущего пункта, добавив в группировку
#       не только класс каюты, но и пол человека
# 4. А теперь построить Area plot для данных из пункта 1
# 5. А теперь построить Area plot для данных из пункта 1, используя stacked=False.
#       В чем отличие от предыдущей?
# 6. Проверить, есть ли какая-то зависимость (например линейная) между age и fare
# 7. Посмотреть,на распределение у возраста (age) - похоже на нормальное или нет
# 8. Посмотреть,на распределение у транспортных расходов (fare) - похоже на нормальное или нет
# 9. Построить тепловую диаграмму суммарных транспортных средств (fare) для пассажиров
#       разного пола (sex) и разных классов (pclass)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 15)

data = pd.read_csv('titanic.csv')

# 1. Сгруппировать данные по классу кают (pclass)
# и построить обычный график для среднего возраста (age) в каждом классе и средним расходам (fare)
dataset = data[['pclass'] + ['age'] + ['fare']]
dataset.groupby('pclass').agg('mean').plot()
plt.show()


# 2. Построить столбчатую диаграмму по данным из предыдущего пункта
dataset.groupby('pclass').agg('mean').plot(kind='bar')
plt.show()

# 3. Построить столбчатую диаграмму по данным из предыдущего пункта,
# добавив в группировку не только класс каюты, но и пол человека
dataset = data[['pclass'] + ['age'] + ['fare'] + ['sex']]
dataset.groupby(['pclass', 'sex']).agg('mean').plot(kind='bar')
plt.show()

# 4. А теперь построить Area plot для данных из пункта 1
dataset = data[['age'] + ['fare'] + ['pclass']]
dataset.groupby(['pclass']).agg('mean').plot(kind='area')
plt.show()

# 5. А теперь построить Area plot для данных из пункта 1, используя stacked=False. В чем отличие от предыдущей?
dataset.groupby(['pclass']).agg('mean').plot(stacked=False, kind='area')
plt.show()

# 6. Проверить, есть ли какая-то зависимость (например линейная) между age и fare
dataset.plot(kind='scatter', x='age', y='fare')
plt.show()

# 7. Посмотреть,на распределение у возраста (age) - похоже на нормальное или нет
# dataset['age'] = dataset['age'].fillna(0)
sns.distplot(dataset['age'])
plt.show()

# 8. Посмотреть,на распределение у транспортных расходов (fare) - похоже на нормальное или нет
dataset['fare'] = dataset['fare'].fillna(0)
sns.distplot(dataset['fare'])
plt.show()


# 9. Построить тепловую диаграмму суммарных транспортных средств (fare)
# для пассажиров разного пола (sex) и разных классов (pclass)
dataset = data[['pclass'] + ['age'] + ['fare'] + ['sex']]

my_heat_map = dataset.pivot_table(index='sex', columns='pclass', values='fare', aggfunc=sum).fillna(0).applymap(float)
sns.heatmap(my_heat_map, annot=True, fmt='.1f', linewidth=0.5)
plt.show()
