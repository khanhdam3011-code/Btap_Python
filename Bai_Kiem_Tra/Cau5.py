m = int(input("Nhập số nguyên dương m: "))
n = input("Nhập số nguyên dương n: ")

tong_n = 0
for chu_so in n:
    tong_n += int(chu_so)

if m % tong_n == 0:
    print(f"--> {m} CHIA HẾT cho tổng các chữ số của {n} (là {tong_n}).")
else:
    print(f"--> {m} KHÔNG chia hết cho tổng các chữ số của {n} (là {tong_n}).")