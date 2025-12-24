
#? Q1
fruits = ['apple', 'banana', 'cherry', 'date', 'fig']
print(fruits[1:4])     
print(fruits[:-2])     
print(fruits[::-1])   

#? Q2
data = "DataScience"
print(data[2:10:2])   

#? Q3
text = "ABCDEFGHIJ"
print(text[8:2:-2]) 

#? Q4
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
sub_matrix = [row[1:3] for row in matrix[0:2]]
print(sub_matrix)  

#? Q5
values = list(range(10))
filtered = values[::2]
print(filtered) 

#? Q6
nums = [10, 20, 30, 40, 50, 60, 70]
print(nums[1:6:2])   
print(nums[-5:-1:2]) 
print(nums[::-3])  

#? Q7
nums = [1, 2, 3, 4, 5]
nums[1:4] = [20, 30]  
print(nums)

#? Q8
text = "abcdefghij"
print(text[7:2:-1])   
print(text[2:7])  