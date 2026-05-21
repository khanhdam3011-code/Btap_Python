chuoi = input("Nhập chuỗi số cách nhau bởi dấu cách: ")

danh_sach_tam = chuoi.split()
ma_tran_1_chieu = []

for x in danh_sach_tam:
    ma_tran_1_chieu.append(int(x))

print(ma_tran_1_chieu)