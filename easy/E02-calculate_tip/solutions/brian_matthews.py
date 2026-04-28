
def calculate_tip(bill: float, tip_percent: float, people: int) -> dict:
    if bill <= 0:
        raise ValueError('bill must be greater than 0')

    if people <= 0:
        raise ValueError('people must be greater than 0')

    if not (0 <= tip_percent <= 100):
        raise ValueError('The percentage must be between 0 and 100.')

    total_tip        = round(bill * tip_percent / 100, 2)
    tip_per_person   = round(total_tip / people, 2)
    total_pay_person = round((bill / people) + tip_per_person, 2)
    total_account    = round(bill + total_tip, 2)

    return {"tip_total": total_tip, "tip_per_person": tip_per_person, "bill_per_person": total_pay_person, "total": total_account}

print(calculate_tip(50.0, -15.0, 4))