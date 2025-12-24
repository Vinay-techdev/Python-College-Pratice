str = "ProgrammingwithPython"
print(str[1:3])

var = "james"*2*3
print(var)

x = 36/4*(3+2)*4+2
print(x)

v1, v2, v3 = 1,2,"3"
#! print(v1+v2+v3)      TypeError: unsupported operand type(s) for +: 'int' and 'str'

y = 2*2**5
print(y)

l1 = []
l1.append([1,[2,3],4])
l1.extend([7,8,9])
print(l1)

print(l1[0][1][1] + l1[2])

l1 = [1,2,3,4]
l2 = l1
l3 = l1.copy()
l4 = l1
print(l1, l2, l3, l4)

l1[0] = 5
print(l1, l2, l3, l4)
