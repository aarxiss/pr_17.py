from datetime import date, datetime

class UkrainianCalendar:
    def __init__(self):
        self.holidays = [
            date(2025, 1, 1),   # Новий рік
            date(2025, 1, 7),   # Різдво (за Юліанським календарем)
            date(2025, 3, 8),   # Міжнародний жіночий день
            date(2025, 4, 20),  # Пасха (припустимо, 2025-04-20)
            date(2025, 5, 1),   # День праці
            date(2025, 5, 9),   # День перемоги
            date(2025, 6, 28),  # День Конституції
            date(2025, 8, 24),  # День Незалежності
            date(2025, 10, 14), # День захисників і захисниць України
        ]

    def get_holiday_list(self):
        return self.holidays

    def is_working_day(self, input_date):
        if isinstance(input_date, str):
            input_date = datetime.strptime(input_date, "%Y-%m-%d").date()
        return input_date.weekday() < 5 and input_date not in self.holidays
