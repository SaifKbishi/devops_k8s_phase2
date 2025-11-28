# app.py
print("hello from multistage docker")
from flask import Flask, jsonify, render_template


app = Flask(__name__)

@app.route('/')
def home():
    #return "Hello from Flask in Docker! while trying helm from VSCode"
    return render_template('index.html' )

@app.route('/images')
def images():
    image_filename = "hikemoreworryless.jpg"
    return render_template('images_page.html', image_filename=image_filename)

@app.route('/health')
def health():
    return render_template('health.html' )

@app.route('/about')
def about():
    return render_template('about.html' )

@app.route('/api/data')
def get_data():    
    sample_data = {
        "name": "Flask App",
        "version": "1.0",
        "status": "Running"
    }
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)