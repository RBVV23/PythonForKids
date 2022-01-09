import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 250)
pd.set_option('display.width', 1000)


df = pd.read_csv('clients.csv')

df = df.drop(['total day charge', 'total night charge', 'total eve charge', 'total intl charge'], axis=1)
corr_matrix = df.drop(['state', 'international plan', 'voice mail plan', 'area code'], axis=1).corr()
## print(corr_matrix)
sns.heatmap(corr_matrix)
plt.show()

hist_columns = ['total night minutes', 'customer service calls',
               'total day calls', 'total intl calls', 'total night calls', 'total intl minutes',
               'account length', 'total eve calls', 'total eve minutes', 'number vmail messages',
               'total day minutes']

for column_name in hist_columns:
    df[column_name].plot(kind='hist', title=column_name)
    plt.show()
