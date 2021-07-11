seq_list = list()

with open(
    "/BiO/Access/home/user31/Korea_Bio/2021-07-08/sequence.protein.2.fasta", "r"
) as st:

    title = st.readline()
    for i in st:
        i = i.strip()
        if i == "":
            continue
        if i[0] != ">":
            seq_list.append(i)
        else:
            title = i
    seq = "".join(seq_list)
print(f"title:{title}")
print(f"seq:{seq}")
