personal_data = ("John Doe", "08.12.2007", "001044AA333")

print("Ім'я:", personal_data[0])
print("Дата народження:", personal_data[1])
print("Номер паспорта:", personal_data[2])

print("Тип даних:", type(personal_data))

student = {
    "ім'я": "Роман Бондаренко",
    "група": "2RP-10",
    "середній бал": 75.3
}

student["вік"] = 16

print("Інформація про студента:")
for key, value in student.items():
    print(f"{key}: {value}")

student["середній бал"] = 95

del student["вік"]

print("\n Оновлена інформація про студента:")
for key, value in student.items():
    print(f"{key}: {value}")
