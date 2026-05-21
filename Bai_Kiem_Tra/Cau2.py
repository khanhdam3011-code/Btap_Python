n = input("Nhập số nguyên dương n: ")

tong_chu_so = 0

for chu_so in n:
    tong_chu_so += int(chu_so)  

if tong_chu_so % 3 == 0:
    print(f"--> Tổng các chữ số là {tong_chu_so}: CHIA HẾT cho 3.")
else:
    print(f"--> Tổng các chữ số là {tong_chu_so}: KHÔNG chia hết cho 3.")