
def validate_card(card_number: str) -> tuple[bool, str]:

    # ALGORITMO LUHN
    def algoritm_luhn(text):
        total_list = []
        list_nums  = [int(i) for i in text]

        list_nums.reverse()

        for i in range(len(list_nums)):
            if i % 2 == 0:
                total_list.append(list_nums[i])
            else:
                multi = list_nums[i] * 2
                if multi > 9:
                    multi -= 9
                total_list.append(multi)

        return sum(total_list) % 10 == 0

    if not card_number.isdecimal():
        return (False, "card number must contain only digits")

    if not 13 <= len(card_number) <= 19:
        return (False, "card number must be between 13 and 19 digits")

    if not algoritm_luhn(card_number):
        return (False, "invalid card number")

    return (True, "valid card number")

print(validate_card('4532015112830366')) # Valida
print(validate_card('4531036646')) # No valida