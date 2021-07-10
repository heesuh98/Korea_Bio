# 4.1
with open("sequence.protein.gp", "r") as handle:
    seq = ""
    #seq = []
    cnt = 0
    lines = handle.readline().rstrip()
    full_lines = handle.readlines()
    print(f"title: {lines}")  # title: LOUCAS'

##origin이 몇번째 줄인지 count하기

for line in full_lines:
    tmp = line.strip()
    if cnt == 1:
        seq = seq + line ##seq.append()로 만들어보기! --> list를 이후 join을 하기
    if tmp.startswith("ORIGIN"):
        cnt = 1


print(f"seq : {seq}")
