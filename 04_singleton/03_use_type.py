class Singleton(type):
    """define a type to achieve singleton"""
    _inst = None

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_inst"):
            cls._inst = super().__init__(cls, *args, **kwargs)
        return cls._inst


class Foo(metaclass=Singleton):
    a = 2


if __name__ == '__main__':
    foo1 = Foo()
    foo2 = Foo()
    print(foo1 is foo2)
    print(id(foo1))
    print(id(foo2))