def read_file(filename):
    count = 0
    data = []
    with open(filename, "r", encoding='utf-8')as f:
        for line in f:
            count += 1
            data.append(line.strip())
    return data

# 文字计数


def dic(data):
    wc = {}
    for lines in data:
        words = lines.split()
        for word in words:
            if word in wc:
                wc[word] += 1
            else:
                wc[word] = 1  # 新增新的key进wc字典

    return wc


def word_check(data):
    for word in data:
        if data[word] > 100000:
            print(word, data[word])


def word_check2(data):
    while True:
        name = input('请输入想要查的字: ')
        if name == 'q':
            break

        if name in data:
            print(name, data[name])
        else:
            print('你所打的字并不存在 ')

    print('感谢使用查询功能. ')


def main():
    filename = 'reviews.txt'
    data = read_file(filename)
    data = dic(data)
    word_check(data)
    word_check2(data)


main()
