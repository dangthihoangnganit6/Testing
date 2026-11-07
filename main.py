def calculate_movie_ticket(age, quantity, ticket_type):
    result = ""

    if (
        (age < 1) 
        or (age > 100) 
        or (quantity < 1)
        or (quantity > 10) 
        or (ticket_type < 1) 
        or (ticket_type > 3)):
        result = "INVALID"
    elif age < 18:
        result = "Không đủ tuổi"
    else:
        if age <= 22:
            base_price = 50000
        else:
            base_price = 80000

        total_price = quantity * (base_price + ticket_type * 10000)

        if quantity <= 3:
            result = f"Tổng tiền = {total_price}"
        elif quantity <= 7:
            result = f"Tổng tiền = {total_price} và thông báo tặng bắp"
        else:
            result = f"Tổng tiền = {total_price} và thông báo tặng combo"

    return result


def calculate_shipping_fee(weight, distance, service_type, cargo_value):
    result = ""

    if (
        (weight < 0.1)
        or (weight > 50.0)
        or (distance < 1.0)
        or (distance > 50.0)
        or (service_type < 1)
        or (service_type > 3)
        or (cargo_value < 0)
        or (cargo_value > 100)
    ):
        result = "INVALID"
    elif weight > 30.0:
        result = "Quá tải trọng"
    else:
        if weight <= 5.0:
            base_rate = 5000
        else:
            base_rate = 7000

        service_surcharge = service_type * 2000
        insurance_fee = cargo_value * 10000
        base_total = distance * (base_rate + service_surcharge) + insurance_fee

        if distance <= 20.0:
            total_price = base_total
        else:
            total_price = base_total - 20000

        result = f"tổng tiền = {total_price}"

    return result