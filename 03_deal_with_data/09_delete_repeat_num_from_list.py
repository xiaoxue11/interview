def method1(a):
    """use set method to delete the repeat number"""
    b = list(set(a))
    print(b)


def method2(a):
    """use copy list method"""
    li = []
    for i in a:
        if i not in li:
            li.append(i)
    print(li)


def method3(a):
    """use dict keys unique"""
    b = {}
    b = b.fromkeys(a)
    print(list(b.keys()))


if __name__ == '__main__':
    num = [1, 2, 4, 2, 4, 5, 7, 10, 5, 5, 7, 8, 9, 0, 3]
    method1(num)
    method2(num)
    method3(num)
