class A:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def myprint(self):
        print('a={}, b={}'.format(self.__a, self.__b))

    def __call__(self, num):
        print('call: {}'.format(num+self.__b))


if __name__ == '__main__':
    a = A(10, 20)
    a.myprint()
    a(80)
