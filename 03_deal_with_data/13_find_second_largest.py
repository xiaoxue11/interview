def find_second_largest(num_list):
    """find the second largest number"""
    one = num_list[0]
    two = num_list[0]
    for i in range(1, len(num_list)):
        if num_list[i] > one:
            two = one
            one = num_list[i]
        elif num_list[i] > two:
            two = num_list[i]
    return two


if __name__ == '__main__':
    num_list = [34, 11, 23, 56, 78, 0, 9, 12, 3, 7, 5]
    ret = find_second_largest(num_list)
    print(ret)