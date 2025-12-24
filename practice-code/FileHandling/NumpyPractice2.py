import pandas as pd

data = {
    "Prod": ["Pen", "Pencil", "Eraser"],
    "Qty": [10, 20, 15],
    "Amount": ["1,000", "2,500", "1,200"]
}
df = pd.DataFrame(data)
print(df)

rename_map = {
    "Prod":"Product",
    "Qty" :"Quantity"
}
df = df.rename(columns= rename_map)
print(df.columns)

data = {
    "Product": ["Pen", "Pencil", "Eraser", "Marker"],
    "Quantity": [10, 20, 5, 15],
    "Amount": [100.0, 200.0, 50.0, 150.0]
}
df = pd.DataFrame(data)

filter_df = df[df["Quantity"] > 10]
print(filter_df)

filter_df_1= df[df["Quantity"] > 10 & (df['Amount'] > 100)]
print(filter_df_1)


data = {
    "Region": ["South", "North", "East", "West"],
    "Product": ["Pen", "Pencil", "Eraser", "Marker"],
    "Amount": [150, 200, 100, 180]
}
df = pd.DataFrame(data)
print(df)

df_sorted = df.sort_values("Amount",ascending=False)
print(df_sorted)

df_sorted_1 = df.sort_values(["Region","Amount"])
print(df_sorted_1)

data = {
    "Region": ["North", "South", "East", "West", "South", "North", "West", "East"],
    "Amount": [2000, 1500, 1800, 2200, 1700, 1600, 2100, 1900]
}
df = pd.DataFrame(data)

print(df["Region"].value_counts())

data = {
    "Amount": [150, 200, 100, 180]
}

df = pd.DataFrame(data)
print(df["Amount"].describe())

data = {
    "Region": ["North", "South", "East", "West", "South", "North", "West", "East"],
    "Amount": [2000, 1500, 1800, 2200, 1700, 1600, 2100, 1900]
}

df = pd.DataFrame(data)
print(df)

grp_region  = df.groupby("Region")
grp_region.sum()