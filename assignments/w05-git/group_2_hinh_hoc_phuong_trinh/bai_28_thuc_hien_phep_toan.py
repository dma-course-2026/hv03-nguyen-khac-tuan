a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
op = input("Nhập phép toán (+, -, *, /): ").strip()

if op == "+":
    print(f"{a} + {b} = {a + b}")
elif op == "-":
    print(f"{a} - {b} = {a - b}")
elif op == "*":
    print(f"{a} * {b} = {a * b}")
elif op == "/":
    if b == 0:
        print("Lỗi: không thể chia cho 0")
    else:
        print(f"{a} / {b} = {a / b}")
else:
    print("Phép toán không hợp lệ")
