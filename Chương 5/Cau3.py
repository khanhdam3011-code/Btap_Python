a = int(input("Nhập số nguyên dương a: "))
b = input("Nhập số nguyên dương b: ")

chu_so_nho_nhat = 9

for chu_so in b:
    so = int(chu_so)
    if so < chu_so_nho_nhat:
        chu_so_nho_nhat = so

if a % chu_so_nho_nhat == 0:
    print(f"--> {a} CHIA HẾT cho chữ số nhỏ nhất của {b} (là {chu_so_nho_nhat}).")
else:
    print(f"--> {a} KHÔNG chia hết cho chữ số nhỏ nhất của {b} (là {chu_so_nho_nhat}).")