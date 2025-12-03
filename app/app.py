# app.py
print("hello from multistage docker")
from flask import Flask, jsonify, render_template, render_template_string
import os


app = Flask(__name__)

is_alive = True
is_ready = False


@app.route('/')
def home():
    #return "Hello from Flask in Docker! while trying helm from VSCode"
    my_variable = os.getenv('hello_from_configmap', 'Default Value')
    #hello_from_configmap01 = os.getenv('hello_from_configmap', 'Sorry could not get hello_from_configmap')
    hello_from_configmap01 = os.getenv('HELLO_FROM_CONFIGMAP', 'Sorry could not get hello_from_configmap')    
    greetings_in_the_body02 = os.getenv('greetings_in_the_body', 'Sorry could not get greetings_in_the_body')
    print(os.getenv('hello_from_configmap', 'Sorry could not get hello_from_configmap in print'))
    #return render_template('index.html', my_variable01=hello_from_configmap01, my_variable02=greetings_in_the_body02)
    return render_template('index.html', my_variable=my_variable)

@app.route('/images')
def images():
    image_filename = "hikemoreworryless.jpg"
    return render_template('images_page.html', image_filename=image_filename)

@app.route('/health')
def health():
    return render_template('health.html', status="Ok" ) if is_alive else render_template('health.html', status="NOT OK"), 200 if is_alive else 500

@app.route('/ready')
def ready():
    return render_template('ready.html', status="READY" ) if is_alive else render_template('ready.html', status="NOT READY"), 200 if is_alive else 500    

@app.route('/about')
def about():
    return render_template('about.html' )


from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/health2')
def health2():
    try:
        with open('/data/health-check.log', 'r') as f:
            logs = f.readlines()
    except FileNotFoundError:
        logs = ["No health check logs found."]
    
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Health Check Results</title>
        <style>
            body { font-family: Arial; margin: 20px; }
            h1 { color: #2c3e50; }
            pre { background: #f4f4f4; padding: 10px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>Health Check Results</h1>
        <pre>{{ logs }}</pre>
    </body>
    </html>
    """
    return render_template_string(html_template, logs="".join(logs))


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