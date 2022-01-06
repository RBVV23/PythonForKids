# 1. Показать, что средний возраст взрослых пассажиров (мужчин и женщин) в первом классе выше, чем во 2 и 3
# 2. Посмотреть, влияет ли класс пассажира (pclass) на его смертность
# 3. Посмотреть, влияет ли пол пассажира (sex) на его смертность
# 4. Посмотреть на зависимость среднего возраста и средних транспортных расходов и смерти


import pandas as pd
import numpy as np

data = pd.read_csv('titanic.csv')

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 15)
print(data.head())

# 1. Показать, что средний возраст взрослых пассажиров (мужчин и женщин) в первом классе выше, чем во 2 и 3
print( data.pivot_table(['age'], ['sex', 'class'], aggfunc = 'mean'))

# 2. Посмотреть, влияет ли класс пассажира (pclass) на его смертность
print( pd.crosstab(data['class'], data['alive'], normalize=True, margins=True ))

