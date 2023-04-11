# Tiffany Ng
import pandas as pd 
import csv 
import seaborn as sns

# reads csv file and creates a panda file of such data
df = pd.read_csv("AB_NYC_2019 - AB_NYC_2019.csv")
df

# creates a seaborn map
# results show that the columns last_review and reviews_per_month have null values
cols = df.columns
sns.heatmap(df[cols].isnull())

# creates a copy of df2 and replaces NaN values located in columns last_review and reviews_per_month
df2 = df.copy()
df2["last_review"] = df2["last_review"].fillna("No review")
df2["reviews_per_month"] = df2["reviews_per_month"].fillna("No review")
cols = df2.columns
sns.heatmap(df2[cols].isnull())

# creates a copy of df and isolates the year of last_review column
df3 = df.copy()
df3.last_review = df3.last_review.str.slice(0,4)
df3

# prints the amount of AirBNBs in each borough
borough = df3["neighbourhood_group"]
borough_dict = {}

for i in borough:
    if i not in borough_dict:
        borough_dict[i] = 1
    else:
        borough_dict[i] +=1
print(borough_dict)
