# Python Flask application that serves the web page and handles the API requests
from flask import Flask, render_template
import os, configparser

# read the input, output, and destination paths from the file
config = configparser.RawConfigParser()
config.read_file(open(r'filepaths.cfg'))
inputPath = config.get('Importer', 'inputPath')
outputPath = config.get('Importer', 'outputPath')
destination = config.get('Importer', 'destination')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/import')
def imp():
    command = "python3 importer.py web"
    out = os.popen(command).read()
    return (out)

@app.route('/input')
def input():
    inputFiles = os.listdir(inputPath)
    if (len(inputFiles) == 0):
        inputFiles = ["No files to process"]
    return render_template('index.html', files=inputFiles)

@app.route('/output')
def output():
    outputFiles = os.listdir(outputPath)
    if (len(outputFiles) == 0):
        outputFiles = ["No files in output directory"]
    return render_template('index.html', files=outputFiles)

@app.route('/destination')
def dest():
    destinationFiles = os.listdir(destination)
    if (len(destinationFiles) == 0):
        destinationFiles = ["No files in destination directory"]
    return render_template('index.html', files=destinationFiles)

if __name__ == '__main__':
    app.run()