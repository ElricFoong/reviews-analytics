data = []
count = 0

with open("reviews.txt", "r") as f:
    for line in f:
        count += 1
        data.append(line)
        if count % 1000 == 0:
            print(len(data))
new = []
for d in data:
    if len(d) < 80:
        new.append(d)
print("Comment less than 100 words are total ",len(new))