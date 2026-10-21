a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

if a > 0:
    print(f"Bất phương trình có nghiệm: x >= {-b / a}")
elif a < 0:
    print(f"Bất phương trình có nghiệm: x <= {-b / a}")
else:
    if b >= 0:
        print("Bất phương trình đúng với mọi x")
    else:
        print("Bất phương trình vô nghiệm")
