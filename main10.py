try:
    result = "текст" + 5
except TypeError as e:
    print(f"Виникла помилка TypeError: {e}")
finally:
    print("Програма завершена.")
