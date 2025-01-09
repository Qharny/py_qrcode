import qrcode

# Function to generate a QR code
def generate_qr_code(link, filename="qrcode.png"):
    
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in pixels
        border=4,  # Border size (default is 4)
    )
    qr.add_data(link)
    qr.make(fit=True)

    # Create the QR code image
    img = qr.make_image(fill="black", back_color="white")

    # Save the QR code as an image file
    img.save(filename)
    print(f"QR Code saved as {filename}")


website_link = input("Enter the website link: ")
generate_qr_code(website_link, "website_qr.png")
