import requests
from bs4 import BeautifulSoup

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#? Extracting table 
url = "https://www.w3schools.com/html/html_tables.asp"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

table = soup.find("table", {"id": "customers"})
row_list = []

for row in table.find_all("tr"):
    cells = row.find_all("td")
    if cells:
        row_list.append([cell.get_text(strip = True) for cell in cells])

print("List output:\n")
print(row_list)

#? Converting extracting data into data frame
df = pd.DataFrame(row_list, columns=["Company", "Contact", "Country"])
print("\n Extracted Data Frame:\n",df)

#! Basic Exploration

#? 1. Basic information
print("\n1. DataFrame Info\n")
print(df.info())

#? 2. Number of rows and columns
print("\n2. Shape of DataFrame")
print(df.shape)

#? 3. First 3 rows
print("\n3. First 3 rows")
print(df.head(3))

#? 4. Last 3 rows
print("\n4. Last 3 rows")
print(df.tail(3))

#! Handling Missing Data

#? 4. Remove rows with missing values
df_no_missing = df.dropna()
print("\n4. After dropping missing values")
print(df_no_missing)

#? 5. Drop Country column
df_no_country = df_no_missing.drop("Country", axis=1)
print("\n5. After dropping Country column")
print(df_no_country)

#! String Operations

#? 6. Split Contact into First_Name and Last_Name
df_no_missing[["First_Name", "Last_Name"]] = df_no_missing["Contact"].str.split(" ", expand=True)
print("\n6. After splitting Contact column")
print(df_no_missing)

#! Descriptive Statistics

#? 7. Count, mean, min, max, std of Revenue
print("\n7. Statistics of Revenue")
df["Revenue"] = [1000, 1500, 1200, 1800, 1600, 1700]
print("Count:", df["Revenue"].count())
print("Mean:", df["Revenue"].mean())
print("Min:", df["Revenue"].min())
print("Max:", df["Revenue"].max())
print("Std:", df["Revenue"].std())

#? 8. Describe method
print("\n8. Using describe()")
print(df["Revenue"].describe())

#? 9. Smallest and largest values
print("\n9. Smallest Revenue:", df["Revenue"].min())
print("Largest Revenue:", df["Revenue"].max())

#? 10. Mean and Median
print("\n10. Mean:", df["Revenue"].mean())
print("Median:", df["Revenue"].median())

#? 11. Difference between consecutive values
print("\n11. Difference between consecutive Revenue values")
print(df["Revenue"].diff())

#! Value Counts

#? 12. Count companies per country
print("\n12. Number of companies per country")
print(df["Country"].value_counts())

#! Visualization - Matplotlib

#? 13. Histogram
plt.hist(df["Revenue"])
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.show()

#? 14. Boxplot
plt.boxplot(df["Revenue"])
plt.title("Revenue Boxplot")
plt.ylabel("Revenue")
plt.show()

#? 15. Line graph
plt.plot(df["Revenue"])
plt.title("Revenue Across Rows")
plt.xlabel("Index")
plt.ylabel("Revenue")
plt.show()

#? 16. Bar graph for companies per country
df["Country"].value_counts().plot(kind="bar")
plt.title("Companies per Country")
plt.xlabel("Country")
plt.ylabel("Count")
plt.show()

#? Scatter plot: Revenue vs Index
plt.scatter(df.index, df["Revenue"], color="green", marker="o")
plt.xlabel("Index")
plt.ylabel("Revenue")
plt.title("Scatter Plot: Revenue")
plt.show()

#? Violin plot
sns.violinplot(y=df["Revenue"], color="skyblue")
plt.ylabel("Revenue")
plt.title("Violin Plot of Revenue")
plt.show()