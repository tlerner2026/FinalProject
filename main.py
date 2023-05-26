#-------------------------------imports and get date from the web--------------------------------#

import pandas as pd
import matplotlib.pyplot as plt
import math

### write data to csv file
# url = "https://www.espn.com/nba/standings/_/group/league"
# dfs = pd.read_html(
#     url
# )
# dfs[1].to_csv("orginal.csv")

#-------------------------------condense data--------------------------------#

### get home and away columns
df = pd.read_csv("orginal.csv")
df = df.loc[:,["HOME", "AWAY"]]

### make it into intergers
df[['Home Wins', 'Home Losses']] = df["HOME"].str.split("-", expand = True)
df[['Away Wins', 'Away Losses']] = df["AWAY"].str.split("-", expand = True)

### write to file
df.to_csv("data.csv")

### read fom file file
df = pd.read_csv("data.csv")
df = df.loc[:,["Home Wins", "Away Wins"]]

### make the intergers into %
percentages_home = []
for row in df["Home Wins"]:
    percentages_home.append(str(math.ceil((int(row) / 41) * 1000)))
df["Home Wins %"] = percentages_home

percentages_away = []
for row in df["Away Wins"]:
    percentages_away.append(str(math.ceil((int(row) / 41) * 1000)))
df["Away Wins %"] = percentages_away

percentages_home_minus_away = []
for i in range(len(df["Home Wins %"])):
    home_row = df["Home Wins %"][i]
    away_row = df["Away Wins %"][i]
    percentages_home_minus_away.append(str(int(home_row)-int(away_row)))

df["Home-Away Wins %"] = percentages_home_minus_away

teams = ["MIL", "BOS", "PHI", "DEN", "MEM", "CLE", "SAC", "NYK", "PHX", "BKN", "MIA", "LAC", "GSW", "LAL", "MIN", "NOP", "ATL", "TOR", "CHI", "OKC", "DAL", "UTA", "IND", "WAS", "ORL", "POR", "CHA", "HOU", "SAS", "DET"]
df["Teams"] = teams

### write to file
df.to_csv("data.csv")

### add make averages ************** not sure how to do this
#-------------------------------make a graph--------------------------------#

df = df[["Home Wins %", "Away Wins %", "Home-Away Wins %", "Teams"]].astype({
    "Home Wins %": int,
    "Away Wins %": int,
    "Home-Away Wins %": int,
    "Teams": str
    })

## this is a scatter plot 
plt.scatter(x = df["Teams"], y = df["Home Wins %"], color = "red")
plt.scatter(x = df["Teams"], y = df["Away Wins %"], color = "blue")
plt.scatter(x = df["Teams"], y = df["Home-Away Wins %"], color = "yellow")

plt.show()