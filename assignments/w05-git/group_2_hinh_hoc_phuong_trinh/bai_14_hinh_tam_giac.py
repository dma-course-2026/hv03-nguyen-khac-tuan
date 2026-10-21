import math

a, b, c = map(float, input("Nhập 3 cạnh a b c: ").split())

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    chu_vi = a + b + c
    p = chu_vi / 2
    dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Chu vi: {chu_vi:.2f}")
    print(f"Diện tích: {dien_tich:.2f}")
else:
    print("Ba số đã nhập không tạo thành tam giác")
