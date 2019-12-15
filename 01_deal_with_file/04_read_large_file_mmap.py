import os
from mmap import mmap


# m = mmap(os.open('test.txt', os.O_RDWR), 0)
# print(m.read(20))
# m.close()
# print(m.read(20))


def get_files(fp):
    """
    use mmap method to read file which size over cpu capacity
    :param fp: file name
    :return: read string based on environment
    """
    with open(fp, 'r+') as f:
        m = mmap(f.fileno(), 0)
        temp = 0
        for i, char in enumerate(m):
            if char == b'\n':
                yield m[temp:i+1].decode()
                temp = i+1


if __name__ == '__main__':
    for content in get_files('test.txt'):
        print(content)

