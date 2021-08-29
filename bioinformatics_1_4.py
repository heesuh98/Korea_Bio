a = input("Enter a integer:")
b = input("Enter another: ")
a = int(a)
b = int(b)

if a > b:
    result = f"{a} is greater than {b}."
    print(result)
elif a < b:
    resultb = f"{a} is less than {b}."
    print(resultb)
else:
    resultc = f"{a} is equal to {b}"
    print(resultc)
