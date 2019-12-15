import string


def get_missing_letter(a):
    letters = string.ascii_lowercase
    s1 = set(letters)
    print(type(letters))
    s2 = set(a)
    # print(s1-s2)
    # print(type(s1-s2))
    print(''.join(sorted(s1-s2)))


if __name__ == '__main__':
    get_missing_letter('python')