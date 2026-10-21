PI = 3.14

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))

s1 = a * b
s2 = PI * (a / 2) ** 2

print(f"Diện tích còn lại: {s1 - s2:.2f}")
