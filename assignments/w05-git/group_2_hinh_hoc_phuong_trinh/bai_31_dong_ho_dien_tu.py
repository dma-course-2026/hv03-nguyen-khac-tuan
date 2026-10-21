h, p, s = map(int, input("Nhập h p s: ").split())

s += 1
if s == 60:
    s = 0
    p += 1
    if p == 60:
        p = 0
        h += 1
        if h == 24:
            h = 0

print(h, p, s)
