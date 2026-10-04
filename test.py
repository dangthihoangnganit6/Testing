import re
from main import calculate_movie_ticket, calculate_shipping_fee

def normalize_output(text):
    """
    Chuẩn hóa kết quả đầu ra:
    Nếu output có dạng 'tổng tiền = [công thức] = [số tiền] ...',
    chuyển về dạng gọn 'tổng tiền = [số tiền] ...' để so sánh chính xác với kết quả hàm.
    """
    match = re.search(r"tổng tiền\s*=\s*.*?=\s*(\d+)(.*)", text)
    if match:
        amount = match.group(1)
        suffix = match.group(2).strip()
        if suffix:
            return f"tổng tiền = {amount} {suffix}"
        return f"tổng tiền = {amount}"
    return text.strip()


# ==============================================================================
# PHẦN 1: BÀI TOÁN 1 - HỆ THỐNG ĐẶT VÉ XEM PHIM
# ==============================================================================

# 1.1. Test cases Phân hoạch tương đương (EP)
ep_test_cases_bai1 = [
    {"id": "EP_TC1", "class": "O1", "inputs": (-5, 5, 2), "expected": "INVALID"},
    {"id": "EP_TC2", "class": "O2", "inputs": (9, 5, 2), "expected": "Không đủ tuổi"},
    {"id": "EP_TC3", "class": "O3", "inputs": (20, 2, 2), "expected": "tổng tiền = 2 x (50000 + 2 x 10000) = 140000"},
    {"id": "EP_TC4", "class": "O4", "inputs": (20, 5, 2), "expected": "tổng tiền = 5 x (50000 + 2 x 10000) = 350000 và thông báo tặng bắp"},
    {"id": "EP_TC5", "class": "O5", "inputs": (20, 9, 2), "expected": "tổng tiền = 9 x (50000 + 2 x 10000) = 630000 và thông báo tặng combo"},
    {"id": "EP_TC6", "class": "O6", "inputs": (61, 2, 2), "expected": "tổng tiền = 2 x (80000 + 2 x 10000) = 200000"},
    {"id": "EP_TC7", "class": "O7", "inputs": (61, 5, 2), "expected": "tổng tiền = 5 x (80000 + 2 x 10000) = 500000 và thông báo tặng bắp"},
    {"id": "EP_TC8", "class": "O8", "inputs": (61, 9, 2), "expected": "tổng tiền = 9 x (80000 + 2 x 10000) = 900000 và thông báo tặng combo"},
]

bqd_test_cases_bai1 = [
    {"id": "bqd_TC1", "class": "O1", "inputs": (-5, 5, 2), "expected": "INVALID"},
    {"id": "bqd_TC1", "class": "O2", "inputs": (50, 15, 2), "expected": "INVALID"},
    {"id": "bqd_TC1", "class": "O3", "inputs": (50, 5, 4), "expected": "INVALID"},
    {"id": "bqd_TC2", "class": "O4", "inputs": (9, 5, 2), "expected": "Không đủ tuổi"},
    {"id": "bqd_TC3", "class": "O5", "inputs": (20, 2, 2), "expected": "tổng tiền = 2 x (50000 + 2 x 10000) = 140000"},
    {"id": "bqd_TC4", "class": "O6", "inputs": (20, 5, 2), "expected": "tổng tiền = 5 x (50000 + 2 x 10000) = 350000 và thông báo tặng bắp"},
    {"id": "bqd_TC5", "class": "O7", "inputs": (20, 9, 2), "expected": "tổng tiền = 9 x (50000 + 2 x 10000) = 630000 và thông báo tặng combo"},
    {"id": "bqd_TC6", "class": "O8", "inputs": (61, 2, 2), "expected": "tổng tiền = 2 x (80000 + 2 x 10000) = 200000"},
    {"id": "bqd_TC7", "class": "O9", "inputs": (61, 5, 2), "expected": "tổng tiền = 5 x (80000 + 2 x 10000) = 500000 và thông báo tặng bắp"},
    {"id": "bqd_TC8", "class": "10", "inputs": (61, 9, 2), "expected": "tổng tiền = 9 x (80000 + 2 x 10000) = 900000 và thông báo tặng combo"},
]

