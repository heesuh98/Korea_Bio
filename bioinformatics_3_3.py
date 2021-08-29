fr = open("sequence.protein.fasta", "r")  # 공백이있는 파일이 아니다
for line in fr:
    line = line.strip()
    if line == "":
        continue
    print(line)
fr.close()
