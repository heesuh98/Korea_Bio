from os import linesep


fr = open(
    "/BiO/Access/home/user31/Korea_Bio/2021-07-08/sequence.protein.2.fasta", "r"
)
line_count = 0

for line in fr:
    line = line.strip()
    if line_count == 1:
        break
    line_count += 1
fr.close()

print(f"The second line is: {line}")
