import csv
import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

# Web Scraping
data = []
head = 'no' # to extract header once

for years in range(1977,2022):
    year = years
    url = f'https://www.fangraphs.com/leaders.aspx?pos=all&stats=bat&lg=all&qual=0&type=8&season={year}&month=0&season1={year}&ind=0&team=0,ts&rost=0&age=0&filter=&players=0&startdate=&enddate='
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    table = soup.find('table', attrs={'id':'LeaderBoard1_dg1_ctl00'})
    
    # to extract header once
    if head =='no':
        headers = [i.text.strip() for i in table.findAll('th')][1:]
        headers.append('yearID')
        data.append(headers)
        head = 'yes'
    
    rows = table.find('tbody').findAll(['tr'])

    for n in range(len(rows)):
        stats = [i.text.strip() for i in rows[n]]
        stats = pd.Series(stats)
        stats = stats.drop([0,1],axis=0) # get rid of 'order No.'
        stats.iloc[-1] = year # add season in column with no values
        data.append(stats)

df = pd.DataFrame(data)
df.columns = df.iloc[0] # set header
df = df.drop(df.index[0]) # drop header row


# for convineince, we need to merge with lahman dataset
# to contain same teamIDs
df_teams = pd.read_csv('/Users/jinc/Desktop/프로젝트/baseball_analysis/baseball_analysis/lahman/core/Teams.csv')
# select only stats above year 1976
df_teams = df_teams[df_teams['yearID'] > 1976][['name','yearID','teamID']]


# Fangraph only contains team name ex) Braves, Red Sox..
# Lahman contains full team name ex) Atlanta Braves, Boston Red Sox..

#Extract team names from fangraph
ext = '|'.join(r"{}".format(x) for x in df.Team)
# Extract 'ext' from from Lahman team names
df_teams['Team'] = df_teams.name.str.extract('('+ext+')',expand=False)
# merge based on the extracted team names
df = df.merge(df_teams[['Team','yearID','teamID']], how='left', on=['Team','yearID'])

# save as csv
df.to_csv('fangraph_bat.csv', index=False)