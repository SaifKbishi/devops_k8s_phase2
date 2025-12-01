# app.py
print("hello from multistage docker")
from flask import Flask, jsonify, render_template
import os


app = Flask(__name__)

@app.route('/')
def home():
    #return "Hello from Flask in Docker! while trying helm from VSCode"
    #my_variable = os.getenv('hello_from_configmap', 'Default Value')
    my_variable = os.getenv('hello_from_configmap', 'Default Value3')
    print(os.getenv("GREETINGS_IN_THE_BODY"))
    print(my_variable)
    print(os.getenv("hello_from_configmap"))
    return render_template('index.html', my_variable=my_variable )
    #return render_template('index.html')

@app.route('/images')
def images():
    image_filename = "hikemoreworryless.jpg"
    return render_template('images_page.html', image_filename=image_filename)

@app.route('/health')
def health():
    status = "Healthy"
    #return jsonify(status="healthy"), 200
    #return render_template('health.html', status=status )
    return render_template('health.html')

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