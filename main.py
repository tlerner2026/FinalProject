#-------------------------------imports and get date from the web--------------------------------#

import pandas as pd
import matplotlib.pyplot as plt

### write data to csv file
url = "https://www.espn.com/nba/standings/_/group/league"
dfs = pd.read_html(
    url
)
dfs[1].to_csv("orginal.csv")

#-------------------------------condense data--------------------------------#

### get home and away columns
df = pd.read_csv("orginal.csv")
df = df.loc[:,["HOME", "AWAY"]]

### make it into intergers
df[['Home Wins', 'Home Losses']] = df["HOME"].str.split("-", expand = True)
df[['Away Wins', 'Away Losses']] = df["AWAY"].str.split("-", expand = True)

### add an home-road to see the difference
# for home, road in df["Home Wins"],df["Away Wins"]:
#     df[['Home-Road Wins More']] = df["Home Wins"] - int["Away Wins"]

df.to_csv("data.csv")

#-------------------------------make a graph--------------------------------#

df = df[["Home Wins", "Away Wins"]].astype("int")

### this is a bar plot 
df.plot( y = ["Home Wins","Away Wins"], kind = "bar")

### this is a line plot
# df.plot( y = ["Home Wins","Away Wins"])

plt.show()