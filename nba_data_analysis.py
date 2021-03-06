# -*- coding: utf-8 -*-
"""NBA Data Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PmkU14quhVKXX0dAfsAb9gK4S4yzmV2t
"""

import requests 
from lxml import html 
import csv
import pandas as pd

#the webpage and and the web contents
r = requests.get('https://www.basketball-reference.com/leagues/NBA_2020_per_game.html')
data = html.fromstring(r.text)

player = data.xpath("//tbody/tr/td[@data-stat='player']/a[@href]/text()")
position = data.xpath("//tbody/tr/td[@class='center ']/text()")
age = data.xpath("//tbody/tr/td[@data-stat='age']/text()")
team = data.xpath("//tbody/tr/td[@data-stat='team_id']/a[@href]/text()|//tbody/tr/td[@data-stat='team_id']/text()")
games = data.xpath("//tbody/tr/td[@data-stat='g']/text()")
games_started = data.xpath("//tbody/tr/td[@data-stat='gs']/text()")
mins_per_g = data.xpath("//tbody/tr/td[@data-stat='mp_per_g']/text()")
fg_per_g = data.xpath("//tbody/tr/td[@data-stat='fg_per_g']/text()")
fga_per_g = data.xpath("//tbody/tr/td[@data-stat='fga_per_g']/text()")
fg_pct = data.xpath("//tbody/tr/td[@data-stat='fg_pct']")
fg_pct = [i.text_content() for i in fg_pct]
fg3_per_g = data.xpath("//tbody/tr/td[@data-stat='fg3_per_g']/text()")
fg3a_per_g = data.xpath("//tbody/tr/td[@data-stat='fg3a_per_g']/text()")
fg3_pct = data.xpath("//tbody/tr/td[@data-stat='fg3_pct']")
fg3_pct = [i.text_content() for i in fg3_pct]
fg2_per_g = data.xpath("//tbody/tr/td[@data-stat='fg2_per_g']/text()")
fg2a_per_g = data.xpath("//tbody/tr/td[@data-stat='fg2a_per_g']/text()")
fg2_pct = data.xpath("//tbody/tr/td[@data-stat='fg2_pct']")
fg2_pct = [i.text_content() for i in fg2_pct]
efg_pct = data.xpath("//tbody/tr/td[@data-stat='efg_pct']")
efg_pct = [i.text_content() for i in efg_pct]
ft_per_g = data.xpath("//tbody/tr/td[@data-stat='ft_per_g']/text()")
fta_per_g = data.xpath("//tbody/tr/td[@data-stat='ft_per_g']/text()")
ft_pct = data.xpath("//tbody/tr/td[@data-stat='ft_pct']")
ft_pct = [i.text_content() for i in ft_pct]
orb_per_g = data.xpath("//tbody/tr/td[@data-stat='orb_per_g']/text()")
drb_per_g = data.xpath("//tbody/tr/td[@data-stat='drb_per_g']/text()")
trb_per_g = data.xpath("//tbody/tr/td[@data-stat='trb_per_g']/text()")
ast_per_g = data.xpath("//tbody/tr/td[@data-stat='ast_per_g']/text()")
stl_per_g = data.xpath("//tbody/tr/td[@data-stat='stl_per_g']/text()")
blk_per_g = data.xpath("//tbody/tr/td[@data-stat='blk_per_g']/text()")
tov_per_g = data.xpath("//tbody/tr/td[@data-stat='tov_per_g']/text()")
pf_per_g = data.xpath("//tbody/tr/td[@data-stat='pf_per_g']/text()")
pts_per_g = data.xpath("//tbody/tr/td[@data-stat='pts_per_g']/text()")

