n = int(input("nhập n: "))
s = 0
for i in range(1, n + 1):
    s += i
print("tổng từ 1 đến n là:", s)

so_luong = int(input("nhập số lượng phần tử của dãy: "))
tong_day = 0

for i in range(so_luong):
    x = int(input(f"nhập số thứ {i + 1}: "))
    tong_day += x  

print("tổng dãy số là:", tong_day)