#imports files, sends them to output, then moves them to destination
import os, subprocess, sys 
from fileManager import FileManager as fileManager

#TESTING PATHS
inputPath = "input"
outputPath = "output"
destination = "destination"

# PRODUCTION
#inputPath = "/mnt/z/INPUT"
#outputPath = "/mnt/z/OUTPUT"
#destination = "/mnt/y/_RECORDINGS/TEMP"

# find all the files in the inputPath
inputFiles = os.listdir(inputPath)
print("Files in inputPath: ", inputFiles)

# if no files to process, exit
if (len(inputFiles) == 0):
    print("No files to process, exiting")
    sys.exit(0)

# loop through all the files and use filemanager class to process each into an mp4 then send to output
for file in inputFiles:
    print(f'Processing file: {file}')
    input_file = f'{inputPath}/{file}'
    output_file = f'{outputPath}/{file}'
    file_manager = fileManager(input_file, output_file)
    print("FileManager created for file: " + file)
    file_manager.check_input_file()
    print("Checked input file")
    file_manager.check_output_file()
    print("Checked output file")
    file_manager.run_ffmpeg()
    print("FFMPEG conversion complete!")
    # move the file to the destination
    subprocess.run(f'mv {output_file} {destination}/{file}', shell=True)
    print("File moved to destination")

# check for the files in the output path, remove matching files in the input path (CLEANUP)
outputFiles = os.listdir(outputPath)
for file in outputFiles:
    if file in inputFiles:
        os.remove(f'{inputPath}/{file}')

# check for the files in the destination path, remove matching files in the input (CLEANUP)
inputFiles = os.listdir(inputPath)
destinationFiles = os.listdir(destination)
for file in destinationFiles:
    if file in inputFiles:
        os.remove(f'{inputPath}/{file}')