m = int(input("Nhập M: "))
n = int(input("Nhập N: "))

tong = 0
for i in range(m, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        tong += i

print(f"Kết quả: {tong}")
