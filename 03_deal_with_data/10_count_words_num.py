import re
from collections import Counter


def main(fp):
    text = {}
    with open(fp, 'r+') as f:
        for line in f:
            line = re.sub("\W", " ", line)
            # print(line)
            line_words = line.split()
            # print(line_words)
            for word in line_words:
                text[word] = text.get(word, 0) + 1
    print(text.items())
    num_word = sorted(text.items(), key=lambda x: x[1], reverse=True)[:10]
    words = [word[0] for word in num_word]
    return words


def test(fp):
    with open(fp, "r+") as f:
        return list(map(lambda x: x[0], Counter(re.sub(r'\W', ' ', f.read()).split()).most_common(10)))


if __name__ == '__main__':
    fp = 'test.txt'
    ret = main(fp)
    print(ret)
    s = test(fp)
    print(s)




