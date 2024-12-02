import requests
from tkinter import Tk, Label
from PIL import Image, ImageTk
from io import BytesIO

def main():
    response = requests.get("https://api.bigdatacloud.net/data/reverse-geocode-client")
    data = response.json()
    country_name = data.get("countryName", "Не вдалося отримати дані")
    
    image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a3/June_odd-eyed-cat_cropped.jpg"
    image_response = requests.get(image_url)
    image_data = Image.open(BytesIO(image_response.content))

    root = Tk()
    root.title("Інформація з API та зображення")
    root.geometry("400x400")

    label_text = Label(root, text=f"Назва країни: {country_name}", font=("Arial", 14))
    label_text.pack(pady=20)

    img = ImageTk.PhotoImage(image_data.resize((200, 200)))
    label_image = Label(root, image=img)
    label_image.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
