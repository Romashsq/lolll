number = input("Введіть число: ")

if number.isdigit():
    number = int(number)
    is_prime = True

    if number < 2:
        is_prime = False
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
    if is_prime:
        print(f"{number} є простим числом.")
    else:
        print(f"{number} не є простим числом.")
else:
    print(f"Ви ввели не ціле число... {number}")