# 1.2. Test cases Kiểm thử giá trị biên (BVA)
bva_test_cases_bai1 = [
    {"id": "BVA_TC1", "inputs": (0, 5, 2), "expected": "INVALID"},
    {"id": "BVA_TC2", "inputs": (1, 5, 2), "expected": "Không đủ tuổi"},
    {"id": "BVA_TC3", "inputs": (2, 5, 2), "expected": "Không đủ tuổi"},
    {"id": "BVA_TC4", "inputs": (17, 5, 2), "expected": "Không đủ tuổi"},
    {"id": "BVA_TC5", "inputs": (18, 5, 2), "expected": "tổng tiền = 5 x (50000 + 2 x 10000) = 350000 và thông báo tặng bắp"},
    {"id": "BVA_TC6", "inputs": (19, 5, 2), "expected": "tổng tiền = 5 x (50000 + 2 x 10000) = 350000 và thông báo tặng bắp"},
    {"id": "BVA_TC7", "inputs": (21, 5, 2), "expected": "tổng tiền = 5 x (50000 + 2 x 10000) = 350000 và thông báo tặng bắp"},
    {"id": "BVA_TC8", "inputs": (22, 5, 2), "expected": "tổng tiền = 5 x (50000 + 2 x 10000) = 350000 và thông báo tặng bắp"},
    {"id": "BVA_TC9", "inputs": (23, 5, 2), "expected": "tổng tiền = 5 x (80000 + 2 x 10000) = 500000 và thông báo tặng bắp"},
    {"id": "BVA_TC10", "inputs": (99, 5, 2), "expected": "tổng tiền = 5 x (80000 + 2 x 10000) = 500000 và thông báo tặng bắp"},
    {"id": "BVA_TC11", "inputs": (100, 5, 2), "expected": "tổng tiền = 5 x (80000 + 2 x 10000) = 500000 và thông báo tặng bắp"},
    {"id": "BVA_TC12", "inputs": (101, 5, 2), "expected": "INVALID"},
    {"id": "BVA_TC13", "inputs": (50, 0, 2), "expected": "INVALID"},
    {"id": "BVA_TC14", "inputs": (50, 1, 2), "expected": "tổng tiền = 1 x (80000 + 2 x 10000) = 100000"},
    {"id": "BVA_TC15", "inputs": (50, 2, 2), "expected": "tổng tiền = 2 x (80000 + 2 x 10000) = 200000"},
    {"id": "BVA_TC16", "inputs": (50, 3, 2), "expected": "tổng tiền = 3 x (80000 + 2 x 10000) = 300000"},
    {"id": "BVA_TC17", "inputs": (50, 4, 2), "expected": "tổng tiền = 4 x (80000 + 2 x 10000) = 400000 và thông báo tặng bắp"},
    {"id": "BVA_TC18", "inputs": (50, 6, 2), "expected": "tổng tiền = 6 x (80000 + 2 x 10000) = 600000 và thông báo tặng bắp"},
    {"id": "BVA_TC19", "inputs": (50, 7, 2), "expected": "tổng tiền = 7 x (80000 + 2 x 10000) = 700000 và thông báo tặng bắp"},
    {"id": "BVA_TC20", "inputs": (50, 8, 2), "expected": "tổng tiền = 8 x (80000 + 2 x 10000) = 800000 và thông báo tặng combo"},
    {"id": "BVA_TC21", "inputs": (50, 9, 2), "expected": "tổng tiền = 9 x (80000 + 2 x 10000) = 900000 và thông báo tặng combo"},
    {"id": "BVA_TC22", "inputs": (50, 10, 2), "expected": "tổng tiền = 10 x (80000 + 2 x 10000) = 1000000 và thông báo tặng combo"},
    {"id": "BVA_TC23", "inputs": (50, 11, 2), "expected": "INVALID"},
    {"id": "BVA_TC24", "inputs": (50, 5, 0), "expected": "INVALID"},
    {"id": "BVA_TC25", "inputs": (50, 5, 1), "expected": "tổng tiền = 5 x (80000 + 1 x 10000) = 450000 và thông báo tặng bắp"},
    {"id": "BVA_TC26", "inputs": (50, 5, 2), "expected": "tổng tiền = 5 x (80000 + 2 x 10000) = 500000 và thông báo tặng bắp"},
    {"id": "BVA_TC27", "inputs": (50, 5, 3), "expected": "tổng tiền = 5 x (80000 + 3 x 10000) = 550000 và thông báo tặng bắp"},
    {"id": "BVA_TC28", "inputs": (50, 5, 4), "expected": "INVALID"},
    {"id": "BVA_TC29", "inputs": (50, 5, 2), "expected": "tổng tiền = 5 x (80000 + 2 x 10000) = 500000 và thông báo tặng bắp"}
]


