from functools import reduce
import operator

# square
x = lambda a,b:a+b
print(x(3, 5))

print(True + True + False)
print(type(lambda x: x*2))

#! functions

mylist= [1,2,3,4,5,6]

#? filter
newList = filter(lambda a: (a/3==2), mylist)
print(newList)
print(list(newList))

#? map
square = map(lambda a: (a**2), mylist)
print(list(square))

#? reduce
sum = reduce(lambda a, b: a+b, mylist)
print(sum)

#? zip
l1 = [1, 2, 3,4]
l2 = ['a', 'b', 'c']
zipped = zip(l1, l2)
print(list(zipped))

#? Unzip
ziped = [(1, 'a'), (2, 'b'), (3, 'c')]
list1= zip(*ziped)

print(list(list1))

#? Max
print(max(l1))

#? min
print(min(l1))

#? operator
print(operator.add(4,5))
print(operator.mul(4,5))
print(operator.gt(5,3))
print(operator.lt(5,3))