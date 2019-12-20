import glob

# ret = glob.glob(r'./*.py')
# print(ret)
# for file in glob.iglob(r"./*.py", recursive=True):
#     print(file)


def func(fp, postfix):
    # pattern = f"{fp}/*{postfix}"
    pattern = "{}/*{}".format(fp, postfix)
    print(pattern)
    for i in glob.iglob(pattern):
        print(i)


if __name__ == '__main__':
    func('.', '.py')