# ==============================================================================
# PHẦN 2: BÀI TOÁN 2 - HỆ THỐNG TÍNH CƯỚC VẬN CHUYỂN HÀNG
# ==============================================================================

# 2.1. Test cases Phân hoạch tương đương (EP)
ep_test_cases_bai2 = [
    {"id": "EP_TC1", "class": "O1", "inputs": (-2.0, 25.5, 2, 50), "expected": "INVALID"},
    {"id": "EP_TC2", "class": "O2", "inputs": (40.0, 25.5, 2, 50), "expected": "Quá tải trọng"},
    {"id": "EP_TC3", "class": "O3", "inputs": (2.5, 10.5, 2, 50), "expected": "tổng tiền = 10.5 x (5000 + 2 x 2000) + 50 x 10000 = 594500"},
    {"id": "EP_TC4", "class": "O4", "inputs": (2.5, 35.0, 2, 50), "expected": "tổng tiền = 35.0 x (5000 + 2 x 2000) + 50 x 10000 - 20000 = 795000"},
    {"id": "EP_TC5", "class": "O5", "inputs": (17.5, 10.5, 2, 50), "expected": "tổng tiền = 10.5 x (7000 + 2 x 2000) + 50 x 10000 = 615500"},
    {"id": "EP_TC6", "class": "O6", "inputs": (17.5, 35.0, 2, 50), "expected": "tổng tiền = 35.0 x (7000 + 2 x 2000) + 50 x 10000 - 20000 = 865000"},
]

bqd_test_cases_bai2 = [
    {"id": "EP_TC1", "class": "O1", "inputs": (-2.0, 25.5, 2, 50), "expected": "INVALID"},
    {"id": "EP_TC1", "class": "O2", "inputs": (25.5, 60.0, 2, 50), "expected": "INVALID"},
    {"id": "EP_TC1", "class": "O3", "inputs": (25.5, 25.5, 5, 50), "expected": "INVALID"},
    {"id": "EP_TC1", "class": "O4", "inputs": (25.5, 25.5, 2, 110), "expected": "INVALID"},
    {"id": "EP_TC2", "class": "O5", "inputs": (40.0, 25.5, 2, 50), "expected": "Quá tải trọng"},
    {"id": "EP_TC3", "class": "O6", "inputs": (2.5, 10.5, 2, 50), "expected": "tổng tiền = 10.5 x (5000 + 2 x 2000) + 50 x 10000 = 594500"},
    {"id": "EP_TC4", "class": "O7", "inputs": (2.5, 35.0, 2, 50), "expected": "tổng tiền = 35.0 x (5000 + 2 x 2000) + 50 x 10000 - 20000 = 795000"},
    {"id": "EP_TC5", "class": "O8", "inputs": (17.5, 10.5, 2, 50), "expected": "tổng tiền = 10.5 x (7000 + 2 x 2000) + 50 x 10000 = 615500"},
    {"id": "EP_TC6", "class": "O9", "inputs": (17.5, 35.0, 2, 50), "expected": "tổng tiền = 35.0 x (7000 + 2 x 2000) + 50 x 10000 - 20000 = 865000"},
]

