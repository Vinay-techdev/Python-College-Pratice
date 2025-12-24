
#? Extracing single json data
data = {
    "Name": "Alpha",
    'Age': 29
}

print("Name: ", data['Name'])
print("Age: ", data['Age'])

#? Extracting JSON Content
print("\nExtracting JSON")
for k, v in data.items():
    print(k, v)

#? Extracing nested json data
data = [
    {'name': 'alpha', 'age': 23},
    {'name': 'bob', 'age': 25}
]

print(data[0]['name'])

for entry in data:
    print(entry['name'], entry['age'])


#! load(), loads(), dump(), dumps() 

#? load() is used to read JSON data from a file
#? and convert it into a Python object (usually a dictionary).

import json

with open('sample.json') as file:
    data = json.load(file)
print("\nUsing 'Load' function\n",data)

        #Extracting data
print(data['name'])
print(data['age'])

#? loads() is used to convert a JSON formatted STRING
#? into a Python object (usually a dictionary).

import json

jsonString = '{"nam": "gamma", "age": 21, "skills": ["python", "ML"]}'
data = json.loads(jsonString)

print("\nUsing 'Loads' function\n",data)
print(type(jsonString))
print(data)
print(type(data))

#? dump() is used to convert a Python object into JSON format
#? and store (write) it directly into a JSON file.

import json

student_info = {
    "student_id": 101,
    "department": "CSE",
    "cgpa": 8.7,
    "subjects": ["DS", "OS", "DBMS"]
}

file = open("student.json", "w")
json.dump(student_info, file)
file.close()

print("\nUsing 'dump' function")
print("Data written to JSON file successfully")
print(type(student_info))

#? dumps() is used to convert a Python object
#? into a JSON formatted string.
import json

course_info = {
    "course_name": "Python Programming",
    "duration_weeks": 8,
    "level": "Beginner",
    "topics": ["Basics", "Numpy", "Pandas", "File Handling"]
}

json_text = json.dumps(course_info)

print("\nUsing 'Dumps' function\n", json_text)
print(type(course_info))
print(json_text)
print(type(json_text))
