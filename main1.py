from calendar_tools import UkrainianCalendar
from datetime import date

calendar = UkrainianCalendar()

# Вивести список свят
print("Список свят:")
for holiday in calendar.get_holiday_list():
    print(holiday)

# Перевірка дат
print("\nПеревірка дати 2025-01-01:", calendar.is_working_day("2025-01-01"))  # Свято
print("Перевірка дати 2025-01-02:", calendar.is_working_day("2025-01-02"))    # Робочий день
print("Перевірка дати 2025-01-05:", calendar.is_working_day("2025-01-05"))    # Неділя