# 2.3. Test cases Kiểm thử giá trị biên (BVA)
bva_test_cases_bai2 = [
    {"id": "BVA_TC1", "inputs": (0.0, 25.5, 2, 50), "expected": "INVALID"},
    {"id": "BVA_TC2", "inputs": (0.1, 25.5, 2, 50), "expected": "tổng tiền = 25.5 x (5000 + 2 x 2000) + 50 x 10000 - 20000 = 709500"},
    {"id": "BVA_TC3", "inputs": (0.2, 25.5, 2, 50), "expected": "tổng tiền = 25.5 x (5000 + 2 x 2000) + 50 x 10000 - 20000 = 709500"},
    {"id": "BVA_TC4", "inputs": (4.9, 25.5, 2, 50), "expected": "tổng tiền = 25.5 x (5000 + 2 x 2000) + 50 x 10000 - 20000 = 709500"},
    {"id": "BVA_TC5", "inputs": (5.0, 25.5, 2, 50), "expected": "tổng tiền = 25.5 x (5000 + 2 x 2000) + 50 x 10000 - 20000 = 709500"},
    {"id": "BVA_TC6", "inputs": (5.1, 25.5, 2, 50), "expected": "tổng tiền = 25.5 x (7000 + 2 x 2000) + 50 x 10000 - 20000 = 760500"},
    {"id": "BVA_TC7", "inputs": (29.9, 25.5, 2, 50), "expected": "tổng tiền = 25.5 x (7000 + 2 x 2000) + 50 x 10000 - 20000 = 760500"},
    {"id": "BVA_TC8", "inputs": (30.0, 25.5, 2, 50), "expected": "tổng tiền = 25.5 x (7000 + 2 x 2000) + 50 x 10000 - 20000 = 760500"},
    {"id": "BVA_TC9", "inputs": (30.1, 25.5, 2, 50), "expected": "Quá tải trọng"},
    {"id": "BVA_TC10", "inputs": (49.9, 25.5, 2, 50), "expected": "Quá tải trọng"},
    {"id": "BVA_TC11", "inputs": (50.0, 25.5, 2, 50), "expected": "Quá tải trọng"},
    {"id": "BVA_TC12", "inputs": (50.1, 25.5, 2, 50), "expected": "INVALID"},
    {"id": "BVA_TC13", "inputs": (25.0, 0.9, 2, 50), "expected": "INVALID"},
    {"id": "BVA_TC14", "inputs": (25.0, 1.0, 2, 50), "expected": "tổng tiền = 1.0 x (7000 + 2 x 2000) + 50 x 10000 = 511000"},
    {"id": "BVA_TC15", "inputs": (25.0, 1.1, 2, 50), "expected": "tổng tiền = 1.1 x (7000 + 2 x 2000) + 50 x 10000 = 512100"},
    {"id": "BVA_TC16", "inputs": (25.0, 19.9, 2, 50), "expected": "tổng tiền = 19.9 x (7000 + 2 x 2000) + 50 x 10000 = 718900"},
    {"id": "BVA_TC17", "inputs": (25.0, 20.0, 2, 50), "expected": "tổng tiền = 20.0 x (7000 + 2 x 2000) + 50 x 10000 = 720000"},
    {"id": "BVA_TC18", "inputs": (25.0, 20.1, 2, 50), "expected": "tổng tiền = 20.1 x (7000 + 2 x 2000) + 50 x 10000 - 20000 = 701100"},
    {"id": "BVA_TC19", "inputs": (25.0, 49.9, 2, 50), "expected": "tổng tiền = 49.9 x (7000 + 2 x 2000) + 50 x 10000 - 20000 = 1028900"},
    {"id": "BVA_TC20", "inputs": (25.0, 50.0, 2, 50), "expected": "tổng tiền = 50.0 x (7000 + 2 x 2000) + 50 x 10000 - 20000 = 1030000"},
    {"id": "BVA_TC21", "inputs": (25.0, 50.1, 2, 50), "expected": "INVALID"},
    {"id": "BVA_TC22", "inputs": (25.0, 25.5, 0, 50), "expected": "INVALID"},
    {"id": "BVA_TC23", "inputs": (25.0, 25.5, 1, 50), "expected": "tổng tiền = 25.5 x (7000 + 1 x 2000) + 50 x 10000 - 20000 = 709500"},
    {"id": "BVA_TC24", "inputs": (25.0, 25.5, 2, 50), "expected": "tổng tiền = 25.5 x (7000 + 2 x 2000) + 50 x 10000 - 20000 = 760500"},
    {"id": "BVA_TC25", "inputs": (25.0, 25.5, 3, 50), "expected": "tổng tiền = 25.5 x (7000 + 3 x 2000) + 50 x 10000 - 20000 = 811500"},
    {"id": "BVA_TC26", "inputs": (25.0, 25.5, 4, 50), "expected": "INVALID"},
    {"id": "BVA_TC27", "inputs": (25.0, 25.5, 2, -1), "expected": "INVALID"},
    {"id": "BVA_TC28", "inputs": (25.0, 25.5, 2, 0), "expected": "tổng tiền = 25.5 x (7000 + 2 x 2000) + 0 x 10000 - 20000 = 260500"},
    {"id": "BVA_TC29", "inputs": (25.0, 25.5, 2, 1), "expected": "tổng tiền = 25.5 x (7000 + 2 x 2000) + 1 x 10000 - 20000 = 270500"},
    {"id": "BVA_TC30", "inputs": (25.0, 25.5, 2, 99), "expected": "tổng tiền = 25.5 x (7000 + 2 x 2000) + 99 x 10000 - 20000 = 1250500"},
    {"id": "BVA_TC31", "inputs": (25.0, 25.5, 2, 100), "expected": "tổng tiền = 25.5 x (7000 + 2 x 2000) + 100 x 10000 - 20000 = 1260500"},
    {"id": "BVA_TC32", "inputs": (25.0, 25.5, 2, 101), "expected": "INVALID"},
    {"id": "BVA_TC33", "inputs": (25.0, 25.5, 2, 50), "expected": "tổng tiền = 25.5 x (7000 + 2 x 2000) + 50 x 10000 - 20000 = 760500"}
]


