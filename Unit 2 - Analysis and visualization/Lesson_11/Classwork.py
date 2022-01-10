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
# print(corr_matrix)

sns.heatmap(corr_matrix)
plt.show()

hist_columns = ['total night minutes', 'customer service calls',
               'total day calls', 'total intl calls', 'total night calls', 'total intl minutes',
               'account length', 'total eve calls', 'total eve minutes', 'number vmail messages',
               'total day minutes']

for column_name in hist_columns:
    df[column_name].plot(kind='hist', title=column_name)
    plt.show()

for column_name in hist_columns:
    sns.distplot(df[column_name], label=column_name)
    plt.show()

hist_columns = ['total night minutes', 'customer service calls',
               'total day calls', 'total intl calls', 'total night calls', 'total intl minutes',
               'account length', 'total eve calls', 'total eve minutes', 'number vmail messages',
               'total day minutes', 'number vmail messages']

for column in hist_columns:
   sns.boxplot(y='churn', x=column, data=df, orient='h')
   plt.show()

print(df['customer service calls'].value_counts())

sns.countplot(x='customer service calls', hue='churn', data=df)
plt.show()

sns.boxplot(y='churn', x='total day minutes', data=df, orient='h')
plt.show()

print(df['state'].value_counts())
print(df['phone number'].value_counts())
print(df['international plan'].value_counts())
print(df['voice mail plan'].value_counts())

sns.countplot(x='international plan', hue='churn', data=df, orient='h')
plt.show()
sns.countplot(x='voice mail plan', hue='churn', data=df, orient='h')
plt.show()

print(df.groupby(['state'])['churn'].agg(np.mean))
print(df.groupby(['state'])['churn'].agg(np.mean).sort_values(ascending=False))
