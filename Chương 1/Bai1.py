chuoi = input("Nhập chuỗi số cách nhau bởi dấu cách: ")

chuoi_dinh_dang_list = "[" + chuoi.replace(" ", ",") + "]"
ma_tran_1_chieu = eval(chuoi_dinh_dang_list)
tong = sum(ma_tran_1_chieu)

print("Ma trận 1 chiều:", ma_tran_1_chieu)
print("Tổng của dãy số:", tong)