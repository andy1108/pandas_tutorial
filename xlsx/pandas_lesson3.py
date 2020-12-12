import pandas as pd 

#reading the excel file
df = pd.read_excel("sample-xls-file-for-testing.xls")
#open command prompt --> pip install xlrd

print(df.head(10))
print(df.columns)

rank = df.groupby("Country").sum().sort_values(by=[" Sales"],ascending=False).reset_index()
#reset_index turns rank into a dataframe again, because if you don't you cannot use country columnn since it's no longer one
print(rank)
r = [i for i in rank["Country"]] #take values from rank and put them in list
print(r)

df.insert(16, "Rank", "") #add new column
print(df.columns)

for position, row_value in df.iterrows(): #how you go row by row
	#assign new value to a certain column based on r list and position in it
	df.at[position, "Rank"] = r.index(row_value["Country"])+1 #.index() can be used for lists to find position of item

print(df.head(20))

df.to_excel("new_edited.xlsx", index=False) #index false is no extra column with numbers

