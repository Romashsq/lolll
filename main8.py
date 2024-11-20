n = 4
for i in range(1, 11):
    result = n * i
    print(f"{n} x {i} = {result}")

# Задание 2: Подсчет количества цифр в числе 44444
number = 44444
count = 0
while number > 0:
    number //= 10
    count += 1
print(f"Количество цифр в вашем числе: {count}")
