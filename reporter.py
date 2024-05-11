from flask import Flask, render_template
import os

# Python Flask application that serves the web page and handles the API requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/import')
def imp():
    command = "python3 importer.py"
    out = os.popen(command).read()
    return (out)

if __name__ == '__main__':
    app.run()