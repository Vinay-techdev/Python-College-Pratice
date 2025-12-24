import csv


# 1. CREATE CSV FILE WITH 20 ROWS + SOME MISSING MARKS

file = open('students.csv', 'w', newline='')
writer = csv.writer(file)

# Writing header
writer.writerow(["SRN", "Name", "Sub1", "Sub2", "Sub3"])

# Writing 20 rows (some have missing values "")
writer.writerow(["01", "Rahul", 85, 76, 90])
writer.writerow(["02", "Sneha", 92, "", 81])          
writer.writerow(["03", "Arjun", 70, 65, 72])
writer.writerow(["04", "Kiran", 55, "", 58])       
writer.writerow(["05", "Megha", 30, 28, 32])
writer.writerow(["06", "Ramesh", 88, 79, ""])        
writer.writerow(["07", "Pooja", "", 93, 89])          
writer.writerow(["08", "Anil", 67, 72, 69])
writer.writerow(["09", "Priya", 82, 77, 85])
writer.writerow(["10", "Vishal", 44, 39, 41])
writer.writerow(["11", "Deepa", 98, 92, 95])
writer.writerow(["12", "Manoj", 74, 70, 73])
writer.writerow(["13", "Lakshmi", "", 65, 60])        
writer.writerow(["14", "Ishaan", 58, 53, 55])
writer.writerow(["15", "Geetha", 47, 50, 45])
writer.writerow(["16", "Sanjay", 90, 88, 87])
writer.writerow(["17", "Harini", 76, 80, 78])
writer.writerow(["18", "Naveen", 83, 85, 81])
writer.writerow(["19", "Swathi", 72, 68, 75])
writer.writerow(["20", "Karthik", 95, 94, 96])

file.close()