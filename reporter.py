# Python Flask application that serves the web page and handles the API requests
from flask import Flask, render_template
import os, configparser

# read the input, output, and destination paths from the file
config = configparser.RawConfigParser()
config.read_file(open(r'filepaths.cfg'))
inputPath = config.get('Filepaths', 'inputPath')
outputPath = config.get('Filepaths', 'outputPath')
destination = config.get('Filepaths', 'destination')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process')
def process():
    command = "python3 converter.py web"
    out = os.popen(command).read()
    return (out)

@app.route('/import')
def imp():
    command = "python3 importer.py"
    out = os.popen(command).read()
    return (out)

@app.route('/input')
def input():
    # if the input file is a directory, process accordingly
    inputFiles = [f for f in os.listdir(inputPath) if os.path.isfile(os.path.join(inputPath, f))]
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

@app.route('/sort')
def sort():
    command = "python3 sorter.py"
    out = os.popen(command).read()
    return (out)

@app.route('/delete_input')
def delete_input():
    command = f"rm -rf {inputPath}/*"
    return "Input files deleted."

@app.route('/delete_output')
def delete_output():
    command = f"rm -rf {outputPath}/*"
    out = os.popen(command).read()
    return "Output files deleted."

if __name__ == '__main__':
    app.run()