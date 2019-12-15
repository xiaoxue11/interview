import os


def print_directory_contents(s_path):
    """
    这个函数接收文件夹的名称作为输入参数
    返回该文件夹中文件的路径
    以及其包含文件夹中文件的路径
    """
    # print(os.listdir(s_path))
    for s_child in os.listdir(s_path):
        # print(s_child)
        s_child_path = os.path.join(s_path, s_child)
        # print(s_child_path)
        if os.path.isdir(s_child_path):
            print_directory_contents(s_child_path)
        else:
            print(s_child_path)


if __name__ == '__main__':
    print(os.name)
    print(os.uname())
    print(os.environ)
    print(os.path.abspath('.'))
    print(os.listdir('.'))
    print(os.path.join(os.path.abspath('.'), 'testdir'))
    print(os.path.split('/Users/michael/testdir/file.txt'))
    print(os.path.splitext('/Users/michael/testdir/file.txt'))
    print_directory_contents('/home/xue/Documents/python_basic/interview')
