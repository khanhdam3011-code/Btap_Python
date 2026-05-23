import baitap

x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

tich = x * y * z
so_chu_so, max_val = baitap.xuly_tich(tich)

print("Tich:", tich)
print("So chu so:", so_chu_so)
print("Chu so lon nhat:", max_val)