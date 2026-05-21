chuoi = input("Nhập ma trận (số cách nhau bằng dấu cách, hàng cách nhau bằng dấu ;): ")

chuoi_tuple = "((" + chuoi.replace(" ", ",").replace(";", "),(") + "))"
ma_tran_tuple = eval(chuoi_tuple)

print("Ma trận 4x3 dưới dạng tuple là:")
print(ma_tran_tuple)
