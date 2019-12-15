import os


def get_files(dir, suffix):
    ret = []
    for root, dirs, files in os.walk(dir):
        for filename in files:
            name, suf = os.path.splitext(filename)
            if suf == suffix:
                ret.append(os.path.join(root, filename))
    return ret


if __name__ == '__main__':
    print(get_files('.', '.py'))
    print(get_files('.', '.txt'))