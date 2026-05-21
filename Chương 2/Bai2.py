s = input("Nhập vào một xâu kí tự: ")

chu_thuong = 0
chu_hoa = 0
chu_so = 0
con_lai = 0

for c in s:
    if "a" <= c <= "z":
        chu_thuong += 1
    elif "A" <= c <= "Z":
        chu_hoa += 1
    elif "0" <= c <= "9":
        chu_so += 1
    else:
        con_lai += 1

print("Số kí tự thường:", chu_thuong)
print("Số kí tự hoa:", chu_hoa)
print("Số kí tự số (0-9):", chu_so)
print("Số kí tự còn lại:", con_lai)