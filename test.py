# chay_kiem_thu.py
from main import tinh_tien_ve, tinh_cuoc_ship

# Bộ test case Robust BVA cho Bài 1 (Vé xem phim)
test_ve_phim = [
    ("TC01", 0, 5, "INVALID"),
    ("TC02", 1, 5, "Không đủ tuổi"),
    ("TC03", 2, 5, "Không đủ tuổi"),
    ("TC04", 17, 5, "Không đủ tuổi"),
    ("TC05", 18, 5, 250000),
    ("TC06", 19, 5, 250000),
    ("TC07", 21, 5, 250000),
    ("TC08", 22, 5, 250000),
    ("TC09", 23, 5, 400000),
    ("TC10", 99, 5, 400000),
    ("TC11", 100, 5, 400000),
    ("TC12", 101, 5, "INVALID"),
    ("TC13", 50, 0, "INVALID"),
    ("TC14", 50, 1, 80000),
    ("TC15", 50, 2, 160000),
    ("TC16", 50, 9, 720000),
    ("TC17", 50, 10, 800000),
    ("TC18", 50, 11, "INVALID"),
    ("TC19", 50, 5, 400000),
]

# Bộ test case Robust BVA cho Bài 2 (Phí ship)
test_cuoc_ship = [
    ("TC01", 0.0, 25.0, "INVALID"),
    ("TC02", 0.1, 25.0, 125000.0),
    ("TC03", 0.2, 25.0, 125000.0),
    ("TC04", 4.9, 25.0, 125000.0),
    ("TC05", 5.0, 25.0, 125000.0),
    ("TC06", 5.1, 25.0, 175000.0),
    ("TC07", 29.9, 25.0, 175000.0),
    ("TC08", 30.0, 25.0, 175000.0),
    ("TC09", 30.1, 25.0, "INVALID"),
    ("TC10", 15.0, 0.9, "INVALID"),
    ("TC11", 15.0, 1.0, 7000.0),
    ("TC12", 15.0, 1.1, 7700.0),
    ("TC13", 15.0, 49.9, 349300.0),
    ("TC14", 15.0, 50.0, 350000.0),
    ("TC15", 15.0, 50.1, "INVALID"),
    ("TC16", 15.0, 25.0, 175000.0),
]

def kiem_tra():
    print("=" * 60)
    print("BẮT ĐẦU CHẠY BỘ KIỂM THỬ")
    print("=" * 60)
    
    so_loi_phat_hien = 0

    # Chạy kiểm thử bài 1
    print("\nKIỂM THỬ BÀI 1: TÍNH TIỀN VÉ")
    for ma_tc, tuoi, sl, mong_doi in test_ve_phim:
        thuc_te = tinh_tien_ve(tuoi, sl)
        if thuc_te != mong_doi:
            so_loi_phat_hien += 1
            print(f"[CẢNH BÁO LỖI] {ma_tc} Thất bại! Đầu vào: (tuổi={tuoi}, sl={sl}) | Thực tế: {thuc_te} != Kỳ vọng: {mong_doi}")

    # Chạy kiểm thử bài 2
    print("\nKIỂM THỬ BÀI 2: TÍNH PHÍ SHIP")
    for ma_tc, kl, kc, mong_doi in test_cuoc_ship:
        thuc_te = tinh_cuoc_ship(kl, kc)
        if thuc_te != mong_doi:
            so_loi_phat_hien += 1
            print(f"[CẢNH BÁO LỖI] {ma_tc} Thất bại! Đầu vào: (khối lượng={kl}, khoảng cách={kc}) | Thực tế: {thuc_te} != Kỳ vọng: {mong_doi}")

    print("\n" + "=" * 60)
    if so_loi_phat_hien == 0:
        print("KẾT QUẢ: 100% TEST CASE PASS (Code hiện tại không bị phát hiện lỗi).")
    else:
        print(f"KẾT QUẢ: BỘ TEST ĐÃ BẮT ĐƯỢC {so_loi_phat_hien} ĐIỂM BẤT THƯỜNG (Mutant bị tiêu diệt)!")
    print("=" * 60)

if __name__ == "__main__":
    kiem_tra()