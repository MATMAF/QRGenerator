import tkinter as tk
import qrcode
from io import BytesIO

def generate_qr_code():
    url = url_entry.get()
    if url:
        qr = qrcode.QRCode(version=2, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="#FFFFFF", back_color="#344955")
        img_data = BytesIO()
        img.save(img_data, format="PNG")
        qr_code_image = tk.PhotoImage(data=img_data.getvalue())
        qr_label.config(image=qr_code_image)
        qr_label.image = qr_code_image

# Create the main application window
root = tk.Tk()
root.title("QRGenerator")
root.geometry("500x400")
root.configure(bg="#344955")

# Create a Label and Entry widget to enter the URL
url_label = tk.Label(root, text="Enter URL:")
url_label.pack(pady=10)
url_label.config(fg="#F9AA33", bg="#344955")
url_entry = tk.Entry(root)
url_entry.pack()
url_entry.config(bg="#232F34", fg="#FFFFFF")

# Create a Button to generate the QR code
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack(pady=10)
generate_button.config(bg="#F9AA33", fg="#4A6572")

# Create a Label to display the QR code
qr_label = tk.Label(root)
qr_label.pack()
qr_label.config(bg="#344955")

# Start the main event loop
root.mainloop()