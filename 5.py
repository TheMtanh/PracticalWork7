class FitnessCenter:
    def __init__(self, client_code, year, month, duration):
        self.client_code = client_code
        self.year = year
        self.month = month
        self.duration = duration


sessions = [
    FitnessCenter("A001", 2023, 1, 60),
    FitnessCenter("B002", 2023, 2, 90),
    FitnessCenter("C003", 2022, 3, 120),
    FitnessCenter("D004", 2023, 4, 45),
    FitnessCenter("E005", 2022, 5, 75),
    FitnessCenter("F006", 2023, 6, 90),
    FitnessCenter("G007", 2024, 1, 60),
    FitnessCenter("H008", 2022, 2, 180),
    FitnessCenter("I009", 2024, 3, 45),
    FitnessCenter("J010", 2023, 4, 120)
]

yearly_duration = {}
for session in sessions:
    yearly_duration[session.year] = yearly_duration.get(session.year, 0) + session.duration

max_year = None
max_duration = 0

for year, total in yearly_duration.items():
    if total > max_duration or (total == max_duration and year < max_year):
        max_duration = total
        max_year = year

print(f"Год с наибольшей продолжительностью: {max_year}")
print(f"Общая продолжительность: {max_duration} минут")