def get_lines(fp, read_size):
    """read specific size content from file"""
    with open(fp, 'r+') as f:
        while True:
            content = f.read(read_size)
            if not content:
                break
            yield content


def get_large_file_content(fp):
    """
    read file size over cpu capacity
    :param fp: file name
    :return: get a generator by yield
    """
    with open(fp, 'r+') as f:
        for i in f:
            # print(type(i))
            # print(i)
            yield i


if __name__ == '__main__':
    # ret = get_lines('test.txt', 200)
    # print(type(ret))
    # for text in ret:
    #     print(text)
    ret = get_large_file_content('test.txt')
    print(type(ret))
    # for i in ret:
    #     print(i)
