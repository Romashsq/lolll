def multiply_numbers(a, b):
    return a * b


try:
    num1 = float(input("введіть перше число: "))
    num2 = float(input("введіть друге число: "))
    result = multiply_numbers(num1, num2)
    print(f"Результат {num1} і {num2}: {result}")
except ValueError:
    print("Будь ласка, введіть коректні числа.")
