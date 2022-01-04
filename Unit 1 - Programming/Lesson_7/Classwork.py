import pandas as pd
import numpy as np


data = pd.read_csv('iris.csv')


print(data['species'].head())
print(data['sepal_length'].head())

print(data['sepal_length'].mean())
print(data['sepal_width'].mean())

print(data[data['sepal_width'] >= 3])
print( data[ (data['sepal_width'] >=3) & (data['sepal_length'] < 5) ] )

print(data['sepal_width'].max())
print(data['sepal_width'].min())

