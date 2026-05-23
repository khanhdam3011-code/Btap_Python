a = int(input("nhập a: "))
b = int(input("nhập b: "))
c = int(input("nhập c: "))

lon_nhat = a

if b > lon_nhat:
    lon_nhat = b

if c > lon_nhat:
    lon_nhat = c

print("số lớn nhất là:", lon_nhat)