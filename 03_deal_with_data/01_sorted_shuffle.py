import random

list1 = [1, 2, 3, 4, 5]
random.shuffle(list1)
print(list1)

d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
print(sorted(d.items(), key=lambda x: x[1]))
print(sorted(d.items(), key=lambda x: x[0]))

str1 = "k:1|k1:2|k2:3|k3:4"
ret = {}
for item in str1.split('|'):
    key, value = item.split(':')
    ret[key] = int(value)
print(ret)

alist = [{"name": "a", "age": 20}, {"name": "b", "age": 30}, {"name": "c", "age": 25}]
for i in alist:
    print(i.__getitem__('age'))
print(sorted(alist, key=lambda x: x.__getitem__('age'), reverse=True))
