n = int(input("Nhập số lượng phần tử n (0 < n < 100): "))

danh_sach = []

for i in range(n):
    x = float(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach.append(x)

tong = 0
dem = 0

for x in danh_sach:
    if 0 < x < 1000:
        tong += x
        dem += 1

if dem > 0:
    tbc = tong / dem
    print(f"--> Trung bình cộng các số thỏa mãn là: {tbc}")
else:
    print("--> Không có số nào nằm trong khoảng (0, 1000)")