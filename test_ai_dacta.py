"""
Test suite cho He thong Kiem thu Hop den (Black-box Testing)
Dua hoan toan tren Dac ta yeu cau nghiep vu (Dac ta bai 1 va Dac ta bai 2).

Bao gom 3 ky thuat kiem thu:
1. Equivalence Partitioning (Phan hoach tuong duong)
2. Boundary Value Analysis (Kiem thu gia tri bien - 3 gia tri)
3. Decision Table Testing (Bang quyet dinh)
"""

import pytest
try:
    from main import calculate_movie_ticket, calculate_shipping_fee
except ImportError:
    # Du phong truong hop module co ten khac hoac duoc import cach khac
    from logic import calculate_movie_ticket, calculate_shipping_fee


# ==============================================================================
# 1. CLASS: EQUIVALENCE PARTITIONING (PHAN HOACH TUONG DUONG)
# ==============================================================================
class Test_AI_EquivalencePartitioning:
    """
    Kiem thu theo ky thuat Phan hoach tuong duong (Equivalence Partitioning).
    Bao phu toan bo cac phan hoach hop le (Valid) va khong hop le (Invalid).
    """

    # ---------------------------------------------------------
    # Bai toan 1: He thong dat ve xem phim
    # ---------------------------------------------------------

    # Phân hoạch KHÔNG HỢP LỆ (Invalid Partitions) cho Bài toán 1
    @pytest.mark.parametrize("age, quantity, ticket_type, expected", [
        # tuổi < 1
        (0, 5, 2, "INVALID"),
        (-10, 5, 2, "INVALID"),
        # tuổi > 100
        (101, 5, 2, "INVALID"),
        (150, 5, 2, "INVALID"),
        # số lượng < 1
        (20, 0, 2, "INVALID"),
        (20, -1, 2, "INVALID"),
        # số lượng > 10
        (20, 11, 2, "INVALID"),
        (20, 20, 2, "INVALID"),
        # hạng vé < 1
        (20, 5, 0, "INVALID"),
        (20, 5, -1, "INVALID"),
        # hạng vé > 3
        (20, 5, 4, "INVALID"),
        (20, 5, 10, "INVALID"),
        # nhiều giá trị không hợp lệ cùng lúc
        (-5, 0, 0, "INVALID"),
        (105, 15, 5, "INVALID"),
    ])
    def test_movie_ticket_invalid_partitions(self, age, quantity, ticket_type, expected):
        result = calculate_movie_ticket(age, quantity, ticket_type)
        assert result == expected

    # Phân hoạch HỢP LỆ (Valid Partitions) cho Bài toán 1
    @pytest.mark.parametrize("age, quantity, ticket_type, expected", [
        # Phân hoạch tuổi ∈ [1 .. 18) -> Không đủ tuổi
        (5, 1, 1, "Không đủ tuổi"),
        (10, 5, 2, "Không đủ tuổi"),
        (17, 10, 3, "Không đủ tuổi"),

        # Phân hoạch tuổi ∈ [18 .. 22] (giá vé 50000 + hạng vé x 10000)
        # - số lượng ∈ [1 .. 3]: không quà tặng
        (20, 2, 1, f"Tổng tiền = {2 * (50000 + 1 * 10000)}"),
        (18, 3, 2, f"Tổng tiền = {3 * (50000 + 2 * 10000)}"),
        (22, 1, 3, f"Tổng tiền = {1 * (50000 + 3 * 10000)}"),
        # - số lượng ∈ (3 .. 7]: tặng bắp
        (19, 5, 1, f"Tổng tiền = {5 * (50000 + 1 * 10000)} và thông báo tặng bắp"),
        (21, 4, 2, f"Tổng tiền = {4 * (50000 + 2 * 10000)} và thông báo tặng bắp"),
        (20, 7, 3, f"Tổng tiền = {7 * (50000 + 3 * 10000)} và thông báo tặng bắp"),
        # - số lượng ∈ (7 .. 10]: tặng combo
        (18, 8, 1, f"Tổng tiền = {8 * (50000 + 1 * 10000)} và thông báo tặng combo"),
        (20, 9, 2, f"Tổng tiền = {9 * (50000 + 2 * 10000)} và thông báo tặng combo"),
        (22, 10, 3, f"Tổng tiền = {10 * (50000 + 3 * 10000)} và thông báo tặng combo"),

        # Phân hoạch tuổi ∈ (22 .. 100] (giá vé 80000 + hạng vé x 10000)
        # - số lượng ∈ [1 .. 3]: không quà tặng
        (30, 2, 1, f"Tổng tiền = {2 * (80000 + 1 * 10000)}"),
        (50, 3, 2, f"Tổng tiền = {3 * (80000 + 2 * 10000)}"),
        (70, 1, 3, f"Tổng tiền = {1 * (80000 + 3 * 10000)}"),
        # - số lượng ∈ (3 .. 7]: tặng bắp
        (25, 4, 1, f"Tổng tiền = {4 * (80000 + 1 * 10000)} và thông báo tặng bắp"),
        (40, 5, 2, f"Tổng tiền = {5 * (80000 + 2 * 10000)} và thông báo tặng bắp"),
        (65, 7, 3, f"Tổng tiền = {7 * (80000 + 3 * 10000)} và thông báo tặng bắp"),
        # - số lượng ∈ (7 .. 10]: tặng combo
        (35, 8, 1, f"Tổng tiền = {8 * (80000 + 1 * 10000)} và thông báo tặng combo"),
        (45, 9, 2, f"Tổng tiền = {9 * (80000 + 2 * 10000)} và thông báo tặng combo"),
        (60, 10, 3, f"Tổng tiền = {10 * (80000 + 3 * 10000)} và thông báo tặng combo"),
    ])
    def test_movie_ticket_valid_partitions(self, age, quantity, ticket_type, expected):
        result = calculate_movie_ticket(age, quantity, ticket_type)
        assert result == expected

    # ---------------------------------------------------------
    # Bai toan 2: He thong tinh cuoc van chuyen hang
    # ---------------------------------------------------------

    # Phân hoạch KHÔNG HỢP LỆ (Invalid Partitions) cho Bài toán 2
    @pytest.mark.parametrize("weight, distance, service_type, cargo_value, expected", [
        # khối lượng < 0.1
        (0.0, 10.0, 2, 20, "INVALID"),
        (-5.0, 10.0, 2, 20, "INVALID"),
        # khối lượng > 50.0
        (50.1, 10.0, 2, 20, "INVALID"),
        (70.0, 10.0, 2, 20, "INVALID"),
        # khoảng cách < 1.0
        (10.0, 0.5, 2, 20, "INVALID"),
        (10.0, -1.0, 2, 20, "INVALID"),
        # khoảng cách > 50.0
        (10.0, 50.5, 2, 20, "INVALID"),
        (10.0, 100.0, 2, 20, "INVALID"),
        # loại dịch vụ < 1
        (10.0, 10.0, 0, 20, "INVALID"),
        (10.0, 10.0, -1, 20, "INVALID"),
        # loại dịch vụ > 3
        (10.0, 10.0, 4, 20, "INVALID"),
        (10.0, 10.0, 10, 20, "INVALID"),
        # giá trị hàng < 0
        (10.0, 10.0, 2, -1, "INVALID"),
        (10.0, 10.0, 2, -50, "INVALID"),
        # giá trị hàng > 100
        (10.0, 10.0, 2, 101, "INVALID"),
        (10.0, 10.0, 2, 200, "INVALID"),
    ])
    def test_shipping_fee_invalid_partitions(self, weight, distance, service_type, cargo_value, expected):
        result = calculate_shipping_fee(weight, distance, service_type, cargo_value)
        assert result == expected

    # Phân hoạch HỢP LỆ (Valid Partitions) cho Bài toán 2
    @pytest.mark.parametrize("weight, distance, service_type, cargo_value, expected_val", [
        # Quá tải trọng: khối lượng ∈ (30.0 .. 50.0]
        (35.0, 15.0, 1, 10, "Quá tải trọng"),
        (40.0, 30.0, 2, 50, "Quá tải trọng"),
        (50.0, 50.0, 3, 100, "Quá tải trọng"),

        # Nhẹ: khối lượng ∈ [0.1 .. 5.0], khoảng cách ngắn ∈ [1.0 .. 20.0]
        # Tiền = distance * (5000 + service * 2000) + cargo_value * 10000
        (2.0, 10, 1, 1, 10 * (5000 + 1 * 2000) + 1 * 10000),
        (4.0, 15, 2, 5, 15 * (5000 + 2 * 2000) + 5 * 10000),

        # Nhẹ: khối lượng ∈ [0.1 .. 5.0], khoảng cách dài ∈ (20.0 .. 50.0]
        # Tiền = distance * (5000 + service * 2000) + cargo_value * 10000 - 20000
        (3.0, 25, 1, 2, 25 * (5000 + 1 * 2000) + 2 * 10000 - 20000),
        (1.0, 40, 3, 10, 40 * (5000 + 3 * 2000) + 10 * 10000 - 20000),

        # Tiêu chuẩn: khối lượng ∈ (5.0 .. 30.0], khoảng cách ngắn ∈ [1.0 .. 20.0]
        # Tiền = distance * (7000 + service * 2000) + cargo_value * 10000
        (15.0, 10, 1, 1, 10 * (7000 + 1 * 2000) + 1 * 10000),
        (20.0, 12, 2, 8, 12 * (7000 + 2 * 2000) + 8 * 10000),

        # Tiêu chuẩn: khối lượng ∈ (5.0 .. 30.0], khoảng cách dài ∈ (20.0 .. 50.0]
        # Tiền = distance * (7000 + service * 2000) + cargo_value * 10000 - 20000
        (10.0, 25, 1, 1, 25 * (7000 + 1 * 2000) + 1 * 10000 - 20000),
        (25.0, 35, 3, 20, 35 * (7000 + 3 * 2000) + 20 * 10000 - 20000),
    ])
    def test_shipping_fee_valid_partitions(self, weight, distance, service_type, cargo_value, expected_val):
        result = calculate_shipping_fee(weight, distance, service_type, cargo_value)
        if isinstance(expected_val, str):
            assert result == expected_val
        else:
            prefix, val_str = result.lower().split("=")
            assert prefix.strip() == "tổng tiền"
            assert float(val_str.strip()) == pytest.approx(float(expected_val))


