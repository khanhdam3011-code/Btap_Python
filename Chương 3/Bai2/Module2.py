import Module1

dai = float(input("Nhập chiều dài HCN: "))
rong = float(input("Nhập chiều rộng HCN: "))
print("--> Diện tích HCN:", Module1.dien_tich_hcn(dai, rong))
print("--> Chu vi HCN:", Module1.chu_vi_hcn(dai, rong))

canh = float(input("Nhập cạnh hình vuông: "))
print("--> Diện tích hình vuông:", Module1.dien_tich_hv(canh))

ban_kinh = float(input("Nhập bán kính hình tròn: "))
print("--> Diện tích hình tròn:", Module1.dien_tich_ht(ban_kinh))