# ==============================================================================
# HÀM THỰC THI KIỂM THỬ CHUNG
# ==============================================================================
def execute_test_suite(suite_name, test_func, test_cases):
    print("\n" + "=" * 90)
    print(f"CHẠY BỘ KIỂM THỬ: {suite_name}")
    print("=" * 90)
    passed_count = 0
    for tc in test_cases:
        actual = test_func(*tc["inputs"])
        expected_norm = normalize_output(tc["expected"])
        actual_norm = normalize_output(actual)
        passed = (actual_norm == expected_norm)
        if passed:
            passed_count += 1

        status = "PASS" if passed else "FAIL"
        class_info = f" - {tc['class']}" if "class" in tc else ""
        print(f"[{tc['id']}{class_info}] Input: {tc['inputs']} -> Status: {status}")
        print(f"   Expected: {expected_norm}")
        print(f"   Actual:   {actual_norm}")
        print("-" * 90)

    print(f"Tổng kết {suite_name}: {passed_count}/{len(test_cases)} test cases PASSED\n")


if __name__ == "__main__":
    # Bài toán 1
    execute_test_suite("BÀI TOÁN 1 - PHÂN HOẠCH TƯƠNG ĐƯƠNG (EP)", calculate_movie_ticket, ep_test_cases_bai1)
    execute_test_suite("BÀI TOÁN 1 - KIỂM THỬ GIÁ TRỊ BIÊN (BVA)", calculate_movie_ticket, bva_test_cases_bai1)
    execute_test_suite("BÀI TOÁN 1 - BẢNG QUYẾT ĐỊNH (BQD)", calculate_movie_ticket, bqd_test_cases_bai1)

    # Bài toán 2
    execute_test_suite("BÀI TOÁN 2 - PHÂN HOẠCH TƯƠNG ĐƯƠNG (EP)", calculate_shipping_fee, ep_test_cases_bai2)
    execute_test_suite("BÀI TOÁN 2 - KIỂM THỬ GIÁ TRỊ BIÊN (BVA)", calculate_shipping_fee, bva_test_cases_bai2)
    execute_test_suite("BÀI TOÁN 2 - BẢNG QUYẾT ĐỊNH (BQD)", calculate_shipping_fee, bqd_test_cases_bai2)