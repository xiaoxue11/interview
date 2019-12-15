import copy

def copy_attr(s):
	s1 = copy.copy(s)
	s2 = copy.deepcopy(s)
	return s1, s2
# immutable data type
# int
a = 3
b = 3
c, d = copy_attr(a)
print(a is b)
print(a is c)
print(a is d)
print('*'*20 + 'int')
# str
a = 'python'
b = 'python'
c, d = copy_attr(a)
print(a is b)
print(a is c)
print(a is d)
print('*'*20+ 'str')
# tuple
a = (1, 3)
b = (1, 3)
e = a
c, d = copy_attr(a)
print(a is b)
print(a is c)
print(a is d)
print(a is e)
print('*'*20+'tuple')
# list
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
e = a
c, d = copy_attr(a)
a.append(5)
print(a is b)
print(a is c)
print(a is d)
print(a is e)
print(a[0] is c[0])
print(a[0] is d[0])
print(e)
print('*'*20+'list')

#list nest list
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)
new_list2 = copy.deepcopy(old_list)

print("Old list:", old_list)
print("New list:", new_list)
old_list.append([6, 6, 6])
print("Old list:", old_list)
print("New list:", new_list)
old_list[0].append(6)
print("Old list:", old_list)
print("New list:", new_list)
print("New list:", new_list2)






# x = [1, 2, 3, 4]
# y = x
# print(id(x))
# print(id(y))
# print(x == y)
# print(y is x)
# x = [1, 2, 3, 4]
# y = x[:]
# print(id(x))
# print(id(y))
# print(x == y)
# print(y is x)
# x = [1, 2, 3, 4]
# y = copy.copy(x)
# print(id(x))
# print(id(y))
# print(x == y)
# print(y is x)
# x = [1, 2, 3, 4]
# y = copy.deepcopy(x)
# print(id(x))
# print(id(y))
# print(x == y)
# print(y is x)
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# x = [a, b]
# y = copy.deepcopy(x)
# x.append(['new_add'])
# a.append(11)
# print(x)
# print(y)
# print(id(a))
# print(id(x[0]))
