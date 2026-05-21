n = int(input("Nhập số lượng phần tử n: "))

danh_sach = []

for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach.append(x)

tong_chan = 0

for x in danh_sach:
    if x % 2 == 0:
        tong_chan += x

print(f"--> Tổng các phần tử chẵn trong dãy là: {tong_chan}")

if tong_chan % 7 == 0 and tong_chan < 200:
    print("--> Thỏa mãn: Tổng này chia hết cho 7 và nhỏ hơn 200.")
else:
    print("--> Không thỏa mãn điều kiện (phải vừa chia hết cho 7 vừa nhỏ hơn 200).")