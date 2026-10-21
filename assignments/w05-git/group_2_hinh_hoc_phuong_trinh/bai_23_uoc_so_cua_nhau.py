a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

if b != 0 and a % b == 0:
    print(f"{b} là ước của {a}")
else:
    print(f"{b} không là ước của {a}")

if a != 0 and b % a == 0:
    print(f"{a} là ước của {b}")
else:
    print(f"{a} không là ước của {b}")
