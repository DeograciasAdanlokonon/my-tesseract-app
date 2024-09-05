from flask import Flask, render_template
# import our OCR function
from PIL import Image
import pytesseract
import os

image = Image.open('image.jpg')
# Perform OCR using pytesseract
text = pytesseract.image_to_string(image)

app = Flask(__name__)


@app.route('/')
def home():
    return f'<h3>{text}</h3>'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
