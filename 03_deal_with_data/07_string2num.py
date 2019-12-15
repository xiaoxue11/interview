from functools import reduce


def string2num(s):
    num = 0
    for char in s:
        for j in range(10):
            if char == str(j):
                num = num*10 + j
    return num


def atoi(s):
    num = 0
    for char in s:
        num = num*10 + ord(char)-ord('0')
    return num


def atoi_simple(s):
    return reduce(lambda num, v: num*10+ord(v)-ord('0'), s, 0)


def atoi_1(s):
    num = 0
    for v in s:
        temp = eval(v)
        num = num*10 + temp
    print(num)


if __name__ == '__main__':
    value = string2num('123')
    print(value)
    print(atoi('4567'))
    print(atoi_simple('7890'))
    atoi_1('1234')
