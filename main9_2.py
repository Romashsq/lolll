def main():
    array = []

    while True:
        print("\nОберіть одну з опцій:")
        print("1. Додати елемент до масиву")
        print("2. Видалити елемент з масиву за індексом")
        print("3. Показати вміст масиву")
        print("4. Завершити програму")

        choice = input("Вибір: ")

        if choice == '1':
            element = input("Введіть число для додавання в масив: ")
            try:
                element = float(element)
                array.append(element)
                print(f"Число {element} успішно додано до масиву.")
            except ValueError:
                print("Будь ласка, введіть правильне число.")

        elif choice == '2':
            index = input("Введіть індекс елемента, який потрібно видалити: ")
            try:
                index = int(index)
                removed_element = array.pop(index)
                print(f"Елемент {removed_element} видалено з масиву.")
            except (ValueError, IndexError):
                print("Помилка: неправильний індекс.")

        elif choice == '3':
            print("Вміст масиву:", array)

        elif choice == '4':
            print("Програма завершена.")
            break

        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
