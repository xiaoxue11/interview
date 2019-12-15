def two_sum(nums, target):
    d ={}
    for i, value in enumerate(nums):
        if value in d:
            return [d[value], i]
        d[target-value] = i


if __name__ == '__main__':
    array = [2, 7, 11, 15]
    target = 9
    ret = two_sum(array, target)
    print(ret)