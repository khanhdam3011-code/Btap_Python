import baitap

n = int(input("n = "))
a = [int(input(f"x[{i+1}] = ")) for i in range(n)]

tong = 0
for x in a:
    if baitap.check_snt(x):
        tong += x

print("Tong SNT:", tong)
if tong % 2 != 0 and tong > 50:
    print("Thoa man")
else:
    print("Khong thoa man")