#combines all the columns
nba2019 = zip(player, 
              position, 
              age, 
              team, 
              games, 
              games_started, 
              mins_per_g, 
              fg_per_g, 
              fga_per_g, 
              fg_pct, 
              fg3_per_g, 
              fg3a_per_g, 
              fg3_pct, 
              fg2_per_g, 
              fg2a_per_g, 
              fg2_pct, 
              efg_pct, 
              ft_per_g, 
              fta_per_g, 
              ft_pct, 
              orb_per_g, 
              drb_per_g,
              trb_per_g,
              ast_per_g,
              stl_per_g,
              blk_per_g,
              tov_per_g,
              pf_per_g,
              pts_per_g)
#organizing our data structure to a pandas dataframe
dfnba = pd.DataFrame(nba2019)
dfnba

dfnba = dfnba.rename(columns = {0:'Player', 
                          1:'Position', 
                          2:'Age', 
                          3:'Team', 
                          4:'GP', 
                          5:'GS', 
                          6:'MP', 
                          7:'FG', 
                          8:'FGA', 
                          9:'FG%', 
                          10:'3P', 
                          11:'3PA', 
                          12:'3P%', 
                          13:'2P', 
                          14:'2PA', 
                          15:'2P%', 
                          16:'eFG%', 
                          17:'FT', 
                          18:'FTA', 
                          19:'FT%', 
                          20:'ORB', 
                          21:'DRB',
                          22:'TRB',
                          23:'AST',
                          24:'STL',
                          25:'BLK',
                          26:'TOV',
                          27:'PF',
                          28:'PTS'})

dfnba.head()

dfnba.info()

#changing data types to have numeric values
dfnba['Age'] = pd.to_numeric(dfnba['Age'])
dfnba['Age'].fillna(0, inplace=True)

dfnba['GP'] = pd.to_numeric(dfnba['GP'])
dfnba['GP'].fillna(0, inplace=True)

dfnba['GS'] = pd.to_numeric(dfnba['GS'])
dfnba['GS'].fillna(0, inplace=True)

dfnba['MP'] = pd.to_numeric(dfnba['MP'])
dfnba['MP'].fillna(0, inplace=True)

dfnba['FG'] = pd.to_numeric(dfnba['FG'])
dfnba['FG'].fillna(0, inplace=True)

dfnba['FGA'] = pd.to_numeric(dfnba['FGA'])
dfnba['FGA'].fillna(0, inplace=True)

dfnba['FG%'] = pd.to_numeric(dfnba['FG%'])
dfnba['FG%'].fillna(0, inplace=True)

dfnba['3P'] = pd.to_numeric(dfnba['3P'])
dfnba['3P'].fillna(0, inplace=True)

dfnba['3PA'] = pd.to_numeric(dfnba['3PA'])
dfnba['3PA'].fillna(0, inplace=True)

dfnba['3P%'] = pd.to_numeric(dfnba['3P%'])
dfnba['3P%'].fillna(0, inplace=True)

dfnba['2P'] = pd.to_numeric(dfnba['2P'])
dfnba['2P'].fillna(0, inplace=True)

dfnba['2PA'] = pd.to_numeric(dfnba['2PA'])
dfnba['2PA'].fillna(0, inplace=True)

dfnba['2P%'] = pd.to_numeric(dfnba['2P%'])
dfnba['2P%'].fillna(0, inplace=True)

dfnba['eFG%'] = pd.to_numeric(dfnba['eFG%'])
dfnba['eFG%'].fillna(0, inplace=True)

dfnba['FT'] = pd.to_numeric(dfnba['FT'])
dfnba['FT'].fillna(0, inplace=True)

dfnba['FTA'] = pd.to_numeric(dfnba['FTA'])
dfnba['FTA'].fillna(0, inplace=True)

dfnba['FT%'] = pd.to_numeric(dfnba['FT%'])
dfnba['FT%'].fillna(0, inplace=True)

dfnba['ORB'] = pd.to_numeric(dfnba['ORB'])
dfnba['ORB'].fillna(0, inplace=True)

dfnba['DRB'] = pd.to_numeric(dfnba['DRB'])
dfnba['DRB'].fillna(0, inplace=True)

