tong = 0

while True:
    so = int(input("Nhập số: "))
    if so == 0:
        break
    if so % 2 == 0:
        tong += so

print("Tổng các số chẵn là:", tong)