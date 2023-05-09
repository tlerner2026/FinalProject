import pandas as pd
import matplotlib.pyplot as plt

# wrtie data to csv file


# url = "https://www.espn.com/nba/standings/_/group/league"
# dfs = pd.read_html(
#     url
# )
# dfs[1].to_csv("standings.csv")


# get home and away columns
df = pd.read_csv("standings.csv")
df = df.loc[:,["HOME", "AWAY"]]

#make it into intergers
for index, row in df.iterrows():
    print(row)


#make a graph

#df = df[["Home", "Road"]].astype("int")
#print(df.info())
#df.plot(x = ["Home","Road"], y = "Win %")
#plt.show()