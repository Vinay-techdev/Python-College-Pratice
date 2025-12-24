
#? Picking - serlization
# picking is the process of converting a python object into binary format
# it can be saved to file or transferred over network


#? What can be picked in python?
# 1. Data type 
# 2. custom class an objects
# 3. Functions
# 4. DataFrame in machine learning
# 5. list, tuples, sets and dict

#! What cannot b picked
# 1. Lambda function
# 2. Nested Functions and local functions
# 3. Sockets,
#? syntax - pickle.dump(object, file)

import pickle
grade_list = ['A', 'B', 'C', 'D', 'E']
file_obj = open("binaryfile.txt", "wb")

pickle.dump(grade_list, file_obj)
print("pickle stores data in abinary format which is not readble format")
file_obj.close()