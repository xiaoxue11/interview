class Demo:
    aa = 'This is a static name, shared by all instance'

    def __init__(self, name):
        self.bb = name

    def custom_func(self, name):
        self.cc = name


obj1 = Demo(11)
print(obj1.aa)
print(obj1.bb)
# print(obj1.cc) wrong, have no cc attribute

print('*'*50)
Demo.aa = 111111
obj1.aa = 1
obj1.custom_func(1111)
print(obj1.aa)
print(obj1.bb)
print(obj1.cc)

print('*'*50)
obj2 = Demo(22)
Demo.aa = 222222
obj2.custom_func(2222)

print("obj2.aa = ", obj2.aa)
print("obj2.bb = ", obj2.bb)
print("obj2.cc = ", obj2.cc)
print("Demo.aa = ", Demo.aa)


