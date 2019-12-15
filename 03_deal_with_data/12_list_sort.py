def main(s):
    if isinstance(s, str):
        li = [int(i) for i in s]
        print(li)
    li.sort(reverse=True)
    for i in range(len(li)):
        if li[i] % 2 > 0:
            li.insert(0, li.pop(i))
    print("".join(str(x) for x in li))


def func2(l):
    print("".join(sorted(l, key=lambda x: int(x) % 2 == 0 and 20 - int(x) or int(x))))


def func3(l):
    print("".join(sorted(l, key=lambda x: (int(x) % 2 == 0, 20 - int(x)))))


if __name__ == '__main__':
    s = '1982376455'
    main(s)
    func2(s)
    func3(s)
    a = [1, 9, 8, 2, 3, 7, 6, 4, 5, 5]
    # ret = sorted(a, key=lambda x: x % 2 == 0 and 20 - x or x)
    # ret = sorted(a, key=lambda x: x % 2 == 0)
    # ret = sorted(a, key=lambda x: x)
    ret = sorted(a, key=lambda x: x % 2 == 0 and 20-x or x)
    print(ret)
