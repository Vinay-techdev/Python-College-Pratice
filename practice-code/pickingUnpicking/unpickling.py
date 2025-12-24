
#? Unpickling - deserliztion
# unpicking is the process of converting binary format into python object
# Syntax pickle.load(file)

import pickle
file_obj = open("binaryfile.txt", "rb")
loaded_data = pickle.load(file_obj)

print("Loaded data -> ", loaded_data)
file_obj.close()