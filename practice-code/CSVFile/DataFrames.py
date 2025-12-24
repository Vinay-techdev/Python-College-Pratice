import csv
import pandas as pd

file = open("students.csv", "r")
reader = csv.reader(file)

print("\n--- CSV CONTENT ---")
for row in reader:
    print(row)

file.close()

# 3. CREATE DATAFRAME FROM CSV

df = pd.read_csv("students.csv")

print("\n--- DATAFRAME LOADED ---")
print(df)

# 4. HANDLE MISSING VALUES
# Convert all marks to numeric and replace missing values with 0

df['Sub1'] = pd.to_numeric(df['Sub1'], errors='coerce').fillna(0)
df['Sub2'] = pd.to_numeric(df['Sub2'], errors='coerce').fillna(0)
df['Sub3'] = pd.to_numeric(df['Sub3'], errors='coerce').fillna(0)

print("\n--- AFTER FILLING MISSING VALUES ---")
print(df)


# 5. FILTER: Display students whose TOTAL > 255 (85*3 subjects)

df['Total'] = df['Sub1'] + df['Sub2'] + df['Sub3']
high = df[df['Total'] > 255][['SRN', 'Name', 'Sub1', 'Sub2', 'Sub3', 'Total']]

print("\n--- STUDENTS WITH TOTAL > 255 ---")
print(high)

# 6. DROP STUDENTS HAVING MARKS < 35 IN ANY SUBJECT

df = df[(df['Sub1'] >= 35) & (df['Sub2'] >= 35) & (df['Sub3'] >= 35)]

print("\n--- AFTER DROPPING MARKS < 35 ---")
print(df)


# 7. DISPLAY FIRST 10 AND LAST 10 ROWS

print("\n--- FIRST 10 ROWS ---")
print(df.head(10))

print("\n--- LAST 10 ROWS ---")
print(df.tail(10))