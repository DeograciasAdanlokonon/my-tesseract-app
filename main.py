from flask import Flask, render_template, jsonify
# import our OCR function
from PIL import Image
import pytesseract
import os

image = Image.open('image.jpg')
# Perform OCR using pytesseract
result = pytesseract.image_to_string(image)

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"response": {"text": result}}), 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
