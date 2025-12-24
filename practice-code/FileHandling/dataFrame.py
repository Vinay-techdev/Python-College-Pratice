import pandas as pd

#? Empty Data Frame
dfEmpty = pd.DataFrame()
print(dfEmpty)

#? Data Frame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 22, 21],
    "City": ["Delhi", "Mumbai", "Chennai"]
}

df = pd.DataFrame(data)
print(df)

#? Reading Excel file
# dfxl = pd.read_excel("Employess.xlsx")
# print(dfxl)

#? Displaying 1st few row and last few rows from given data
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 22, 21],
    "City": ["Delhi", "Mumbai", "Chennai"]
}
dfCount = pd.DataFrame(data)

print(dfCount.head(1))
print(dfCount.tail(1))

print(dfCount.shape)
print(dfCount.columns)
print(dfCount.index)
#? Checking data type
print(dfCount.dtypes)

#? Changing data type
df["Age"] = df['Age'].astype('Int16')

#? Loaction
print("\nLocation\n",dfCount.loc[0:3])

print("\nName\n",dfCount["Name"])
print("\nAge\n",dfCount["Age"])
print("\nAge\n",dfCount["City"])

#? Missing value
print(df.isna().sum())