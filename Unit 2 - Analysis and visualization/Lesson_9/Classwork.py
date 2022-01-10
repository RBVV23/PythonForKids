import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 20)

data = pd.read_csv('FIFA18_Ultimate_Team_players_2.csv')
useful_cols = ['player_ID', 'player_name', 'player_extended_name', 'quality',
               'revision', 'origin', 'overall', 'club', 'league', 'position',
               'age', 'height', 'weight', 'intl_rep', 'pace', 'pace_acceleration',
               'pace_sprint_speed',  'cf', 'cb', 'cdm']

df = data[useful_cols]

print(df.info())
df['league'] = pd.factorize(df['league'])[0]
new_df = df[['cf'] + ['cb'] + ['cdm'] + ['overall'] + ['league']]
# print(new_df.groupby('league').mean())
# new_df.groupby('league').mean().plot()
new_df.groupby('league').mean().plot(kind='bar')
new_df.groupby('league').mean().plot(kind='area')
new_df.groupby('league').mean().plot(kind='area', stacked=False)
plt.show()

df = df.head(1000)
df.plot(kind='scatter', x='pace', y='pace_acceleration')
plt.show()

df['pace'].plot(kind='hist')
plt.show()

cols = ['pace', 'pace_acceleration', 'pace_sprint_speed']
sns_plot = sns.pairplot(df[cols])
sns_plot.savefig('pairplot_1.png')
#
cols = ['age', 'height', 'weight']
sns_plot = sns.pairplot(df[cols])
sns_plot.savefig('pairplot_2.png')

sns.distplot(df['overall'])
plt.show()

g = sns.jointplot(x='pace_acceleration', y='pace_sprint_speed', data=df)
g.savefig('jointplot_2.png')

league_position_overalls = df.pivot_table(index='league', columns='position', values='overall',
                                          aggfunc='sum').fillna(0).applymap(float)
sns.heatmap(league_position_overalls, annot=True, fmt='.1f', linewidth=0.5)
plt.show()