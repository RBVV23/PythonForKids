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