dfnba['TRB'] = pd.to_numeric(dfnba['TRB'])
dfnba['TRB'].fillna(0, inplace=True)

dfnba['AST'] = pd.to_numeric(dfnba['AST'])
dfnba['AST'].fillna(0, inplace=True)

dfnba['STL'] = pd.to_numeric(dfnba['STL'])
dfnba['STL'].fillna(0, inplace=True)

dfnba['BLK'] = pd.to_numeric(dfnba['BLK'])
dfnba['BLK'].fillna(0, inplace=True)

dfnba['TOV'] = pd.to_numeric(dfnba['TOV'])
dfnba['TOV'].fillna(0, inplace=True)

dfnba['PF'] = pd.to_numeric(dfnba['PF'])
dfnba['PF'].fillna(0, inplace=True)

dfnba['PTS'] = pd.to_numeric(dfnba['PTS'])
dfnba['PTS'].fillna(0, inplace=True)


dfnba.info()

pd.DataFrame.to_csv(dfnba, 'nbastats.csv')

from bs4 import BeautifulSoup

url = "http://www.espn.com/nba/salaries"
r = requests.get(url)

#here we are using beautiful soup to scrape the data
soup = BeautifulSoup(r.content, "lxml")

# use a for loop to ensure the webpages generate properly
a = "http://www.espn.com/nba/salaries/_/year/2020/page/"
for i in range(1,15):
    print(a,i)

salary_table = []
a = "http://www.espn.com/nba/salaries/_/year/2020/page/"

for i in range(1,13):
    url = (a,i)
  
    soup = BeautifulSoup(r.content, "lxml")
    
    g_data = soup.find_all("tr", {"class": "oddrow"})
    for item in g_data:
        table1 = item.text
        salary_table.append(table1)    
    g_data1 = soup.find_all("tr", {"class": "evenrow"})
    for item in g_data1:
        table2 = item.text
        salary_table.append(table2)

#here we will change our data structure to a pandas dataframe
salary = pd.DataFrame(salary_table)
salary.head()

#salary.to_csv("salary.csv", encoding="utf-8")

from IPython.display import Image
from IPython.core.display import HTML

df = pd.read_csv("/salaryupdated.csv", header=None)
df = pd.DataFrame(df)
df.head()

#salary = df
df.columns = ['0','Player', 'Salary']
df.head()
df = df.drop('0', 1)
df.head()

pd.DataFrame.to_csv(df, 'finishedsalary.csv')

stats = pd.read_csv('nbastats.csv')
stats.head()

stats = stats.drop_duplicates(subset=['Player'], keep=False)
stats

"""Work on merging the tables salary and stats

# Analyzing the Data
"""

stats['Team'].describe()

"""Out of the 30 teams that are in the NBA, the Brooklyn Nets had the most players on their roster during the 2019-2020 season. With this data, I can conclude that the team was well over the limit of ~15 players, and that they were most likely over the cap space limit for player salary. """

stats.groupby('Team').size()

"""Here we are able to see the number of rostered players on each team, and from there we can also see that many teams are over the 15 player limit, with 13 players at most having to be active each game. """

stats['Position'].describe()

"""I wanted to see what the most played position in the league would be, and this year, it's the Shooting Guard, who is essentially the primary shooter on each team. There were 109 Shooting Guards in the league at the time. """

stats.groupby('Position').size()

"""Aside from the Shooting Guard being the most frequent position, the other 4 positions are all similar in frequency, with Small Forward being the least frequent. """

stats.groupby('Age').size()

"""I also wanted to analyze the frequency of each range of Age within the NBA so I can use it for later when I'm visualizing the data. From this info, I see that a majority of the players are in their mid 20's. 

"""

stats.loc[stats['PTS'].idxmax()]

"""I implemented this code to determine the player with the highest Poitns per Game: James Harden. With this scoring data, anyone who drafts Harden to their fantasy team will not get let down"""

stats.loc[stats['AST'].idxmax()]

