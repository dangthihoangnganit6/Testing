"""
Test suite cho Kiem thu Hop trang (White-box Testing) dua tren cau truc ma lenh (main.py).

Bao gom 2 ky thuat:
1. Control Flow Testing: Dat 100% Statement Coverage va 100% Branch Coverage (bao phu ca cac dieu kien don trong bieu thuc or).
2. Data Flow Testing (All-Uses): Bao phu toan bo cac cap D-U (Def-Use pairs) cho cac bien chinh.
"""

import pytest
from main import calculate_movie_ticket, calculate_shipping_fee


# ==============================================================================
# 1. CLASS: CONTROL FLOW TESTING (STATEMENT & BRANCH COVERAGE)
# ==============================================================================
class Test_AI_ControlFlow:
    """
    Kiem thu dong dieu khien (Control Flow Testing):
    - 100% Statement Coverage (Bao phu moi dong lenh).
    - 100% Branch Coverage (Bao phu moi nhanh re True/False, ke ca cac dieu kien or phuc hop).
    """

    # --------------------------------------------------------------------------
    # 1.1 calculate_movie_ticket - Branch Coverage cho bieu thuc OR (Dong 4-10)
    # If condition:
    # (age < 1) or (age > 100) or (quantity < 1) or (quantity > 10) or (ticket_type < 1) or (ticket_type > 3)
    # --------------------------------------------------------------------------
    @pytest.mark.parametrize("branch_id, age, quantity, ticket_type, expected", [
        ("Cond1_Age_Underflow_True", 0, 2, 1, "INVALID"),       # age < 1 is True
        ("Cond2_Age_Overflow_True", 101, 2, 1, "INVALID"),      # age > 100 is True
        ("Cond3_Quantity_Underflow_True", 20, 0, 1, "INVALID"),  # quantity < 1 is True
        ("Cond4_Quantity_Overflow_True", 20, 11, 1, "INVALID"),  # quantity > 10 is True
        ("Cond5_TicketType_Underflow_True", 20, 2, 0, "INVALID"),# ticket_type < 1 is True
        ("Cond6_TicketType_Overflow_True", 20, 2, 4, "INVALID"), # ticket_type > 3 is True
    ])
    def test_movie_ticket_invalid_compound_or_branches(self, branch_id, age, quantity, ticket_type, expected):
        """Kiem thu tung nhanh True cua bieu thuc OR phuc hop o Dong 4-10."""
        result = calculate_movie_ticket(age, quantity, ticket_type)
        assert result == expected

    # --------------------------------------------------------------------------
    # 1.2 calculate_movie_ticket - Statement & Branch Coverage toan bo ham
    # --------------------------------------------------------------------------
    @pytest.mark.parametrize("path_id, age, quantity, ticket_type, expected", [
        # Nhanh: elif age < 18 (Dong 12) -> True (Dong 13: result = 'Không đủ tuổi')
        ("Path_Age_Under18", 17, 2, 1, "Không đủ tuổi"),

        # Nhanh: age in [18..22] (Dong 15: age <= 22 is True -> base_price = 50000)
        # - quantity <= 3 is True (Dong 22 -> Dong 23)
        ("Path_Age22_Qty3", 20, 2, 1, "Tổng tiền = 120000"),
        # - elif quantity <= 7 is True (Dong 24 -> Dong 25)
        ("Path_Age22_Qty7", 20, 5, 2, "Tổng tiền = 350000 và thông báo tặng bắp"),
        # - else (quantity > 7) (Dong 26 -> Dong 27)
        ("Path_Age22_Qty10", 20, 9, 3, "Tổng tiền = 720000 và thông báo tặng combo"),

        # Nhanh: age > 22 (Dong 15: age <= 22 is False -> Dong 17 else: base_price = 80000)
        # - quantity <= 3 is True (Dong 22 -> Dong 23)
        ("Path_AgeOver22_Qty3", 30, 2, 1, "Tổng tiền = 180000"),
        # - elif quantity <= 7 is True (Dong 24 -> Dong 25)
        ("Path_AgeOver22_Qty7", 30, 5, 2, "Tổng tiền = 500000 và thông báo tặng bắp"),
        # - else (quantity > 7) (Dong 26 -> Dong 27)
        ("Path_AgeOver22_Qty10", 30, 9, 3, "Tổng tiền = 990000 và thông báo tặng combo"),
    ])
    def test_movie_ticket_control_flow_paths(self, path_id, age, quantity, ticket_type, expected):
        """Kiem thu cac duong thuc thi phu 100% Statement va Branch con lai."""
        result = calculate_movie_ticket(age, quantity, ticket_type)
        assert result == expected

    # --------------------------------------------------------------------------
    # 1.3 calculate_shipping_fee - Branch Coverage cho bieu thuc OR (Dong 35-44)
    # If condition:
    # (weight < 0.1) or (weight > 50.0) or (distance < 1.0) or (distance > 50.0)
    # or (service_type < 1) or (service_type > 3) or (cargo_value < 0) or (cargo_value > 100)
    # --------------------------------------------------------------------------
    @pytest.mark.parametrize("branch_id, weight, distance, service_type, cargo_value, expected", [
        ("Cond1_Weight_Underflow_True", 0.0, 10.0, 1, 10, "INVALID"),
        ("Cond2_Weight_Overflow_True", 50.1, 10.0, 1, 10, "INVALID"),
        ("Cond3_Distance_Underflow_True", 10.0, 0.5, 1, 10, "INVALID"),
        ("Cond4_Distance_Overflow_True", 10.0, 50.5, 1, 10, "INVALID"),
        ("Cond5_Service_Underflow_True", 10.0, 10.0, 0, 10, "INVALID"),
        ("Cond6_Service_Overflow_True", 10.0, 10.0, 4, 10, "INVALID"),
        ("Cond7_Cargo_Underflow_True", 10.0, 10.0, 1, -1, "INVALID"),
        ("Cond8_Cargo_Overflow_True", 10.0, 10.0, 1, 101, "INVALID"),
    ])
    def test_shipping_fee_invalid_compound_or_branches(self, branch_id, weight, distance, service_type, cargo_value, expected):
        """Kiem thu tung nhanh True cua bieu thuc OR phuc hop o Dong 35-44."""
        result = calculate_shipping_fee(weight, distance, service_type, cargo_value)
        assert result == expected

    # --------------------------------------------------------------------------
    # 1.4 calculate_shipping_fee - Statement & Branch Coverage toan bo ham
    # --------------------------------------------------------------------------
    @pytest.mark.parametrize("path_id, weight, distance, service_type, cargo_value, expected", [
        # Nhanh: elif weight > 30.0 (Dong 46) -> True (Dong 47: result = 'Quá tải trọng')
        ("Path_Overweight", 35.0, 10.0, 1, 10, "Quá tải trọng"),

        # Nhanh: weight <= 5.0 is True (Dong 49 -> Dong 50: base_rate = 5000)
        # - distance <= 20.0 is True (Dong 58 -> Dong 59: total_price = base_total)
        # base_total = 10 * (5000 + 1 * 2000) + 1 * 10000 = 80000
        ("Path_WeightLight_DistShort", 2.0, 10, 1, 1, "tổng tiền = 80000"),
        # - distance <= 20.0 is False (Dong 58 -> Dong 61: total_price = base_total - 20000)
        # base_total = 25 * (5000 + 1 * 2000) + 1 * 10000 = 185000 -> 165000
        ("Path_WeightLight_DistLong", 2.0, 25, 1, 1, "tổng tiền = 165000"),

        # Nhanh: weight <= 5.0 is False (Dong 49 -> Dong 52 else: base_rate = 7000)
        # - distance <= 20.0 is True (Dong 58 -> Dong 59: total_price = base_total)
        # base_total = 10 * (7000 + 1 * 2000) + 1 * 10000 = 100000
        ("Path_WeightStandard_DistShort", 10.0, 10, 1, 1, "tổng tiền = 100000"),
        # - distance <= 20.0 is False (Dong 58 -> Dong 61: total_price = base_total - 20000)
        # base_total = 25 * (7000 + 1 * 2000) + 1 * 10000 = 235000 -> 215000
        ("Path_WeightStandard_DistLong", 10.0, 25, 1, 1, "tổng tiền = 215000"),
    ])
    def test_shipping_fee_control_flow_paths(self, path_id, weight, distance, service_type, cargo_value, expected):
        """Kiem thu cac duong thuc thi phu 100% Statement va Branch con lai cua shipping fee."""
        result = calculate_shipping_fee(weight, distance, service_type, cargo_value)
        assert result == expected


