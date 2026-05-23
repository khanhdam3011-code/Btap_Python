n = int(input("nhập n: "))
a = int(input("nhập a: "))
b = int(input("nhập b: "))

if n % 2 == 0:
    print(f"{n} là số chẵn")
else:
    print(f"{n} là số lẻ")

if a == 0:
    if b == 0:
        print("phương trình vô số nghiệm")
    else:
        print("phương trình vô nghiệm")
else:
    x = -b / a
    print(f"phương trình có nghiệm x = {x:.2f}")