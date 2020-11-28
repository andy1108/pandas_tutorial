import pandas as pd 


df = pd.read_excel("pokemon_data.xlsx") #loads the excel file

#print(df)

#print(df.head())
#print(df.tail())

#print(df.columns)

#print(df["Name"][0:10])

print(df[["Name", "Speed", "HP"]])

print("-----------------")
print(df.iloc[1]) #locates based on index number
print("-----------------")
print(df.iloc[2:4])
print("-----------------")
print(df.loc[(df["Type 1"] == "Fire")]) #locates based on attribute value for column specified
print(df[df["Type 1"].isin(["Fire"])]) #looks in the column for rows with multiple possible attributes
#to note that .isin() only takes lists "[]" even for one item
print("-----------------\n\n\n\n")
print(df.head())
useless_rows = [0,1,2]
df1 = df.drop(useless_rows, axis=0)#can use array instead of manual list
#axis 0 is rows, axis 1 is columns
indexNames = df[df["Type 1"] == "Fire"].index #finds all rows with condition specified, puts all index values of those rows in the indexname variable
df = df.drop(indexNames, axis = 0) #pass indexnames as rows to remove
print(df["Type 2"])

df = df.dropna(axis = 0) #default axis value is 0 (can ommit)

print(df["Type 2"])

print(df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison")]) #filter with multiple rows

names = df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison")].index #multiple conditions
print(names)
df = df.drop(names, axis = 0) #pass indexnames as rows to remove

print(df)

df["Type 1"] = df["Type 1"].str.replace("Grass", "Leaf")
#type 1 is now equal to = type 1 but instead of grass, replace it with leaf

editing = df.loc[df["Type 2"] == "Poison"].index

for i in editing:
	print("This is index number " + str(i))
	print("\n")
	df.loc[i]["Type 1"] = "Pencil" #this doesn't work
	df.at[i, "Type 1"] = "Pencil" #at index i, column Type 1 change it to pencil
	print(df.loc[i])



