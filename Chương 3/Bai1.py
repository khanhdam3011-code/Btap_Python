def tinh_giai_thua(n):
    giai_thua = 1
    for i in range(1, n + 1):
        giai_thua *= i
    return giai_thua


n = int(input("Nhập một số nguyên dương n: "))

if n < 0:
    print("Không tính được giai thừa của số âm.")
else:
    ket_qua = tinh_giai_thua(n)
    print(f"--> Giai thừa của {n} là: {ket_qua}")