# ==============================================================================
# 2. CLASS: DATA FLOW TESTING (ALL-USES CRITERION)
# ==============================================================================
class Test_AI_DataFlow_AllUses:
    """
    Kiem thu dong du lieu (Data Flow Testing) theo tieu chuan All-Uses:
    Xac dinh tat ca cac cap D-U (Def-Use pairs), bao gom:
    - c-use (computation use)
    - p-use (predicate use)
    Dam bao moi duong di khong bi dinh nghia lai (def-clear path) tu def den use deu duoc kiem thu.
    """

    # --------------------------------------------------------------------------
    # 2.1 All-Uses cho calculate_movie_ticket
    # Du-pairs:
    # 1. def(age, 1) -> p-use(age, 5), p-use(age, 6), p-use(age, 12), p-use(age, 15)
    # 2. def(quantity, 1) -> p-use(quantity, 7), p-use(quantity, 8), c-use(quantity, 20), p-use(quantity, 22), p-use(quantity, 24)
    # 3. def(ticket_type, 1) -> p-use(ticket_type, 9), p-use(ticket_type, 10), c-use(ticket_type, 20)
    # 4. def(base_price, 16) [50000] -> c-use(base_price, 20)
    # 5. def(base_price, 18) [80000] -> c-use(base_price, 20)
    # 6. def(total_price, 20) -> c-use(total_price, 23), c-use(total_price, 25), c-use(total_price, 27)
    # 7. def(result, 11) -> c-use(result, 29)
    # 8. def(result, 13) -> c-use(result, 29)
    # 9. def(result, 23) -> c-use(result, 29)
    # 10. def(result, 25) -> c-use(result, 29)
    # 11. def(result, 27) -> c-use(result, 29)
    # --------------------------------------------------------------------------
    @pytest.mark.parametrize("du_pair_id, age, quantity, ticket_type, expected", [
        # DU: def(result, 11) -> use(result, 29)
        ("DU_result_def11_use29", 0, 1, 1, "INVALID"),

        # DU: def(result, 13) -> use(result, 29)
        ("DU_result_def13_use29", 15, 1, 1, "Không đủ tuổi"),

        # DU: def(base_price, 16) [50k] -> use(base_price, 20); def(total_price, 20) -> use(total_price, 23); def(result, 23) -> use(result, 29)
        ("DU_base_price_50k_to_qty3", 20, 2, 1, "Tổng tiền = 120000"),

        # DU: def(base_price, 16) [50k] -> use(base_price, 20); def(total_price, 20) -> use(total_price, 25); def(result, 25) -> use(result, 29)
        ("DU_base_price_50k_to_qty7", 20, 5, 2, "Tổng tiền = 350000 và thông báo tặng bắp"),

        # DU: def(base_price, 16) [50k] -> use(base_price, 20); def(total_price, 20) -> use(total_price, 27); def(result, 27) -> use(result, 29)
        ("DU_base_price_50k_to_qty10", 20, 8, 3, "Tổng tiền = 640000 và thông báo tặng combo"),

        # DU: def(base_price, 18) [80k] -> use(base_price, 20); def(total_price, 20) -> use(total_price, 23); def(result, 23) -> use(result, 29)
        ("DU_base_price_80k_to_qty3", 25, 1, 1, "Tổng tiền = 90000"),

        # DU: def(base_price, 18) [80k] -> use(base_price, 20); def(total_price, 20) -> use(total_price, 25); def(result, 25) -> use(result, 29)
        ("DU_base_price_80k_to_qty7", 25, 4, 2, "Tổng tiền = 400000 và thông báo tặng bắp"),

        # DU: def(base_price, 18) [80k] -> use(base_price, 20); def(total_price, 20) -> use(total_price, 27); def(result, 27) -> use(result, 29)
        ("DU_base_price_80k_to_qty10", 25, 10, 3, "Tổng tiền = 1100000 và thông báo tặng combo"),
    ])
    def test_movie_ticket_all_uses(self, du_pair_id, age, quantity, ticket_type, expected):
        """Kiem thu tat ca cac du-pairs All-Uses cho calculate_movie_ticket."""
        result = calculate_movie_ticket(age, quantity, ticket_type)
        assert result == expected

    # --------------------------------------------------------------------------
    # 2.2 All-Uses cho calculate_shipping_fee
    # Du-pairs:
    # 1. def(weight, 32) -> p-use(36), p-use(37), p-use(46), p-use(49)
    # 2. def(distance, 32) -> p-use(38), p-use(39), c-use(56), p-use(58)
    # 3. def(service_type, 32) -> p-use(40), p-use(41), c-use(54)
    # 4. def(cargo_value, 32) -> p-use(42), p-use(43), c-use(55)
    # 5. def(base_rate, 50) [5000] -> c-use(base_rate, 56)
    # 6. def(base_rate, 52) [7000] -> c-use(base_rate, 56)
    # 7. def(service_surcharge, 54) -> c-use(service_surcharge, 56)
    # 8. def(insurance_fee, 55) -> c-use(insurance_fee, 56)
    # 9. def(base_total, 56) -> c-use(base_total, 59), c-use(base_total, 61)
    # 10. def(total_price, 59) -> c-use(total_price, 63)
    # 11. def(total_price, 61) -> c-use(total_price, 63)
    # 12. def(result, 45) -> c-use(result, 65)
    # 13. def(result, 47) -> c-use(result, 65)
    # 14. def(result, 63) -> c-use(result, 65)
    # --------------------------------------------------------------------------
    @pytest.mark.parametrize("du_pair_id, weight, distance, service_type, cargo_value, expected", [
        # DU: def(result, 45) -> use(result, 65)
        ("DU_result_def45_use65", -1.0, 10.0, 1, 10, "INVALID"),

        # DU: def(result, 47) -> use(result, 65)
        ("DU_result_def47_use65", 35.0, 10.0, 1, 10, "Quá tải trọng"),

        # DU: def(base_rate, 50) [5k] -> c-use(56)
        #     def(service_surcharge, 54) -> c-use(56)
        #     def(insurance_fee, 55) -> c-use(56)
        #     def(base_total, 56) -> c-use(59) [distance <= 20]
        #     def(total_price, 59) -> c-use(63)
        #     def(result, 63) -> c-use(65)
        ("DU_base_rate_5k_dist_short", 3.0, 10, 2, 5, "tổng tiền = 140000"),

        # DU: def(base_rate, 50) [5k] -> c-use(56)
        #     def(base_total, 56) -> c-use(61) [distance > 20]
        #     def(total_price, 61) -> c-use(63)
        #     def(result, 63) -> c-use(65)
        ("DU_base_rate_5k_dist_long", 3.0, 30, 2, 5, "tổng tiền = 300000"),

        # DU: def(base_rate, 52) [7k] -> c-use(56)
        #     def(base_total, 56) -> c-use(59) [distance <= 20]
        #     def(total_price, 59) -> c-use(63)
        #     def(result, 63) -> c-use(65)
        ("DU_base_rate_7k_dist_short", 15.0, 10, 3, 10, "tổng tiền = 230000"),

        # DU: def(base_rate, 52) [7k] -> c-use(56)
        #     def(base_total, 56) -> c-use(61) [distance > 20]
        #     def(total_price, 61) -> c-use(63)
        #     def(result, 63) -> c-use(65)
        ("DU_base_rate_7k_dist_long", 15.0, 40, 3, 10, "tổng tiền = 600000"),
    ])
    def test_shipping_fee_all_uses(self, du_pair_id, weight, distance, service_type, cargo_value, expected):
        """Kiem thu tat ca cac du-pairs All-Uses cho calculate_shipping_fee."""
        result = calculate_shipping_fee(weight, distance, service_type, cargo_value)
        assert result == expected
