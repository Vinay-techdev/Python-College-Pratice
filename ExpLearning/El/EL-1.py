
#? Q1 
aList = [4, 8, 12, 16]
aList[1:4] = [20, 24, 28]
print(aList)

#? Q2
sampleList = [10, 20, 30, 40] 
del sampleList[0:6]
print(sampleList)

#? Q3
aList = [10, 20, 30, 40, 50 ,60, 70, 80]
print(aList[2:5])

#? Q4
print(aList[:4])

#? Q5
print(aList[3:])

#? Q6
samList = [10, 20, 30, 40, 50]
samList.append(60)
print(samList)

#? Q7
list = [5, 10, 15, 25]
print(list[::-2])

#? Q8
list2 = ['xyz', 'zara', 'python']
print(max(list2))

#? Q9
l = [None] * 10
print(len(l))

#? Q10
print({1, 2, 3, 4, 5} - {3, 4} ^ {5, 6, 7})

#? Q11
x = {1, 2, 3}
y = {1, 2}
print(y.issubset(x))

#? Q12
s = {'foo', 'bar','baz', 'qux'}
s = {'bar'}
print(s)

#? Q13
s = {'foo', 'bar','baz', 'qux'}
s &= {'foo', 'bar','baz'}
print(s)

#? Q14
s = {'foo', 'bar','baz', 'qux'}
s.discard('bar')
print(s)

#? Q15
l1 = []
l1.append([1, [2,3], 4])
print(l1)

#? Q16
l1.extend([7, 8, 9])
print(l1[0][1][1] + l1[2])

#? Q17
ls1 = [1, 2, 3, 4]
ls2 = ls1
ls3 = l1.copy()
ls4 = ls1
print(ls1, ls2, ls3, ls4)

#? Q18
ls1[0] = [5]
print(ls1, ls2, ls3, ls4)

#? Q19
L = [1, 3,5, 7, 9]
print(L.pop(-3), end=' ')

#? Q20
a = {"python" : 1, "programs": 2}
b = {'python': 2, 'programs': 1}
print(a == b)

#? Q21
dic1= {'GoogleDocs': 1, 'Google': 2, 'googledocs': 3}
print(dic1['googledocs'])

#? Q22
d1 = {'jhon': 40, 'peter': 45}
d2 = {'jhon': 466, 'peter': 45}
print(d1>d2)

#? Q23
test = {1: 'A', 2: 'B', 3: 'C'}
del test[1]
test[1] = 'D'
del test[2]
print(len(test))

#? Q24
a={}
a['a']=1
a['b'] = [2, 3,4]
print(a)


# El Contiue......

# ? Q1
string = input("Enter string: ")

result = {ch: {i for i, c in enumerate(string) if c == ch} for ch in set(string)}
print(result)

#? Q2
l = ["Virat", "ABD", "KL Rahul", "Hardik Pandey"]

dict1 = {name: len(name) for name in l}
print(dict1)

# using anonymous function

#? Q3

employees = {"John": 45000, "Alice": 55000, "Bob": 40000}
sorted_employees = dict(sorted(employees.items(), key=lambda x: x[1]))
print(sorted_employees)

#? Q4

s = "hello world"
freq = {ch: s.count(ch) for ch in set(s)}
print(freq)

#? Q5
words = ["apple", "idea", "orange", "sky", "echo"]
vowels = 'aeiouAEIOU'

isVowels = filter(lambda x: x[0] in vowels and x[-1] in vowels,words)
print(list(isVowels))

#? Q6
import random

# My Method
num = random.randrange(1, 50)
if(num <= 15):
    print("Number is low: ", num)
elif(num <= 35):
    print("Number is Med", num)
elif(num <= 50):
    print("Number is High: ", num)

# LLM Code
nums = [random.randint(1, 50) for _ in range(10)]
categories = list(map(lambda x: "Low" if x <= 15 else "Medium" if x <= 35 else "High", nums))
print("Numbers:", nums)
print("Categories:", categories)

#? Q7

def func():
    print("hello")

#! a = del func - SyntaxError: invalid syntax
del func
func()