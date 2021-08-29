# 읽고 다른 파일에 write하라
fr = open("sequence.protein.fasta", "r")
seq_list = list()
for line in fr:
    line = line.strip()
    if line == "":
        continue
    seq_list.append(line)
fr.close()

seq = "\n".join(seq_list)
fw = open("sequence.protein.2.fasta", "w")
fw.write("%s\n" % (seq))
fw.close()
