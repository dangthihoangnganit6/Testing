def calculate_movie_ticket(age, quantity, ticket_type):
    # Kiểm tra kiểu dữ liệu nguyên
    if not (isinstance(age, int) and isinstance(quantity, int) and isinstance(ticket_type, int)):
        return "INVALID"

    # Kiểm tra miền xác định đầu vào
    if not (1 <= age <= 100 and 1 <= quantity <= 10 and 1 <= ticket_type <= 3):
        return "INVALID"

    # Kiểm tra điều kiện độ tuổi
    if 1 <= age < 18:
        return "Không đủ tuổi"

    # Xác định đơn giá theo nhóm tuổi
    if 18 <= age <= 22:
        base_price = 50000
    else:  # 22 < age <= 100
        base_price = 80000

    # Tính tổng tiền
    total_price = quantity * (base_price + ticket_type * 10000)

    # Xác định quà tặng theo số lượng vé
    if 1 <= quantity <= 3:
        return f"tổng tiền = {total_price}"
    elif 3 < quantity <= 7:
        return f"tổng tiền = {total_price} và thông báo tặng bắp"
    else:  # 7 < quantity <= 10
        return f"tổng tiền = {total_price} và thông báo tặng combo"


def calculate_shipping_fee(weight, distance, service_type, cargo_value):
    # Kiểm tra kiểu dữ liệu
    if not (isinstance(weight, (int, float)) and isinstance(distance, (int, float))):
        return "INVALID"
    if not (isinstance(service_type, int) and isinstance(cargo_value, (int, float))):
        return "INVALID"

    # Kiểm tra miền xác định đầu vào
    if not (0.1 <= weight <= 50.0 and 1.0 <= distance <= 50.0 and 1 <= service_type <= 3 and 0 <= cargo_value <= 100):
        return "INVALID"

    # Kiểm tra giới hạn tải trọng
    if weight > 30.0:
        return "Quá tải trọng"

    # Xác định giá cước cơ bản theo khối lượng
    if weight <= 5.0:
        base_rate = 5000
    else:  # 5.0 < weight <= 30.0
        base_rate = 7000

    # Phụ thu dịch vụ và bảo hiểm
    service_surcharge = service_type * 2000
    insurance_fee = cargo_value * 10000

    # Tính tổng tiền theo khoảng cách
    base_total = distance * (base_rate + service_surcharge) + insurance_fee

    if distance <= 20.0:
        total_price = int(base_total)
    else:  # 20.0 < distance <= 50.0 (giảm 20.000 VNĐ)
        total_price = int(base_total - 20000)

    return f"tổng tiền = {total_price}"