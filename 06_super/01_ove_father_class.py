class A:
    def spam(self):
        print('A')


class B(A):
    def spam(self):
        print('B')
        super().spam()


if __name__ == '__main__':
    b = B()
    b.spam()