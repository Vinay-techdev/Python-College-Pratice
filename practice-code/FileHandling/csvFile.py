import csv

#! Reading csv file
#? #1 csv.reader()
# with open("students.csv",'r') as file:
#     reader = csv.reader(file,delimiter=':')
#     for row in reader:
#         print(row)

#? #2 csv.DictReader()

# with open("students.csv",'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)

#? 3 Header - next() -> reads line by line
with open("students.csv",'r') as file:
    reader = csv.reader(file)
    headers1= next(reader)
    headers2= next(reader)
    print("CSV Headers: ", headers1)
    print("CSV Headers: ", headers2)

# # to add
# with open("students.csv",'r') as file:
#     filename = ["Name", "Age", "City"]
#     reader = csv.DictReader(file, fieldnames=filename)
#     for row in reader:
#         print(row)

#! Writing csv file
#? 4. Writing a file -> csv.writer() and writerows()
data = [
    ["Name", "age", "City"],
    ["Virat", 36, "New Delhi"],
    ["Vinay", 21, "karnataka"],
    ["heee", 5, "hooo"],
    ]

with open("output.csv",'w') as file:
    writer =  csv.writer(file)
    writer.writerows(data)