"""Similar to PPG, APG, or Assists Per Game is a very important statline because it shows which players like to share the wealth on their team. In this case, LeBron James was the leagues leader in Assists, with just over 10 Assists per game. Again, LBJ will not let anyone down with regards to Fantasy Basketball.

"""

stats.loc[stats['TRB'].idxmax()]

"""Adding on to the data that we are about to see, the player position that records the most Total Rebounds Per Game is definitely going to be the big man of the team, or the center. In this case, it's Clint Capela of the Houston Rockets. Total Rebounds is also a statistic that gets a lot of points on Fantasy Basketball teams."""

stats.loc[stats['TOV'].idxmax()]

"""Like many other basketbal fans, I'd think that the player with the highest turnovers would be Russell Westbrook but the stats say otherwise. Having """

stats.loc[stats['PF'].idxmax()]

"""# Vizualizing the Data

"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
from sklearn.cluster import KMeans

#to start off our data analysis we will use a clustering algorithm to create clusters within our data 
k_means = KMeans(init='k-means++', n_clusters=3, random_state=0)
k_means.fit(stats.drop(['Player', 'Position', 'Team'], axis=1))
clus = pd.DataFrame(k_means.labels_, columns = ['Cluster'])
df1 = stats.join(clus)

#now we do analysis to see how our algorithm clustered our data 
sns.lmplot("Cluster", "PTS", df1, x_jitter=.15, y_jitter=.15)

"""Using clustering algorithm to split the data by PTS, or Points Per Game. A cluster graph represents the combination of multiple groups of data, in this case 'player', 'position', and 'points' for the players in the league. """

stats['Age'].hist(figsize=(8,8))

"""From this Histogram grouped by Age, we can see that """

stats['PTS'].hist(figsize=(8,8))

"""By grouping another histogram by PTS, or Points Scored per Game by players, we can see that """

sns.lmplot("Age", "PTS", stats, col="Position", hue="Position", x_jitter=.15, size=5)

sns.lmplot("GP", "PTS", stats, col="Position", hue="Position", x_jitter=.15, size=5)

sns.lmplot("Age", "PTS", stats, x_jitter=.15)

sns.lmplot("FG", "FGA", stats, x_jitter=.30)

"""We can see the relationship between field goals attempted and made by each player in the league. """

sns.lmplot("TOV", "PF", stats, x_jitter=.30)

"""Turnovers and Personal Fouls are a big part of each players, stats. They contribute to a player's +-, and can negatively impact a team in many ways. These negative stats also can make the player lose points on a Fantasy Team on in betting areas.

# Linear Regression
"""

# importing all of the necessary libraries for regression 
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.metrics import explained_variance_score
import statsmodels.formula.api as sm
from bokeh.models import Jitter
from sklearn import linear_model


from sklearn.feature_selection import f_regression
from sklearn.feature_selection import SelectKBest

from sklearn.feature_selection import RFE

from sklearn import linear_model
from sklearn.linear_model import Ridge

plt.figure(figsize=(12,12))
sns.heatmap(stats.corr(), annot=True)

"""This is a heat map of all of the data that we have scraped from Basketball-Reference. A heat map is a data visualization technique that shows magnitude of a phenomenon as color in two dimensions. The more variation of color a data value has, the "higher" the value is seen to be. Very interesting!"""

stats = stats.drop('Player')
stats = stats.drop('Position')
stats= stats.drop('Team')

#assigning columns to X and Y variables
y = stats['PTS'] 
X = stats.drop(['PTS'], axis =1)
reg = linear_model.Ridge (alpha = .1)
reg.fit(X,y) 
reg_y = reg.predict(X)
Ridge(alpha=0.5, copy_X=True, fit_intercept=True, max_iter=None,
      normalize=False, random_state=None, solver='auto', tol=0.001)
print(reg.coef_)

print (reg.intercept_)
print_sep()
print ("mean square error: ", mean_squared_error(y, reg_y))
print_sep()
print("variance or r-squared: ", explained_variance_score(y, reg_y))