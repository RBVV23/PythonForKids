import random

import pandas as pd
import numpy as np

data = pd.read_csv('iris.csv')

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 15)

data['random_column'] = np.random.randint(1, 4, data.shape[0])
print(data.head())
# print( pd.crosstab(data['species'], data['random_column']) )
# print( pd.crosstab(data['species'], data['random_column'], normalize = True) )
print( pd.crosstab(data['species'], data['random_column'], normalize = True, margins = True) )

# print( data.pivot_table(['sepal_length', 'sepal_width'], ['species'], aggfunc='mean') )
# print( data.pivot_table(['sepal_length', 'sepal_width'], ['petal_width'], aggfunc='max') )

data['random_column'] = np.random.randint(1, 3, data.shape[0])
print( data.pivot_table(['sepal_length', 'sepal_width'], ['species', 'random_column'], aggfunc='min') )
data=data.drop(['random_column'], axis=1)
# print(data)


col_1 = np.random.choice([0, 1], size=data.shape[0]//3, p=[7./8, 1./8])
col_2 = np.random.choice([0, 1], size=data.shape[0]//3, p=[1./2, 1./2])
col_3 = np.random.choice([0, 1], size=data.shape[0]//3, p=[1./4, 3./4])

print(col_1)
print(col_2)
print(col_3)
# print(concatenate((col_1, col_2, col_3), axis=0)

data['is_died'] = np.concatenate((col_1, col_2, col_3), axis=0)

print(pd.crosstab(data['species'], data['is_died'], margins=True))
print( data.pivot_table(['petal_length', 'petal_width', 'sepal_length', 'sepal_width'], ['is_died'], aggfunc='mean') )
# print( data.pivot_table(['petal_length', 'petal_width', 'sepal_length', 'sepal_width'], ['species'], aggfunc='mean') )
# print( data.pivot_table(['petal_length', 'petal_width', 'sepal_length', 'sepal_width'], ['species', 'is_died'], aggfunc='mean') )