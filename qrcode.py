import qrcode

def generate_upi_qr_code(upi_id, amount, description):
    # Combine UPI details
    upi_string = f"upi://pay?pa={upi_id}&mc=123&tid=321&tr={description}&tn={description}&am={amount}&cu=INR"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(upi_string)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    qr_img.save("upi_qr_code.png")

if __name__ == "__main__":
    # Replace these values with your UPI details
    upi_id = "example@upi"
    amount = "50.00"
    description = "Payment for goods"

    generate_upi_qr_code(upi_id, amount, description)

#pip install qrcode[pil]  required to install
