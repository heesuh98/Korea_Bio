seq_list = []
fr = open("sequence.nucleotide.fasta", "r")
for line in fr:
    if line[0] != ">":
        line = line.strip()
        seq_list.append(line)
fr.close()
seq = "".join(seq_list)

aa = []
for a in seq:
    aa.append(a)
    if len(aa) % 3 == 0:
        print("".join(aa))
        aa = []
