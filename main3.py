import string as s
text = input("Введіть повідомлення: ")
print("Маленький регістр:" + text.lower())
print("Великий регістр:" + text.upper())
print("Велика перша літера:" + text.capitalize())
print("Довжина рядка: "+str(len(text)))
print("Перший символ: "+text[0])
print("Заміна (видалення пробілу):" + text.replace("", ""))
print("Рядок з цифрами: " + s.digits)

print("Рядок з малими літерами:" + s.ascii_lowercase)
print("Рядок з великими літерами:" + s.ascii_uppercase)
