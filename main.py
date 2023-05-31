#-------------------------------imports and get date from the web--------------------------------#

### imports
import pandas as pd
import matplotlib.pyplot as plt
import math
import matplotlib.patches as mpatches

### write data to csv file
year = input("What year do you want? 2016 to 2023: ")
url = f"https://www.espn.com/nba/standings/_/season/{year}/group/league"
dfs = pd.read_html(
    url
)

### write the data to files
with open("teams.txt", "w") as f:
    f = f.write(str(dfs[0]))
dfs[1].to_csv("orginaldata.csv")

#-------------------------------condense data--------------------------------#

### get home and away columns
df = pd.read_csv("orginaldata.csv")
df = df.loc[:,["HOME", "AWAY"]]

### make it into intergers
df[['Home Wins', 'Home Losses']] = df["HOME"].str.split("-", expand = True)
df[['Away Wins', 'Away Losses']] = df["AWAY"].str.split("-", expand = True)

### write to file
df.to_csv("newdata.csv")

### read fom file file
df = pd.read_csv("newdata.csv")
df = df.loc[:,["Home Wins", "Away Wins"]]

### make the intergers into %
def win_percentage(value):
    """
    takes a parameter 'value' which is 'Home' or 'Away' and turns them into a data frame.
    """
    percentages = []
    for row in df[f"{value} Wins"]:
        percentages.append(str(math.ceil((int(row) / 41) * 100)))
    df[f"{value} Wins %"] = percentages

### call the functions
win_percentage("Home")
win_percentage("Away")

### percentages for home-away this is different formula than above
percentages_home_minus_away = []
for i in range(len(df["Home Wins %"])):
    home_row = df["Home Wins %"][i]
    away_row = df["Away Wins %"][i]
    percentages_home_minus_away.append(str(int(home_row)-int(away_row)))
df["Home-Away Wins %"] = percentages_home_minus_away

### make average lines
def average_line(value):
    """
    takes the parameter 'value' which is either 'Home' or 'Away' or 'Home-Away' it then returns a list 
    of the average for that location.
    """
    average = []
    total = 0
    for row in df[f"{value} Wins %"]:
        total += int(row)*100
    total = total/30
    total = math.ceil((total/100))
    for _ in range(30):
            average.append(total)   
    return average

### write a list of teams
teams = []
with open("teams.txt", "r") as f:
     all_teams = f.readlines()
     for line in all_teams:
        slice = line.index("-")
        team = line[slice+2:slice+5]

        if team == 'GSG':
            team = 'GSW'
        elif team == 'NON':
            team = 'NOP'
        elif team == 'NYN':
            team = 'NYK'

        teams.append(team)
df["Teams"] = teams

### write to file
df.to_csv("newdata.csv")

#-------------------------------make a graph--------------------------------#

### make lists into correct data types
df = df[["Home Wins %", "Away Wins %", "Home-Away Wins %", "Teams"]].astype({
    "Home Wins %": int,
    "Away Wins %": int,
    "Home-Away Wins %": int,
    "Teams": str
    })

### create a legend and titles
fig, ax = plt.subplots()
red_patch = mpatches.Patch(color='red', label='Home Win %')
blue_patch = mpatches.Patch(color='blue', label='Away Win %')
black_patch = mpatches.Patch(color='black', label='Home-Away Win %')
ax.legend(handles=[red_patch, blue_patch, black_patch])
ax.set_xlabel('Teams')
plt.xticks(rotation = 90)
ax.set_ylabel('Win %')
ax.set_title('Importance of Home-Court in the NBA')

## plot the data with scatter plots and lines for averages
plt.scatter(x = df["Teams"], y = df["Home Wins %"], color = "red")
plt.scatter(x = df["Teams"], y = df["Away Wins %"], color = "blue")
plt.scatter(x = df["Teams"], y = df["Home-Away Wins %"], color = "black")
plt.plot(average_line("Home"), color = "red", linestyle="dashed", linewidth = 2)
plt.plot(average_line("Away"), color = "blue", linestyle = "dashed", linewidth = 2)
plt.plot(average_line("Home-Away"), color = "black", linestyle = "dashed", linewidth = 2)
plt.xlim(-0.5, 29.5)
plt.tight_layout()

### save the figure 
# plt.savefig(f"graph_{year}.png")

### show the plot
plt.show()