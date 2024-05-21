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
    out = []
    out.append(os.popen(command).read())
    return render_template('output.html', files=out)

@app.route('/import')
def imp():
    command = "python3 importer.py"
    out = []
    out.append(os.popen(command).read())
    return render_template('output.html', files=out)

@app.route('/input')
def input():
    # if the input file is a directory, process accordingly
    inputFiles = [ ]
    for path, folders, files in os.walk(inputPath):
        for filename in files:
            inputFiles.append("FILE: "+filename)
        for folder_name in folders:
            inputFiles.append("DIR: "+folder_name + " ↓")
            files = os.listdir(f"{path}/{folder_name}")
            for filename in files:
                inputFiles.append('   '+filename)
        break
    if (len(inputFiles) == 0):
        inputFiles = ["No files to process"]
    return render_template('index.html', files=inputFiles)

@app.route('/output')
def output():
    outputFiles = []
    for path, folders, files in os.walk(outputPath):
        for filename in files:
            outputFiles.append("FILE: "+filename)
        for folder_name in folders:
            outputFiles.append("DIR: "+folder_name + " ↓")
            files = os.listdir(f"{path}/{folder_name}")
            for filename in files:
                outputFiles.append('   '+filename)
        break
    if (len(outputFiles) == 0):
        outputFiles = ["No files in output directory"]
    return render_template('index.html', files=outputFiles)

@app.route('/destination')
def dest():
    destinationFiles = []
    for path, folders, files in os.walk(destination):
        for filename in files:
            destinationFiles.append("FILE: "+filename)
        for folder_name in folders:
            destinationFiles.append("DIR: "+folder_name + " ↓")
            files = os.listdir(f"{path}/{folder_name}")
            for filename in files:
                destinationFiles.append('FILE: '+filename)
        break
    if (len(destinationFiles) == 0):
        destinationFiles = ["No files in destination directory"]
    return render_template('index.html', files=destinationFiles)

@app.route('/sort')
def sort():
    command = "python3 sorter.py"
    out = []
    out.append(os.popen(command).read())
    return render_template('output.html', files=out)

@app.route('/delete_input')
def delete_input():
    command = f"rm -rf {outputPath}/*"
    out = []
    out.append("Success. Files in /input have been deleted.")
    return render_template('output.html', files=out)

@app.route('/delete_output')
def delete_output():
    command = f"rm -rf {outputPath}/*"
    out = []
    out.append("Success. Files in /output have been deleted.")
    return render_template('output.html', files=out)

if __name__ == '__main__':
    app.run()