import tkinter as tk
from tkinter import messagebox


def pow_number():
    try:
        num1 = float(entry_number_1.get())
        num2 = float(entry_number_2.get())
        result = num1 ** num2
        label_result.config(text=f"Результат: {result}")
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть дійсні числа!")


root = tk.Tk()
root.title("Калькулятор ступеня")
root.geometry("300x200")
root.resizable(width=True, height=True)
root.config(bg="white")

for i in range(2):
    root.grid_rowconfigure(i, weight=1)
for i in range(2):
    root.grid_columnconfigure(i, weight=1)

label_instruction = tk.Label(
    root, text="Вхідні дані:", bg="green", fg="white", font=("Consolas", 14, "bold"))
label_instruction.grid(row=0, column=0, columnspan=2,
                       sticky="nsew", padx=10, pady=10)

entry_number_1 = tk.Entry(root)
entry_number_1.insert(0, "2")
entry_number_1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

entry_number_2 = tk.Entry(root)
entry_number_2.insert(0, "3")
entry_number_2.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

button_calculate = tk.Button(
    root, text="Піднести до степеня", command=pow_number)
button_calculate.grid(row=2, column=0, columnspan=2,
                      sticky="nsew", padx=10, pady=10)

label_result = tk.Label(root, text="Результат: ",
                        font=("Consolas", 14, "bold"))
label_result.grid(row=3, column=0, columnspan=2,
                  sticky="nsew", padx=10, pady=10)

root.mainloop()
