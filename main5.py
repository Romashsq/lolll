from datetime import datetime as dt

current_date = dt.now()

print(f"Поточна дата і час: {current_date}")
print(f"Поточна дата: {current_date.date()}")
print(f"Поточний рік: {current_date.year}")
print(f"Поточний місяць: {current_date.month}")
print(f"Поточний день: ({current_date.day}")
print(f"Поточний час: {current_date.time()}")
print(f"Поточна година: {current_date.hour}")
print(f"Поточні хвилини: ({current_date.minute}")
print(f"Поточні секунди: {current_date.second}")

birthdate_input = input("Введіть дату народження (дд. мм. pppp): ")
birth_date = dt.strptime(birthdate_input, "%d.%m.%Y")

average_days_per_year = 365.2425
age = int((current_date - birth_date).days / average_days_per_year)
print(f"Bam вік: {age} років")
