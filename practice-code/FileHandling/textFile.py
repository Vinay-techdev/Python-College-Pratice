
#! Opening file in read mode
file = open("students.txt","r")
print(file) # Print Object of file

#? read
f = open("students.txt","r")
print("name of the file is ",f.name)
print(f"The file is open in {f.mode} mode")

st = f.read()
print(st)

f.close()

# with
with open("students.txt","r") as file:
    content = file.read()
    print(content)

#Readline
f = open("students.txt","r")
str1 = f.readline()
print("Readline - ",str1)

# Readlines
f = open("students.txt","r")
str1 = f.readlines()
print("Readlines - ",str1)



#! Opening file in write mode
file = open("students.txt", "w")
print(file)   # Prints file object

# ? write
f = open("Employees.txt", "w")
print("Name of the file is :", f.name)
print(f"The file is open in {f.mode} mode")

# Writing data
f.write("Rahul - 85\n")
f.write("Sneha - 92\n")
f.write("Arjun - 78\n")
f.write("Megha - 88\n")

f.close()
print("Data written successfully!\n")

# with
with open("students.txt", "w") as file:
    file.write("This content is written using WITH block.\n")
    file.write("With automatically closes the file.\n")

print("Data written using 'with' block.\n")

# Write single line using writelines
f = open("students.txt", "w")
lines = [
    "Line 1: Hello Student\n",
    "Line 2: Welcome to Python File Handling\n",
    "Line 3: This is writelines()\n"
]
f.writelines(lines)
print("Data written using writelines()\n")
f.close()
