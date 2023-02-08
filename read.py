import time
import progressbar
bar = progressbar.ProgressBar(max_value=1000000)
data = []
count = 0
with open('reviews.txt', 'r')as f:
    for lines in f:
        count += 1
        data.append(lines.strip())
        bar.update(count)
        # print(len(data))

wc = {}
for lines in data:
    word = lines.split()
    for word in word:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1

while True:
    user = input(' type ')
    if user == 'q':
        break
    if user in wc:
        print(user, wc[user])
    else:
        print('not available')
