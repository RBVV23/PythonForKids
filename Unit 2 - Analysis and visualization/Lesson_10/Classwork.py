import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 250)
pd.set_option('display.width', 1000)


data = pd.read_csv('FIFA18_Ultimate_Team_players_2.csv')


df = data.head(1000)

sns.boxplot(x='overall', data=df, orient='h')
plt.show()

top_leagues = df['league'].value_counts().sort_values(ascending=False).head(5).index.values
# bottom_leagues = df['league'].value_counts().sort_values(ascending=True).head(5).index.values
# print(bottom_leagues)
sns.boxplot(y='league', x='overall', data=df[df['league'].isin(top_leagues)], orient='h')
# sns.boxplot(y='league', x='overall', data=df[df['league'].isin(bottom_leagues)], orient='h')
plt.show()

df = pd.read_csv('clients.csv')
print(df.shape)
print(df.info())

# print(df['state'].value_counts())
print(df['churn'].value_counts())
df['churn'].value_counts().plot(kind='bar')
plt.show()
# print(df.corr())

corr_matrix = df.drop(['state', 'international plan', 'voice mail plan', 'area code'], axis=1).corr()
# print(corr_matrix)
sns.heatmap(corr_matrix)
plt.show()

df = df.drop(['total day charge', 'total night charge', 'total eve charge', 'total intl charge'], axis=1)

corr_matrix = df.drop(['state', 'international plan', 'voice mail plan', 'area code'], axis=1).corr()
# print(corr_matrix)
sns.heatmap(corr_matrix)
plt.show()

