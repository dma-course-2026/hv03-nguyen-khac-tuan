a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    x, y, z = sorted([a, b, c])
    if abs(x ** 2 + y ** 2 - z ** 2) < 1e-9:
        print("Là tam giác vuông")
    else:
        print("Không phải tam giác vuông")
else:
    print("Ba cạnh không tạo thành tam giác")
