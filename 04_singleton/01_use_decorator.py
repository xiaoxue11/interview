def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


@singleton
class Foo(object):
    a = 1


if __name__ == '__main__':
    foo1 = Foo()
    foo2 = Foo()
    print(foo1 == foo2)
    print(id(foo1))
    print(id(foo2))