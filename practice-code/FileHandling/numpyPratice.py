import numpy as np
import pandas as pd

#? DATAFRAME WITH MISSING VALUES

data = {
    "Age": [20, 22, np.nan, 21, np.nan]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)


#? Filling missing values using MEAN
#? (use ONLY one method)

df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nAfter filling missing values (Mean):")
print(df)

#? ANOTHER DATAFRAME

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 22, 21],
    "City": ["Delhi", "Mumbai", "Chennai"]
}

df = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df)

#? Drop column (correct column name)

df = df.drop("City", axis=1)

print("\nAfter dropping City column:")
print(df)

#? Apply
print("\nAfter Applying :")
df = df.apply(
    lambda col: col.str.replace(r'[\"\\]', '', regex=True)
    if col.dtype == "object" else col
)
print(df)
