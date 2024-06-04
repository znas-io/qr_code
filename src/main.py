# "https://www.swfhc.org"

import qrcode
from flask import Flask, send_file
import io

app = Flask(__name__)

# Function to generate QR code
def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    return img

# Flask route to serve the QR code
@app.route('/swfhc')
def serve_qr_code():
    url = "https://www.swfhc.org"  # Replace with your URL
    img = generate_qr_code(url)
    
    # Save the image to a BytesIO object without specifying format
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr)
    img_byte_arr.seek(0)
    
    return send_file(img_byte_arr, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
