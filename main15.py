import os


def create_or_append_file(file_name):
    with open(file_name, "a") as file:
        text = input("Введіть текст для запису: ")
        file.write(text + "\n")
    print("Текст записано у файл.")


def read_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            content = file.read()
        print("Вміст файлу:")
        print(content)
    else:
        print("Файл не знайдено.")


def edit_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()
        print("Поточний вміст файлу:")
        for i, line in enumerate(lines, start=1):
            print(f"{i}: {line.strip()}")

        line_to_edit = int(input("Введіть номер рядка для редагування: ")) - 1
        if 0 <= line_to_edit < len(lines):
            new_text = input("Введіть новий текст для цього рядка: ")
            lines[line_to_edit] = new_text + "\n"
            with open(file_name, "w") as file:
                file.writelines(lines)
            print("Файл успішно відредаговано.")
        else:
            print("Невірний номер рядка.")
    else:
        print("Файл не знайдено.")


def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print("Файл успішно видалено.")
    else:
        print("Файл не знайдено.")


def main():
    file_name = "example.txt"

    while True:
        print("\nОберіть опцію:")
        print("1. Записати у файл")
        print("2. Прочитати файл")
        print("3. Редагувати файл")
        print("4. Видалити файл")
        print("5. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            create_or_append_file(file_name)
        elif choice == "2":
            read_file(file_name)
        elif choice == "3":
            edit_file(file_name)
        elif choice == "4":
            delete_file(file_name)
        elif choice == "5":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
