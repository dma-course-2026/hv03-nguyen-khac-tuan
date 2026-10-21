n = int(input("Nhập số có 3 chữ số: "))

if 100 <= n <= 999:
    tram = n // 100
    chuc = (n % 100) // 10
    don_vi = n % 10
    print(f"Hàng trăm = {tram}")
    print(f"Hàng chục = {chuc}")
    print(f"Hàng đơn vị = {don_vi}")
else:
    print("Số vừa nhập không phải số có 3 chữ số")
