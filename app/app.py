# app.py
from flask import Flask, jsonify, render_template, request, send_file, abort
import os
from collections import deque

app = Flask(__name__)
LOG_PATH = "/data/health-check.log"
is_alive = True
is_ready = False

@app.route('/')
def home():
    my_variable = os.getenv('hello_from_configmap', 'Default Value')
    hello_from_configmap01 = os.getenv('HELLO_FROM_CONFIGMAP', 'Sorry could not get hello_from_configmap')
    greetings_in_the_body02 = os.getenv('greetings_in_the_body', 'Sorry could not get greetings_in_the_body')
    return render_template('index.html', my_variable=my_variable)

@app.route('/images')
def images():
    image_filename = "hikemoreworryless.jpg"
    return render_template('images_page.html', image_filename=image_filename)

@app.route('/health')
def health():
#    return jsonify(status = "alive"), 200
    return render_template('health.html', status="Ok" ) if is_alive else render_template('health.html', status="NOT OK"), 200 if is_alive else 500

@app.route('/ready')
def ready():
    return render_template('ready.html', status="READY" ) if is_alive else render_template('ready.html', status="NOT READY"), 200 if is_alive else 500    

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

HEALTH_HTML_PATH = "/data/health.html"

@app.route('/health2')
def health2():
    if os.path.exists(HEALTH_HTML_PATH):
        # Return as HTML
        return send_file(HEALTH_HTML_PATH, mimetype="text/html")
    else:
        # Not ready yet (e.g., first CronJob hasn’t run)
        abort(404, description="Report not generated yet. Wait for the next CronJob run.")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008, debug=True)