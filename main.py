def tinh_tien_ve(tuoi: int, so_luong: int):
    # Ràng buộc kiểu dữ liệu
    if not isinstance(tuoi, int) or isinstance(tuoi, bool):
        return "INVALID"
    if not isinstance(so_luong, int) or isinstance(so_luong, bool):
        return "INVALID"

    # Kiểm tra miền giá trị hợp lệ bằng toán tử 'and'
    if (1 <= tuoi <= 100) and (1 <= so_luong <= 10):
        # Phân loại độ tuổi
        if 1 <= tuoi <= 17:
            return "Không đủ tuổi"
        elif 18 <= tuoi <= 22:
            return 50000 * so_luong
        else:
            return 80000 * so_luong
    else:
        return "INVALID"


def tinh_cuoc_ship(khoi_luong: float, khoang_cach: float):
    # Ràng buộc kiểu dữ liệu
    if not isinstance(khoi_luong, (int, float)) or isinstance(khoi_luong, bool):
        return "INVALID"
    if not isinstance(khoang_cach, (int, float)) or isinstance(khoang_cach, bool):
        return "INVALID"

    kl = round(float(khoi_luong), 4)
    kc = round(float(khoang_cach), 4)

    # Kiểm tra miền giá trị hợp lệ bằng toán tử 'and'
    if (0.1 <= kl <= 30.0) and (1.0 <= kc <= 50.0):
        # Tính cước
        if kl <= 5.0:
            return round(5000.0 * kc, 2)
        else:
            return round(7000.0 * kc, 2)
    else:
        return "INVALID"