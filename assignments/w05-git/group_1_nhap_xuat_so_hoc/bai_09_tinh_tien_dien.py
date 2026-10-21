ho_ten = input("Nhập họ tên chủ hộ: ")
chi_so_cu, chi_so_moi = map(int, input("Nhập chỉ số tháng trước và tháng này: ").split())

so_kw = chi_so_moi - chi_so_cu

if so_kw < 0:
    print("Chỉ số tháng này phải lớn hơn hoặc bằng tháng trước")
else:
    if so_kw <= 60:
        tien = so_kw * 5
    elif so_kw <= 160:
        tien = 60 * 5 + (so_kw - 60) * 8
    else:
        tien = 60 * 5 + 100 * 8 + (so_kw - 160) * 10

    print(f"Chủ hộ: {ho_ten}")
    print(f"Lượng điện tiêu thụ: {so_kw} kW")
    print(f"Số tiền phải trả là: {tien:.2f}")
