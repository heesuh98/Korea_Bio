fr = open(
    "/BiO/Access/home/user31/Korea_Bio/2021-07-09/sequence.protein.2.fasta", "r"
)
title = ""
seq_list = list()
for line in fr:
    line = line.strip()
    if line == "":
        continue
    if line[0] != ">":
        seq_list.append(line)
    else:
        title = line
fr.close()

seq = "".join(seq_list)
while True:
    aa = input("Enter amino acid code:")
    if aa == "XXX":
        print("Okay, I will stop.")
        break
    else:
        found_pos_list = list()
        i = 1
        for c in seq:
            if c == aa:
                found_pos_list.append(str(i))
            i += 1
        print("Found at : %s" % (",".join(found_pos_list)))
