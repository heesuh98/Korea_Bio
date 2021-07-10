# seq에서  알파벳만 저장해서 출력하기
# 4.1
with open(
    "/BiO/Access/home/user31/Korea_Bio/2021-07-09/sequence.protein.gp", "r"
) as handle:
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

a = seq.strip("\n")
alphas = ""
all_alpha = ""

for i in a:
    if i.isalpha() == True:
        alphas = i
        all_alpha = alphas + all_alpha
result_seq = f"seq : {all_alpha}"
# print(result_seq)

##########
# 3번
count = 0
for i in result_seq:
    print(i, end="")
    count += 1
    if count == 70:
        print("")
        count = 0
