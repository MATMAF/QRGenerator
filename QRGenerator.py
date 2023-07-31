import tkinter as tk
import qrcode
from io import BytesIO
import pyglet
import os
import shutil
import sys

def generate_qr_code():
    url = url_entry.get()
    if url:
        qr = qrcode.QRCode(version=2, box_size=10, border=2)
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="#FFFFFF", back_color="#344955")
        img_data = BytesIO()
        img.save(img_data, format="PNG")
        qr_code_image = tk.PhotoImage(data=img_data.getvalue())
        qr_label.config(image=qr_code_image)
        qr_label.image = qr_code_image
        download_button.pack(pady=10)

def download_qr_code():
    url = url_entry.get()
    if url:
        qr = qrcode.QRCode(version=2, box_size=10, border=2)
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="#111111", back_color="#FFFFFF")
        img_data = "qrcode.png"
        img.save(img_data, format="PNG")
    
    download_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    shutil.move("qrcode.png", download_folder)
    download_label.pack(pady=10)

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Add font
font_path = resource_path("src/Nunito.ttf")
pyglet.font.add_file(font_path)

# Create the main application window
root = tk.Tk()
root.title("QRGenerator")
icon_path = resource_path("src/icon.ico")
root.iconbitmap(icon_path)
root.geometry("500x500")
root.configure(bg="#344955")

# Create a Label and Entry widget to enter the URL
url_label = tk.Label(root, text="Enter URL:", font=("Nunito", 10))
url_label.pack(pady=10)
url_label.config(fg="#F9AA33", bg="#344955")
url_entry = tk.Entry(root, font=("Nunito", 10))
url_entry.pack()
url_entry.config(bg="#232F34", fg="#FFFFFF")

# Create a Button to generate the QR code
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code, font=("Nunito", 10))
generate_button.pack(pady=10)
generate_button.config(bg="#F9AA33", fg="#4A6572")

# Create a Label to display the QR code
qr_label = tk.Label(root)
qr_label.pack()
qr_label.config(bg="#344955")

# Create a Button to download the QR code
download_button = tk.Button(root, text="Download QR Code", command=download_qr_code, font=("Nunito", 10))
download_button.pack(pady=10)
download_button.config(bg="#F9AA33", fg="#4A6572")
download_button.pack_forget()

# Create a Label to display QR Code Downloaded
download_label = tk.Label(root, text="QR Code Downloaded", font=("Nunito", 10))
download_label.pack(pady=10)
download_label.config(fg="#F9AA33", bg="#344955")
download_label.pack_forget()

# Start the main event loop
root.mainloop()