a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
d = int(input("Nhập d: "))

max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
if d > max_val:
    max_val = d

print(f"Giá trị lớn nhất trong 4 số là: {max_val}")
