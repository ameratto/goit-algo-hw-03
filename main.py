from datetime import datetime, date
import random
from typing import Any
import re


# Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
# У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
# Для роботи з датами слід використовувати модуль datetime Python.
def get_days_from_today(user_date: str):
    today = date.today().toordinal()
    corrected_date_format = re.findall(r'\d+', re.sub(r'[-./]', " ", user_date))
    match corrected_date_format:
        case [y, m, d] if len(y) == 4 and (len(m) == 2 and int(m) <= 12) and len(d) == 2:
            # print("format: YYYY MM DD")
            return date(year=int(y), month=int(m), day=int(d)).toordinal() - today
        case [y, d, m] if len(y) == 4 and len(d) == 2 and (len(m) == 2 and int(m) <= 12):
            # print("format: YYYY DD MM")
            return date(year=int(y), month=int(m), day=int(d)).toordinal() - today
        case [d, m, y] if len(d) == 2 and (len(m) == 2 and int(m) <= 12) and len(y) == 4:
            # print("format: DD MM YYYY")
            return date(year=int(y), month=int(m), day=int(d)).toordinal() - today
        case [m, d, y] if (len(m) == 2 or int(m) <= 12) and len(d) == 2 and len(y) == 4:
            # print("format: MM DD YYYY")
            return date(year=int(y), month=int(m), day=int(d)).toordinal() - today
        case _:
            return None


def get_numbers_ticket(val_max: int, val_min: int, val_quantity: int) -> list[Any]:
    set_of_numbers = set()
    if val_min < 1 or val_max > 1000:
        print(f"Невірне значення параметра min або max: {val_min if val_min <= 0 else val_max}")
        return list()
    while len(set_of_numbers) < val_quantity:
        set_of_numbers.add(random.randint(val_min, val_max))
    return sorted(list(set_of_numbers))


def normalize_phone(phone_number: str):
    normalize_phone_number = re.findall(r"\d{10}$", re.sub(r'\D+', '', phone_number))
    return '+38' + normalize_phone_number[0]
    # match phone_code:
    #     case 'ukr':
    #         return '+38' + phone_number
    #     case 'jp':
    #         return '+81' + phone_number
    #     case 'en':
    #         return '+1264' + phone_number
    #     case _:
    #         return phone_number


desired_dates = ["2026-07-11",
                 "2026/07/11",
                 "2026/11/07",
                 "11/07/2026",
                 "07/11/2026"]
# print("Завдання 1:")
# for desired_date in desired_dates:
#     print(f"Результат виконання функції get_days_from_today : \n\
#     Кількість днів від сьогоднішньої дати {date.today()} до вказаної {desired_date} = \
#     {get_days_from_today(desired_date)}")

# ----- #

var_min = 5
var_max = 1560
quantity = 5
print("Завдання 2:")
print(f"Результат виконання функції get_numbers_ticket з наступними параметрами var_min = {var_min}, var_max = {var_max}, quantity = {quantity}: \n\
{get_numbers_ticket(var_max, var_min, quantity)}")

# ----- #

phone_number_strings = ["    +38(050)123-32-34",
                        "     0503451234",
                        "(050)8889900",
                        "38050-111-22-22",
                        "38050 111 22 11   "]
# print("Завдання 3:")
# for number in phone_number_strings:
#     print(f"{normalize_phone(number)}")
