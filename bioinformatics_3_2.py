with open("title.txt", "r") as fr:
    for line in fr:
        line = line.strip()
        break
print("The first line is: %s" % (line))
