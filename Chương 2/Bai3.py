toan = float(input("Nhập điểm Toán: "))
ly = float(input("Nhập điểm Lý: "))
hoa = float(input("Nhập điểm Hóa: "))

dtb = (toan + ly + hoa) / 3

print("Điểm trung bình:", dtb)

if dtb < 5:
    print("Xếp loại: Yếu")
elif dtb < 6.5:
    print("Xếp loại: Trung bình")
elif dtb < 8:
    print("Xếp loại: Khá")
else:
    print("Xếp loại: Giỏi")