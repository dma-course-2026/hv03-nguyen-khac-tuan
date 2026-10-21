import math

x0, y0 = map(float, input("Nhập tọa độ tâm x0 y0: ").split())
r = float(input("Nhập bán kính R: "))
xa, ya = map(float, input("Nhập tọa độ điểm A xa ya: ").split())

d = math.sqrt((xa - x0) ** 2 + (ya - y0) ** 2)

if abs(d - r) < 1e-9:
    print("Điểm A nằm trên đường tròn")
elif d < r:
    print("Điểm A nằm trong đường tròn")
else:
    print("Điểm A nằm ngoài đường tròn")
