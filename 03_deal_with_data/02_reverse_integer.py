def reverse_integer(value):
    """一个整数，例如-123 --> -321"""
    flag = 1 if value >= 0 else -1
    str_value = str(abs(value))
    new = str_value[::-1]
    return flag*int(new)


if __name__ == '__main__':
    num = int(input('please input a number: '))
    print(reverse_integer(num))
    a = [1, 2, 3, 5]
    print(a[10:])
