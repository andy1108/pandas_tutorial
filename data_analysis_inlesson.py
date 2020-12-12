import pandas as pd 

all_data = pd.read_csv("all_data.csv")

#what time should we display ads to maximise sales likelihood

#print(all_data.head())
#print(all_data["Order Date"].head())
#print(all_data.columns)

all_data["Order Date"] = all_data["Order Date"].str[8:14]
#print(all_data["Order Date"].head())
#all_data["Order Date"] = all_data["Order Date"].apply(pd.to_datetime)
#to date time is inbuilt function into pandas, to convert dates into actual date variable
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html

all_data.insert(6, "Hour", all_data["Order Date"].str[1:3])
all_data.insert(7, "Minute", all_data["Order Date"].str[4:7])

#hours = [hour for hour, df in all_data.groupby("Hour")]
hours = []
for hour, df in all_data.groupby("Hour"):
	#print(str(hour) + " \n " + str(df))
	hours.append(hour)

#print(hours) #x-axis for graph

y_value = all_data.groupby("Hour").count() #returns number of rows for that specific group

import matplotlib.pyplot as plt  #same as - from matplotlib import pyplot
#faster to type if you use "as"

# plt.plot(hours, y_value)
# plt.xlabel("Hours")
# plt.ylabel("Number of orders")
# plt.grid()
# plt.show()

#What products are most often sold together?

#find all rows with duplicate order id
df = all_data[all_data["Order ID"].duplicated(keep=False)]
#keep: first, last, False ---- first - removes the first instance of the duplicate, last removes the last instance of the duplicate and false keeps all of them

print(df)

df["Grouped"] = df.groupby("Order ID")["Product"].transform(lambda x: ",".join(x)) #assign product name to x, and then join them with a comma in between one by one
print(df["Grouped"])

#looks like this now:
#123 - Iphone jhaflksajflksajdflkaj Iphone MacBook Charger
#123 - MacBook jhaflksajflksajdflkaj Iphone MacBook Charger
#123 - Charger jhaflksajflksajdflkaj Iphone MacBook Charger

df = df[["Order ID", "Grouped"]].drop_duplicates() #drop duplicates and only keep id and grouped columns

from itertools import combinations
from collections import Counter

count = Counter()

for row in df["Grouped"]:
	row_list = row.split(",") #makes individual lists for each row where each item is separated by comma
	#print(row_list)
	count.update(Counter(combinations(row_list, 2))) #counts the number of combinations of the items in row list in pairs of 2

#x_axis = [str(key) for key in count]
#y_axis = [int(count.get(key)) for key in count]

#plt.bar(x_axis, y_axis)
#plt.xticks(x_axis, rotation="vertical", size=8)
#plt.show()







