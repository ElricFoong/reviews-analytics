data = []
count = 0

with open("reviews.txt", "r") as f:
    for line in f:
        count += 1
        data.append(line)
        if count % 1000 == 0:
            print(len(data))
sum_len = 0
for d in data:
    sum_len += len(d)
print("average comment of length are ", sum_len/len(data))
