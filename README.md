# QR Code Generator

This is a simple Python script that generates a QR code from a website link and saves it as an image file. You can use it to quickly create QR codes for URLs and share them easily.

## Features
- Converts any website link into a QR code.
- Saves the QR code as an image file.
- Supports customization of QR code size and error correction.

## Prerequisites
Make sure you have Python installed on your system. You also need to install the required dependency:
```
pip install qrcode[pil]
```

## Usage
1. Clone this repository or copy the script.
2. Run the script using Python.

```
import qrcode
```
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

# Example usage
website_link = "https://example.com"
generate_qr_code(website_link, "website_qr.png")


3. Run the script:
```
python script.py
```
4. The generated QR code image (`website_qr.png`) will be saved in the current directory.

## Customization
You can modify the script to:
- Change the QR code colors by adjusting `fill` and `back_color`.
- Modify the QR code size using the `box_size` and `border` parameters.
- Improve error correction by setting `error_correction=qrcode.constants.ERROR_CORRECT_H` for better fault tolerance.
---
## Example Output
After running the script, you'll get an image file (`website_qr.png`) that looks like this:

![QR Code Example](example_qr.png)




