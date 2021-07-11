seq_list = list()

with open(
    "/BiO/Access/home/user31/Korea_Bio/2021-07-08/sequence.protein.2.fasta", "r"
) as st:

    title = st.readline()
    for line in handle:
        line = line.strip
        if line == "":
            continue
        if line[0] != ">":
            seq_list.append(line)
        else:
            title = line

seq = "".join(seq_list)
while True:
    position = input("Position:")
    aa = title
