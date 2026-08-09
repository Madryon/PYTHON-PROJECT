import qrcode

data = input("Enter URL or text to encode into QR code: ")
file_name = input("Enter output filename (e.g. my_qr.png): ")

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(file_name)

print(f"QR code successfully created and saved as {file_name}")
