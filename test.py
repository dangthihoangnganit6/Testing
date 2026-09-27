import re
from main import calculate_movie_ticket, calculate_shipping_fee

def normalize_output(text):
    """
    Chuẩn hóa kết quả đầu ra:
    Nếu output có dạng 'tổng tiền = [công thức] = [số tiền] ...',
    chuyển về dạng gọn 'tổng tiền = [số tiền] ...' để so sánh chính xác với kết quả hàm.
    """
    match = re.search(r"tổng tiền = .*?=\s*(\d+)(.*)", text)
    if match:
        amount = match.group(1)
        suffix = match.group(2).strip()
        if suffix:
            return f"tổng tiền = {amount} {suffix}"
        return f"tổng tiền = {amount}"
    return text.strip()


# ==========================================
# TEST CASES BÀI TOÁN 1
# ==========================================
test_cases_bai1 = [
    {
        "id": "TC1",
        "class": "O1",
        "inputs": (-5, 5, 2),
        "expected": "INVALID"
    },
    {
        "id": "TC2",
        "class": "O2",
        "inputs": (9, 5, 2),
        "expected": "Không đủ tuổi"
    },
    {
        "id": "TC3",
        "class": "O3",
        "inputs": (20, 2, 2),
        "expected": "tổng tiền = 2 x (50000 + 2 x 10000) = 140000"
    },
    {
        "id": "TC4",
        "class": "O4",
        "inputs": (20, 5, 2),
        "expected": "tổng tiền = 5 x (50000 + 2 x 10000) = 350000 và thông báo tặng bắp"
    },
    {
        "id": "TC5",
        "class": "O5",
        "inputs": (20, 9, 2),
        "expected": "tổng tiền = 9 x (50000 + 2 x 10000) = 630000 và thông báo tặng combo"
    },
    {
        "id": "TC6",
        "class": "O6",
        "inputs": (61, 2, 2),
        "expected": "tổng tiền = 2 x (80000 + 2 x 10000) = 200000"
    },
    {
        "id": "TC7",
        "class": "O7",
        "inputs": (61, 5, 2),
        "expected": "tổng tiền = 5 x (80000 + 2 x 10000) = 500000 và thông báo tặng bắp"
    },
    {
        "id": "TC8",
        "class": "O8",
        "inputs": (61, 9, 2),
        "expected": "tổng tiền = 9 x (80000 + 2 x 10000) = 900000 và thông báo tặng combo"
    }
]


# ==========================================
# TEST CASES BÀI TOÁN 2
# ==========================================
test_cases_bai2 = [
    {
        "id": "TC1",
        "class": "O1",
        "inputs": (-2.0, 25.5, 2, 50),
        "expected": "INVALID"
    },
    {
        "id": "TC2",
        "class": "O2",
        "inputs": (40.0, 25.5, 2, 50),
        "expected": "Quá tải trọng"
    },
    {
        "id": "TC3",
        "class": "O3",
        "inputs": (2.5, 10.5, 2, 50),
        "expected": "tổng tiền = 10.5 x (5000 + 2 x 2000) + 50 x 10000 = 594500"
    },
    {
        "id": "TC4",
        "class": "O4",
        "inputs": (2.5, 35.0, 2, 50),
        "expected": "tổng tiền = 35.0 x (5000 + 2 x 2000) + 50 x 10000 - 20000 = 795000"
    },
    {
        "id": "TC5",
        "class": "O5",
        "inputs": (17.5, 10.5, 2, 50),
        "expected": "tổng tiền = 10.5 x (7000 + 2 x 2000) + 50 x 10000 = 615500"
    },
    {
        "id": "TC6",
        "class": "O6",
        "inputs": (17.5, 35.0, 2, 50),
        "expected": "tổng tiền = 35.0 x (7000 + 2 x 2000) + 50 x 10000 - 20000 = 865000"
    }
]


def run_tests():
    print("=" * 90)
    print("CHẠY KIỂM THỬ BÀI TOÁN 1: HỆ THỐNG ĐẶT VÉ XEM PHIM")
    print("=" * 90)
    bai1_passed = 0
    for tc in test_cases_bai1:
        actual = calculate_movie_ticket(*tc["inputs"])
        expected_norm = normalize_output(tc["expected"])
        actual_norm = normalize_output(actual)
        passed = (actual_norm == expected_norm)
        if passed:
            bai1_passed += 1

        status = "PASS" if passed else "FAIL"
        print(f"[{tc['id']} - {tc['class']}] Input: {tc['inputs']} -> Status: {status}")
        print(f"   Expected: {expected_norm}")
        print(f"   Actual:   {actual_norm}")
        print("-" * 90)
    print(f"Tổng kết Bài toán 1: {bai1_passed}/{len(test_cases_bai1)} test cases PASSED\n")

    print("=" * 90)
    print("CHẠY KIỂM THỬ BÀI TOÁN 2: HỆ THỐNG TÍNH CƯỚC VẬN CHUYỂN HÀNG")
    print("=" * 90)
    bai2_passed = 0
    for tc in test_cases_bai2:
        actual = calculate_shipping_fee(*tc["inputs"])
        expected_norm = normalize_output(tc["expected"])
        actual_norm = normalize_output(actual)
        passed = (actual_norm == expected_norm)
        if passed:
            bai2_passed += 1

        status = "PASS" if passed else "FAIL"
        print(f"[{tc['id']} - {tc['class']}] Input: {tc['inputs']} -> Status: {status}")
        print(f"   Expected: {expected_norm}")
        print(f"   Actual:   {actual_norm}")
        print("-" * 90)
    print(f"Tổng kết Bài toán 2: {bai2_passed}/{len(test_cases_bai2)} test cases PASSED")
    print("=" * 90)


if __name__ == "__main__":
    run_tests()