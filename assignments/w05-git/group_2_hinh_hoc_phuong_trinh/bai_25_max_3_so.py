a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c

print(f"Giá trị lớn nhất trong 3 số là: {max_val}")
