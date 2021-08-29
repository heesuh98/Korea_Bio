num = input("Which times table: ")
num = int(num)
if not 1 < num < 9:
    print("What?")
else:
    for i in range(1, 10):
        gugu = i * num
        print(f"{num} * {i} = {gugu}")
