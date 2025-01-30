from flask import Flask, render_template, request, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert')
def convert_page():
    return render_template('convert.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/convert', methods=['POST'])
def convert_images():
    images = request.files.getlist('images')
    
    if not images:
        return "No images uploaded", 400

    image_list = [Image.open(img).convert("RGB") for img in images]

    pdf_bytes = io.BytesIO()
    image_list[0].save(pdf_bytes, format='PDF', save_all=True, append_images=image_list[1:])
    pdf_bytes.seek(0)

    return send_file(pdf_bytes, mimetype='application/pdf', as_attachment=True, download_name="converted.pdf")

if __name__ == '__main__':
    app.run(debug=True)