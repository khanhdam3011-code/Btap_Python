a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))

tong = a + b
print(f"--> Tổng (a + b) = {tong}")

chu_so_lon_nhat = -1  

for chu_so in str(tong):
    so = int(chu_so)
    if so > chu_so_lon_nhat:
        chu_so_lon_nhat = so

print(f"--> Chữ số lớn nhất trong tổng là: {chu_so_lon_nhat}")