from datetime import datetime, date
import random
from typing import Any


# Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
# У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
# Для роботи з датами слід використовувати модуль datetime Python.
def get_days_from_today(user_date: str) -> int:
    today = date.today().toordinal()
    return datetime.strptime(user_date, '%Y-%m-%d').toordinal() - today

def get_numbers_ticket(val_quantity: int, val_min: int = 1, val_max: int = 1000) -> list[Any]:
    set_of_numbers = set()
    if val_min < 1 or val_max > 1000:
        print(f"Невірне значення параметра min або max: {val_min if val_min <= 0 else val_max}")
        return list()
    while len(set_of_numbers) <= val_quantity:
        set_of_numbers.add(random.randint(val_min, val_max))
    return sorted(list(set_of_numbers))

desired_date = '2026-06-15'
var_min = 1
var_max = 156
quantity = 5

# print("Завдання 1:")
# print(f"Результат виконання функції get_days_from_today : \n\
# Кількість днів від сьогоднішньої дати {date.today()} до вказаної {desired_date} = \
# {get_days_from_today(desired_date)}")

# print("Завдання 2:")
# print(f"Результат виконання функції get_numbers_ticket з наступними параметрами var_min = {var_min}, var_max = {var_max}, quantity = {quantity}: \n\
# {get_numbers_ticket(quantity, var_min, var_max)}")
