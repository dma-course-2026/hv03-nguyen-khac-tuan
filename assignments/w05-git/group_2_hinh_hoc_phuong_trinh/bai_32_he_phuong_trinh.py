a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
m = float(input("Nhập m: "))
c = float(input("Nhập c: "))
d = float(input("Nhập d: "))
n = float(input("Nhập n: "))

D = a * d - b * c
Dx = m * d - b * n
Dy = a * n - m * c

if D != 0:
    x = Dx / D
    y = Dy / D
    print(f"Hệ có nghiệm duy nhất: x = {x:.3f}, y = {y:.3f}")
elif Dx == 0 and Dy == 0:
    print("Hệ có vô số nghiệm")
else:
    print("Hệ vô nghiệm")
