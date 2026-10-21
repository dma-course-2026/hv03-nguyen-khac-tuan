a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    if a == b or b == c or a == c:
        print("Là tam giác cân")
    else:
        print("Không phải tam giác cân")
else:
    print("Ba cạnh không tạo thành tam giác")
