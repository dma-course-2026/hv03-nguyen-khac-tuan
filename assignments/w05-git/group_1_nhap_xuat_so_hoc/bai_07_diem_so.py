a, b, c = map(float, input("Nhập 3 điểm: ").split())

dtb = (a + b + c) / 3

print(f"Điểm trung bình là: {dtb:.1f}")
if dtb >= 5.0:
    print("Đậu")
else:
    print("Rớt")
