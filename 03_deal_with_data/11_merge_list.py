def merge_two_lists(a, b):
    temp = []
    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            temp.append(b[0])
            del b[0]
        else:
            temp.append(a[0])
            del a[0]
    while len(a) > 0:
        temp.append(a[0])
        del a[0]
    while len(b) > 0:
        temp.append(b[0])
        del b[0]
    return temp


if __name__ == '__main__':
    l1 = [1, 3, 5, 7, 9]
    l2 = [2, 4, 6, 8]
    l1.extend(l2)
    print(l1)
    ret = merge_two_lists(l1, l2)
    print(ret)
