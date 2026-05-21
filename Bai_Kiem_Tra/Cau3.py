n = input("Nhập số nguyên dương n: ")

tich_chu_so = 1

for chu_so in n:
    tich_chu_so *= int(chu_so)

if tich_chu_so % 2 == 0 and tich_chu_so > 20:
    print(f"--> Tích các chữ số là {tich_chu_so}: THỎA MÃN (chẵn và > 20).")
else:
    print(f"--> Tích các chữ số là {tich_chu_so}: KHÔNG thỏa mãn điều kiện.")