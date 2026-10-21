a, b, c, d, e = map(float, input("Nhập 5 số thực a b c d e: ").split())

min_val = a
if b < min_val:
    min_val = b
if c < min_val:
    min_val = c
if d < min_val:
    min_val = d
if e < min_val:
    min_val = e

print(f"Giá trị nhỏ nhất trong 5 số là: {min_val}")
