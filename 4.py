class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration

    def __repr__(self):
        return (f"Клиент: {self.client_code}, Год/Месяц: {self.year}/{self.month}, "
                f"Длительность: {self.duration} минут")


sessions = [
    FitnessCenter("A001", 2023, 1, 60),
    FitnessCenter("B002", 2023, 2, 90),
    FitnessCenter("C003", 2023, 3, 45),
    FitnessCenter("D004", 2023, 4, 120),
    FitnessCenter("E005", 2023, 5, 75)
]

shortest = min(sessions, key=lambda x: x.duration)
longest = max(sessions, key=lambda x: x.duration)

print("\nСамое короткое занятие:")
print(shortest)
print("\nСамое длинное занятие:")
print(longest)