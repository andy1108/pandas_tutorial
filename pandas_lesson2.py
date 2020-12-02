import pandas as pd
import os

#paths = []
#for file in os.listdir("./Sales_Data/"):
#	if "2019" in file and file.endswith(".csv"):
#		paths.append(file) #add to the end of the list

#print(paths)
#print(os.listdir("./Sales_Data"))
#print("\n")
#paths = [item[0:10] for item in os.listdir("./Sales_Data")]
#inline for statement, assigns the path to temporary variable file
#and adds it to list files
#origin = "./Sales_Data/"
#paths = [item for item in os.listdir(origin[:-1]) if (item.endswith(".csv") and "2019" in item)]
#print(paths)

#all_months_data = pd.DataFrame() #this creates empty dataframe
#print(all_months_data)

#for x in paths:
#	#print(origin+x)
#	df = pd.read_csv(origin+x)
#	all_months_data = pd.concat([all_months_data, df]) #two parameters in list format [new file, file to add]
#	print(all_months_data[all_months_data.columns[0]].count()+1) #counts number of rows
#print(all_months_data.columns[0]) #prints first column - Order ID
#print(len(all_months_data.columns)) #total number of columns

#all the files in the loop are added to the new one (bigger one)
#all_months_data.to_csv("all_data.csv", index=False) #if index=True - Python will add an extra column counting from 0 to number of rows

all_data = pd.read_csv("all_data.csv")
print(all_data["Order Date"].head())

#remove nulls
nan_df = all_data[all_data.isna().any(axis=1)] #what is null - specifically for rows?
print(nan_df.head())
all_data = all_data.dropna(how="all") #any means if the row contains any nulls, all if all are nulls

#remove the "Or" error
all_data = all_data[all_data["Order Date"].str[0:2] != "Or"]

#all_data["Month"] = all_data["Order Date"].str[0:2]+" - "+ all_data["Order Date"].str[6:9] #convert to string before cutting
all_data["Month"] = all_data["Order Date"].str[0:2] 
print(all_data["Month"])
all_data["Month"] = all_data["Month"].astype("int32")

all_data["Quantity Ordered"] = pd.to_numeric(all_data["Quantity Ordered"])
all_data["Price Each"] = pd.to_numeric(all_data["Price Each"])

all_data["Sales"] = all_data["Quantity Ordered"] * all_data["Price Each"]
#print(all_data.columns)

sales_data = all_data["Sales"] #save all data of column sales before moving
all_data.drop(labels=["Sales"], axis=1, inplace = True) #inplace updates itself, without reassigning
all_data.insert(4, "Sales", sales_data) #insert at 4th position (counting from 0), named "Sales" with sales_data
print(all_data.columns)


print(all_data.groupby("Month").sum().sort_values(by=["Sales"], ascending=False))

new_df = all_data.groupby("Product").sum()
print(new_df.sort_values("Product")) #sort by alphabetical order

import matplotlib.pyplot as plt #extra plotting just cause
months = range(1,13)
plt.bar(months, all_data.groupby("Month").sum()["Sales"])
plt.show()






