# seq에서  알파벳만 저장해서 출력하기
# 4.1
with open("sequence.protein.gp", "r") as handle:
    title = ""
    seq = ""
    cnt = 0
    lines = handle.readline()
    full_lines = handle.readlines()
    title = lines.rstrip()  # title: LOUCAS'
    print(f"title: {title}")  # title: LOUCAS'

##origin이 몇번째 줄인지 count하기
for line in full_lines:
    tmp = line.strip()
    if cnt == 1:
        seq = seq + line
    if tmp.startswith("ORIGIN"):
        cnt = 1

###############
# 2번

a = seq.strip("\n")
alphas = ""
all_alpha = ""

for i in a:
    if i.isalpha():
        all_alpha = i + all_alpha
result_seq = f"seq : {all_alpha}"
print(result_seq)
