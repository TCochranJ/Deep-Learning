import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import csv

filename = open('2017.csv', 'r')

file = csv.DictReader(filename)

Economy = []
HappScore = []
Freedom = []

data = pd.read_csv('2017.csv')
data = data.drop(data.columns[0], axis=1)

for col in file:
    Economy.append(col['Economy..GDP.per.Capita.'])
    HappScore.append(col['Happiness.Score'])
    Freedom.append(col['Freedom'])

Economy = list(map(float, Economy))
HappScore = list(map(float,HappScore))
Freedom = list(map(float, Freedom))

plt.scatter(Economy, HappScore, color = 'b', label = 'GDP per Capita')
plt.title("Tyler Cochran - GDP per Capita vs. Happiness Score")
plt.xlabel("GDP per Capita")
plt.ylabel("Happiness Score")
plt.legend()
plt.show()

plt.scatter(Freedom, HappScore, color = 'g', label = 'Freedom')
plt.title("Tyler Cochran - Freedom vs. Happiness Score")
plt.xlabel("Freedom")
plt.ylabel("Happiness Score")
plt.legend()
plt.show()

x_labels = ['Happiness Rank', 'Happiness Score', 'W_High', 'W_Low', 'Economy', 'Family',
            'Health', 'Freedom', 'Generosity', 'Trust', 'Dystopia Residual']
y_labels = ['Happiness Rank', 'Happiness Score', 'W_High', 'W_Low', 'Economy', 'Family',
            'Health', 'Freedom', 'Generosity', 'Trust', 'Dystopia Residual']
sns.set(font_scale=0.5)
sns.heatmap(data.corr(), annot = True, fmt = '.1f', xticklabels = x_labels, yticklabels = y_labels,
            linewidth = .5, linecolor = 'w')
plt.xticks(rotation = 30)
plt.show()