# ==============================================================================
# 2. CLASS: BOUNDARY VALUE ANALYSIS (KIEM THU GIA TRI BIEN - 3 GIA TRI)
# ==============================================================================
class Test_AI_BoundaryValueAnalysis:
    """
    Kiem thu gia tri bien (BVA) theo ky thuat 3 gia tri:
    {min-, min, min+} va {max-, max, max+}
    cung cac diem bien chuyen tiep cua tung vung dieu kien con.
    """

    # ---------------------------------------------------------
    # Bai toan 1: He thong dat ve xem phim
    # ---------------------------------------------------------

    # 1.1 Biên biến Tuổi (age):
    # - Biên toàn cục min (1): {0, 1, 2}
    # - Biên chuyển tiếp đủ tuổi (18): {17, 18, 19}
    # - Biên chuyển tiếp mức giá tuổi (22): {21, 22, 23}
    # - Biên toàn cục max (100): {99, 100, 101}
    @pytest.mark.parametrize("age, quantity, ticket_type, expected", [
        # Biên min toàn cục: 0 (min-), 1 (min), 2 (min+)
        (0, 2, 1, "INVALID"),
        (1, 2, 1, "Không đủ tuổi"),
        (2, 2, 1, "Không đủ tuổi"),

        # Biên chuyển tiếp tuổi 18: 17, 18, 19
        (17, 2, 1, "Không đủ tuổi"),
        (18, 2, 1, f"Tổng tiền = {2 * (50000 + 1 * 10000)}"),
        (19, 2, 1, f"Tổng tiền = {2 * (50000 + 1 * 10000)}"),

        # Biên chuyển tiếp tuổi 22: 21, 22, 23
        (21, 2, 1, f"Tổng tiền = {2 * (50000 + 1 * 10000)}"),
        (22, 2, 1, f"Tổng tiền = {2 * (50000 + 1 * 10000)}"),
        (23, 2, 1, f"Tổng tiền = {2 * (80000 + 1 * 10000)}"),

        # Biên max toàn cục: 99 (max-), 100 (max), 101 (max+)
        (99, 2, 1, f"Tổng tiền = {2 * (80000 + 1 * 10000)}"),
        (100, 2, 1, f"Tổng tiền = {2 * (80000 + 1 * 10000)}"),
        (101, 2, 1, "INVALID"),
    ])
    def test_movie_ticket_bva_age(self, age, quantity, ticket_type, expected):
        result = calculate_movie_ticket(age, quantity, ticket_type)
        assert result == expected

    # 1.2 Biên biến Số lượng (quantity):
    # - Biên toàn cục min (1): {0, 1, 2}
    # - Biên chuyển tiếp quà bắp (3): {2, 3, 4}
    # - Biên chuyển tiếp quà combo (7): {6, 7, 8}
    # - Biên toàn cục max (10): {9, 10, 11}
    @pytest.mark.parametrize("age, quantity, ticket_type, expected", [
        # Biên min: 0, 1, 2 (với age=20, ticket_type=1)
        (20, 0, 1, "INVALID"),
        (20, 1, 1, f"Tổng tiền = {1 * (50000 + 1 * 10000)}"),
        (20, 2, 1, f"Tổng tiền = {2 * (50000 + 1 * 10000)}"),

        # Biên chuyển tiếp số lượng 3: 2, 3, 4
        (20, 3, 1, f"Tổng tiền = {3 * (50000 + 1 * 10000)}"),
        (20, 4, 1, f"Tổng tiền = {4 * (50000 + 1 * 10000)} và thông báo tặng bắp"),

        # Biên chuyển tiếp số lượng 7: 6, 7, 8
        (20, 6, 1, f"Tổng tiền = {6 * (50000 + 1 * 10000)} và thông báo tặng bắp"),
        (20, 7, 1, f"Tổng tiền = {7 * (50000 + 1 * 10000)} và thông báo tặng bắp"),
        (20, 8, 1, f"Tổng tiền = {8 * (50000 + 1 * 10000)} và thông báo tặng combo"),

        # Biên max: 9, 10, 11
        (20, 9, 1, f"Tổng tiền = {9 * (50000 + 1 * 10000)} và thông báo tặng combo"),
        (20, 10, 1, f"Tổng tiền = {10 * (50000 + 1 * 10000)} và thông báo tặng combo"),
        (20, 11, 1, "INVALID"),
    ])
    def test_movie_ticket_bva_quantity(self, age, quantity, ticket_type, expected):
        result = calculate_movie_ticket(age, quantity, ticket_type)
        assert result == expected

    # 1.3 Biên biến Hạng vé (ticket_type):
    # - Biên min (1): {0, 1, 2}
    # - Biên max (3): {2, 3, 4}
    @pytest.mark.parametrize("age, quantity, ticket_type, expected", [
        (20, 2, 0, "INVALID"),
        (20, 2, 1, f"Tổng tiền = {2 * (50000 + 1 * 10000)}"),
        (20, 2, 2, f"Tổng tiền = {2 * (50000 + 2 * 10000)}"),
        (20, 2, 3, f"Tổng tiền = {2 * (50000 + 3 * 10000)}"),
        (20, 2, 4, "INVALID"),
    ])
    def test_movie_ticket_bva_ticket_type(self, age, quantity, ticket_type, expected):
        result = calculate_movie_ticket(age, quantity, ticket_type)
        assert result == expected

    # ---------------------------------------------------------
    # Bai toan 2: He thong tinh cuoc van chuyen hang
    # ---------------------------------------------------------

    # 2.1 Biên Khối lượng (weight):
    # - Biên min (0.1): 0.0, 0.1, 0.2
    # - Biên tải trọng nhẹ (5.0): 4.9, 5.0, 5.1
    # - Biên tải trọng tối đa (30.0): 29.9, 30.0, 30.1
    # - Biên max toàn cục (50.0): 49.9, 50.0, 50.1
    @pytest.mark.parametrize("weight, distance, service_type, cargo_value, expected_val", [
        # Biên min toàn cục: 0.0 (min-), 0.1 (min), 0.2 (min+)
        (0.0, 10, 1, 10, "INVALID"),
        (0.1, 10, 1, 10, 10 * (5000 + 1 * 2000) + 10 * 10000),
        (0.2, 10, 1, 10, 10 * (5000 + 1 * 2000) + 10 * 10000),

        # Biên chuyển tiếp 5.0: 4.9, 5.0, 5.1
        (4.9, 10, 1, 10, 10 * (5000 + 1 * 2000) + 10 * 10000),
        (5.0, 10, 1, 10, 10 * (5000 + 1 * 2000) + 10 * 10000),
        (5.1, 10, 1, 10, 10 * (7000 + 1 * 2000) + 10 * 10000),

        # Biên tải trọng tối đa 30.0: 29.9, 30.0, 30.1
        (29.9, 10, 1, 10, 10 * (7000 + 1 * 2000) + 10 * 10000),
        (30.0, 10, 1, 10, 10 * (7000 + 1 * 2000) + 10 * 10000),
        (30.1, 10, 1, 10, "Quá tải trọng"),

        # Biên max toàn cục: 49.9, 50.0, 50.1
        (49.9, 10, 1, 10, "Quá tải trọng"),
        (50.0, 10, 1, 10, "Quá tải trọng"),
        (50.1, 10, 1, 10, "INVALID"),
    ])
    def test_shipping_fee_bva_weight(self, weight, distance, service_type, cargo_value, expected_val):
        result = calculate_shipping_fee(weight, distance, service_type, cargo_value)
        if isinstance(expected_val, str):
            assert result == expected_val
        else:
            prefix, val_str = result.lower().split("=")
            assert prefix.strip() == "tổng tiền"
            assert float(val_str.strip()) == pytest.approx(float(expected_val))

    # 2.2 Biên Khoảng cách (distance):
    # - Biên min (1.0): 0.9, 1.0, 1.1
    # - Biên ưu đãi cự ly (20.0): 19.9, 20.0, 20.1
    # - Biên max (50.0): 49.9, 50.0, 50.1
    @pytest.mark.parametrize("weight, distance, service_type, cargo_value, expected_val", [
        # Biên min: 0.9, 1.0, 1.1
        (2.0, 0.9, 1, 5, "INVALID"),
        (2.0, 1.0, 1, 5, 1.0 * (5000 + 1 * 2000) + 5 * 10000),
        (2.0, 1.1, 1, 5, 1.1 * (5000 + 1 * 2000) + 5 * 10000),

        # Biên chuyển tiếp ưu đãi 20.0: 19.9, 20.0, 20.1
        (2.0, 19.9, 1, 5, 19.9 * (5000 + 1 * 2000) + 5 * 10000),
        (2.0, 20.0, 1, 5, 20.0 * (5000 + 1 * 2000) + 5 * 10000),
        (2.0, 20.1, 1, 5, 20.1 * (5000 + 1 * 2000) + 5 * 10000 - 20000),

        # Biên max: 49.9, 50.0, 50.1
        (2.0, 49.9, 1, 5, 49.9 * (5000 + 1 * 2000) + 5 * 10000 - 20000),
        (2.0, 50.0, 1, 5, 50.0 * (5000 + 1 * 2000) + 5 * 10000 - 20000),
        (2.0, 50.1, 1, 5, "INVALID"),
    ])
    def test_shipping_fee_bva_distance(self, weight, distance, service_type, cargo_value, expected_val):
        result = calculate_shipping_fee(weight, distance, service_type, cargo_value)
        if isinstance(expected_val, str):
            assert result == expected_val
        else:
            prefix, val_str = result.lower().split("=")
            assert prefix.strip() == "tổng tiền"
            assert float(val_str.strip()) == pytest.approx(float(expected_val))

    # 2.3 Biên Loại dịch vụ (service_type) và Giá trị hàng (cargo_value)
    @pytest.mark.parametrize("weight, distance, service_type, cargo_value, expected_val", [
        # Biên loại dịch vụ: 0 (min-), 1 (min), 3 (max), 4 (max+)
        (2.0, 10, 0, 5, "INVALID"),
        (2.0, 10, 1, 5, 10 * (5000 + 1 * 2000) + 5 * 10000),
        (2.0, 10, 3, 5, 10 * (5000 + 3 * 2000) + 5 * 10000),
        (2.0, 10, 4, 5, "INVALID"),

        # Biên giá trị hàng: -1 (min-), 0 (min), 1 (min+), 99 (max-), 100 (max), 101 (max+)
        (2.0, 10, 1, -1, "INVALID"),
        (2.0, 10, 1, 0, 10 * (5000 + 1 * 2000) + 0 * 10000),
        (2.0, 10, 1, 1, 10 * (5000 + 1 * 2000) + 1 * 10000),
        (2.0, 10, 1, 99, 10 * (5000 + 1 * 2000) + 99 * 10000),
        (2.0, 10, 1, 100, 10 * (5000 + 1 * 2000) + 100 * 10000),
        (2.0, 10, 1, 101, "INVALID"),
    ])
    def test_shipping_fee_bva_service_and_cargo(self, weight, distance, service_type, cargo_value, expected_val):
        result = calculate_shipping_fee(weight, distance, service_type, cargo_value)
        if isinstance(expected_val, str):
            assert result == expected_val
        else:
            prefix, val_str = result.lower().split("=")
            assert prefix.strip() == "tổng tiền"
            assert float(val_str.strip()) == pytest.approx(float(expected_val))


