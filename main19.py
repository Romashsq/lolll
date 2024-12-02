import os
import time

def main():
    print("Запускаємо процес (блокнот)...")
    if os.name == "nt":
        os.system("notepad.exe")
    else:
        os.system("gedit")
    
    print("Затримка 5 секунд...")
    time.sleep(5)
    
    print("Відкриваємо веб-сторінку...")
    if os.name == "nt":
        os.system("start https://www.python.org")
    elif os.name == "posix":
        os.system("xdg-open https://www.python.org")

if __name__ == "__main__":
    main()