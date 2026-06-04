from datetime import datetime, date


# Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
# Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
# У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
# Для роботи з датами слід використовувати модуль datetime Python.
def get_days_from_today(user_date: str) -> int:
    today = date.today().toordinal()
    return datetime.strptime(user_date, '%Y-%m-%d').toordinal() - today


desired_date = '2026-06-15'

print(f"Результат виконання функції get_days_from_today : \n\
Кількість днів від сьогоднішньої дати {date.today()} до вказаної {desired_date} = \
{get_days_from_today(desired_date)}")