# ==============================================================================
# 3. CLASS: DECISION TABLE (BANG QUYET DINH)
# ==============================================================================
class Test_AI_DecisionTable:
    """
    Kiem thu theo Bang quyet dinh (Decision Table).
    Phu toan bo cac ket hop dieu kien nghiep vu va hanh dong tuong ung.
    """

    # ---------------------------------------------------------
    # Decision Table - Bai toan 1: He thong dat ve xem phim
    # Rules:
    # R1: Tuổi không hợp lệ -> INVALID
    # R2: Số lượng không hợp lệ -> INVALID
    # R3: Hạng vé không hợp lệ -> INVALID
    # R4: Tuổi < 18 -> "Không đủ tuổi"
    # R5: Tuổi [18..22], Số lượng [1..3] -> Giá 50k, không quà
    # R6: Tuổi [18..22], Số lượng (3..7] -> Giá 50k, tặng bắp
    # R7: Tuổi [18..22], Số lượng (7..10] -> Giá 50k, tặng combo
    # R8: Tuổi (22..100], Số lượng [1..3] -> Giá 80k, không quà
    # R9: Tuổi (22..100], Số lượng (3..7] -> Giá 80k, tặng bắp
    # R10: Tuổi (22..100], Số lượng (7..10] -> Giá 80k, tặng combo
    # ---------------------------------------------------------
    @pytest.mark.parametrize("rule_id, age, quantity, ticket_type, expected", [
        ("R1_Tuoi_KhongHopLe", -1, 2, 1, "INVALID"),
        ("R2_SoLuong_KhongHopLe", 20, 15, 1, "INVALID"),
        ("R3_HangVe_KhongHopLe", 20, 2, 5, "INVALID"),
        ("R4_KhongDuTuoi", 16, 2, 1, "Không đủ tuổi"),
        ("R5_Tre_SoLuongIt_Hang1", 18, 2, 1, f"Tổng tiền = {2 * (50000 + 1 * 10000)}"),
        ("R5_Tre_SoLuongIt_Hang2", 20, 3, 2, f"Tổng tiền = {3 * (50000 + 2 * 10000)}"),
        ("R5_Tre_SoLuongIt_Hang3", 22, 1, 3, f"Tổng tiền = {1 * (50000 + 3 * 10000)}"),
        ("R6_Tre_TangBap_Hang1", 19, 4, 1, f"Tổng tiền = {4 * (50000 + 1 * 10000)} và thông báo tặng bắp"),
        ("R6_Tre_TangBap_Hang2", 21, 6, 2, f"Tổng tiền = {6 * (50000 + 2 * 10000)} và thông báo tặng bắp"),
        ("R6_Tre_TangBap_Hang3", 22, 7, 3, f"Tổng tiền = {7 * (50000 + 3 * 10000)} và thông báo tặng bắp"),
        ("R7_Tre_TangCombo_Hang1", 18, 8, 1, f"Tổng tiền = {8 * (50000 + 1 * 10000)} và thông báo tặng combo"),
        ("R7_Tre_TangCombo_Hang2", 20, 9, 2, f"Tổng tiền = {9 * (50000 + 2 * 10000)} và thông báo tặng combo"),
        ("R7_Tre_TangCombo_Hang3", 22, 10, 3, f"Tổng tiền = {10 * (50000 + 3 * 10000)} và thông báo tặng combo"),
        ("R8_Lon_SoLuongIt_Hang1", 23, 1, 1, f"Tổng tiền = {1 * (80000 + 1 * 10000)}"),
        ("R8_Lon_SoLuongIt_Hang2", 30, 2, 2, f"Tổng tiền = {2 * (80000 + 2 * 10000)}"),
        ("R8_Lon_SoLuongIt_Hang3", 45, 3, 3, f"Tổng tiền = {3 * (80000 + 3 * 10000)}"),
        ("R9_Lon_TangBap_Hang1", 24, 4, 1, f"Tổng tiền = {4 * (80000 + 1 * 10000)} và thông báo tặng bắp"),
        ("R9_Lon_TangBap_Hang2", 35, 5, 2, f"Tổng tiền = {5 * (80000 + 2 * 10000)} và thông báo tặng bắp"),
        ("R9_Lon_TangBap_Hang3", 50, 7, 3, f"Tổng tiền = {7 * (80000 + 3 * 10000)} và thông báo tặng bắp"),
        ("R10_Lon_TangCombo_Hang1", 23, 8, 1, f"Tổng tiền = {8 * (80000 + 1 * 10000)} và thông báo tặng combo"),
        ("R10_Lon_TangCombo_Hang2", 40, 9, 2, f"Tổng tiền = {9 * (80000 + 2 * 10000)} và thông báo tặng combo"),
        ("R10_Lon_TangCombo_Hang3", 60, 10, 3, f"Tổng tiền = {10 * (80000 + 3 * 10000)} và thông báo tặng combo"),
    ])
    def test_movie_ticket_decision_table(self, rule_id, age, quantity, ticket_type, expected):
        result = calculate_movie_ticket(age, quantity, ticket_type)
        assert result == expected

    # ---------------------------------------------------------
    # Decision Table - Bai toan 2: He thong tinh cuoc van chuyen hang
    # Rules:
    # R1: Bất kỳ đầu vào nào ngoài phạm vi -> "INVALID"
    # R2: Khối lượng vượt 30kg (30 < W <= 50) -> "Quá tải trọng"
    # R3: Khối lượng nhẹ (0.1 <= W <= 5), Khoảng cách ngắn (1 <= D <= 20) -> Cước 5000, không giảm trừ
    # R4: Khối lượng nhẹ (0.1 <= W <= 5), Khoảng cách dài (20 < D <= 50) -> Cước 5000, giảm trừ 20000
    # R5: Khối lượng tiêu chuẩn (5 < W <= 30), Khoảng cách ngắn (1 <= D <= 20) -> Cước 7000, không giảm trừ
    # R6: Khối lượng tiêu chuẩn (5 < W <= 30), Khoảng cách dài (20 < D <= 50) -> Cước 7000, giảm trừ 20000
    # ---------------------------------------------------------
    @pytest.mark.parametrize("rule_id, weight, distance, service_type, cargo_value, expected_val", [
        ("R1_Weight_Invalid", -1.0, 10.0, 1, 10, "INVALID"),
        ("R1_Distance_Invalid", 10.0, 60.0, 1, 10, "INVALID"),
        ("R1_Service_Invalid", 10.0, 10.0, 0, 10, "INVALID"),
        ("R1_Cargo_Invalid", 10.0, 10.0, 1, -5, "INVALID"),
        ("R2_Overweight", 32.0, 15.0, 1, 10, "Quá tải trọng"),
        ("R2_Overweight_Max", 50.0, 25.0, 2, 20, "Quá tải trọng"),
        ("R3_Light_Short_Service1", 2.0, 10, 1, 5, 10 * (5000 + 1 * 2000) + 5 * 10000),
        ("R3_Light_Short_Service2", 3.0, 15, 2, 10, 15 * (5000 + 2 * 2000) + 10 * 10000),
        ("R3_Light_Short_Service3", 5.0, 20, 3, 0, 20 * (5000 + 3 * 2000) + 0 * 10000),
        ("R4_Light_Long_Service1", 1.0, 25, 1, 5, 25 * (5000 + 1 * 2000) + 5 * 10000 - 20000),
        ("R4_Light_Long_Service2", 2.5, 30, 2, 12, 30 * (5000 + 2 * 2000) + 12 * 10000 - 20000),
        ("R4_Light_Long_Service3", 4.0, 50, 3, 20, 50 * (5000 + 3 * 2000) + 20 * 10000 - 20000),
        ("R5_Standard_Short_Service1", 6.0, 10, 1, 5, 10 * (7000 + 1 * 2000) + 5 * 10000),
        ("R5_Standard_Short_Service2", 15.0, 12, 2, 15, 12 * (7000 + 2 * 2000) + 15 * 10000),
        ("R5_Standard_Short_Service3", 30.0, 20, 3, 30, 20 * (7000 + 3 * 2000) + 30 * 10000),
        ("R6_Standard_Long_Service1", 10.0, 22, 1, 5, 22 * (7000 + 1 * 2000) + 5 * 10000 - 20000),
        ("R6_Standard_Long_Service2", 20.0, 35, 2, 10, 35 * (7000 + 2 * 2000) + 10 * 10000 - 20000),
        ("R6_Standard_Long_Service3", 28.0, 48, 3, 25, 48 * (7000 + 3 * 2000) + 25 * 10000 - 20000),
    ])
    def test_shipping_fee_decision_table(self, rule_id, weight, distance, service_type, cargo_value, expected_val):
        result = calculate_shipping_fee(weight, distance, service_type, cargo_value)
        if isinstance(expected_val, str):
            assert result == expected_val
        else:
            prefix, val_str = result.lower().split("=")
            assert prefix.strip() == "tổng tiền"
            assert float(val_str.strip()) == pytest.approx(float(expected_val))
