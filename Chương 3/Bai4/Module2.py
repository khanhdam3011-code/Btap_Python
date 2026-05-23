import Module1  

def hien_thi(phep_tinh, ket_qua):
    if type(ket_qua) == str:
        print(f"Kết quả phép {phep_tinh}: {ket_qua}")
    else:
        print(f"Kết quả phép {phep_tinh} là: {ket_qua:.2f}")

x = int(input("Nhập số thứ nhất: "))
y = int(input("Nhập số thứ hai: "))

hien_thi("cộng", Module1.tong(x, y))
hien_thi("trừ", Module1.tru(x, y))
hien_thi("nhân", Module1.nhan(x, y))
hien_thi("chia", Module1.chia(x, y))