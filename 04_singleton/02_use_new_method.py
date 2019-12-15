class Singleton(object):
    """define singleton class"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__init__(cls, *args, **kwargs)
        return cls._instance


class Foo(Singleton):
    a = 1


if __name__ == '__main__':
    foo1 = Foo()
    foo2 = Foo()
    print(foo1 == foo2)
    print(id(foo1))
    print(id(foo2))
