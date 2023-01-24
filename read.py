data = []
counter = 0
with open("reviews.txt", "r")as f:
    for line in f:
        counter += 1
        data.append(line)
        if counter % 1000 == 0:

            print(len(data))
