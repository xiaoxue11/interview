# list comprehension
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i for i in a if i < 5]
print(b)

# filter
c = filter(lambda x: x < 5, a)
print(list(c))

b = {}
b = b.fromkeys(a)
c = list(b.keys())
print(c)

list_data = [1, 2, 5, 8, 10, 3, 18, 6, 20]
print(list_data[::2])

l1 = [1, 3, 2, 5, 4]
for i in range(len(l1)):
    print(l1.insert(0, l1.pop(i)))
    print(l1)


def multi():
    return [lambda x: i*x for i in range(4)]


for m in multi():
    print(m)
print([m(3) for m in multi()])

a = 10
b = 20
c = [a]
a = 15
print(c)

print(dir('a'))
print("*"*50)
print(list(map(lambda x: x*x, [y for y in range(3)])))
# print(list_data.count())

print(1/4+0.75)
print(dict(([1, 2], [3, 4])))
print(set('123'))
temp = frozenset((1, 2, 4))
print(type(temp))
print(temp)
print('hello' is 'hello')
a=b=c=1
a+=b
a,b=b,a
x=[1,2]
y=[3,4]
print(x+y)

num=8
if num>=0 and num<=10:
    print(num)