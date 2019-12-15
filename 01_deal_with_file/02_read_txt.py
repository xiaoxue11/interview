def get_text_with_read(fp):
    """get file content by read, return str"""
    with open(fp, 'r+') as f:
        content = f.read()
        print(content)
        print(type(content))


def get_line_with_readline(fp):
    """get text content each line by readline, return str"""
    with open(fp, 'r+') as f:
        while True:
            line = f.readline()
            if line:
                print(type(line))
                print(line)
            else:
                break


def get_lines_with_readlines(fp):
    """
    read text context by readlines
    :param fp: file name
    :return: list, each line
    """
    with open(fp, 'r+') as f:
        lines = f.readlines()
        print(type(lines))
        for line in lines:
            print(line)


if __name__ == '__main__':
    get_text_with_read('test.txt')
    print('*'*100)
    get_line_with_readline('test.txt')
    print('*' * 100)
    get_lines_with_readlines('test.txt')
