cnt = 0
l_seq = []
with open("sequence.nucleotide.gb", "r") as handle:
    data = handle.readlines()
    for line in data:
        cnt += 1 #enumerate쓰기
        if "/translation" in line:
            start = cnt
            break

for i in range(len(data)):
    if i >= start - 1:
        if "                     " in data[i]:
            l_seq.append(data[i].strip())
        if "exon" in data[i]:
            break
import re

s = ""
for i in l_seq:
    l_seq = re.findall("[A-Z]", i)
    seq = "".join(l_seq)
    s += seq
print(s + "*")  # 종결코돈 추가
