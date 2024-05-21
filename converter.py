#imports files, sends them to output, then moves them to destination
import os, subprocess, sys
from src.fileManager import FileManager as fileManager
from src.colouredPrint import textColour as tc
import configparser

# check for the argument passed to the script
outputType = sys.argv[1]

# read the input, output, and destination paths from the file
config = configparser.RawConfigParser()
config.read_file(open(r'filepaths.cfg'))
inputPath = config.get('Filepaths', 'inputPath')
outputPath = config.get('Filepaths', 'outputPath')
destination = config.get('Filepaths', 'destination')

# loop through all the files and use filemanager class to process each into an mp4 then send to output
def processfiles_cmd():
    # find all the files in the inputPath
    inputFiles = os.listdir(inputPath)
    print(f"{tc.YELLOW}Files in inputPath: {tc.ENDC}{tc.CYAN}{inputFiles}{tc.ENDC}")

    # if no files to process, exit
    if (len(inputFiles) == 0):
        print(f"{tc.BOLD}{tc.RED}No files to process, exiting.{tc.ENDC}")
        sys.exit(0)

    # loop through all the files in the inputPath
    for file in inputFiles:
        print(f'{tc.BLUE}CMD | Processing file: {tc.CYAN}[{file}]{tc.ENDC}')
        # set the input and output file paths
        input_file = f'{inputPath}/{file}'
        output_file = f'{outputPath}/{file}'
        # create a file manager object
        file_manager = fileManager(input_file, output_file)
        print(f"{tc.PURPLE}FileManager created for file: {tc.CYAN}[{file}]{tc.ENDC}")
        # check to see if input file exists
        file_manager.check_input_file()
        print(f"{tc.GREEN}Input file exists. {tc.ENDC}")
        # check to see if output file exists
        file_manager.check_output_file()
        print(f"{tc.GREEN}Output file does not already exist.{tc.ENDC}")
        # run ffmpeg to convert the file
        file_manager.run_ffmpeg()
        print(f"{tc.PINK}FFMPEG conversion complete!{tc.ENDC}")
        # move the file to the destination
        subprocess.run(f'mv {output_file} {destination}/{file}', shell=True)
        print(f"{tc.GREEN}File moved to destination.{tc.ENDC}")

        inputFiles = os.listdir(inputPath)
        destinationFiles = os.listdir(destination)
        for file in destinationFiles:
            if file in inputFiles:
                print(f"{tc.YELLOW}CLEANUP: Removing file {file} from inputPath.{tc.ENDC}")
                os.remove(f'{inputPath}/{file}')

def processfiles_web():
    # find all the files in the inputPath
    inputFiles = os.listdir(inputPath)
    print(f"Files in inputPath: {inputFiles}")

    # if no files to process, exit
    if (len(inputFiles) == 0):
        print(f"No files to process, exiting.")
        sys.exit(0)

    for file in inputFiles:
        print(f'WEB: Processing file: [{file}]')
        # set the input and output file paths
        input_file = f'{inputPath}/{file}'
        output_file = f'{outputPath}/{file}'
        # create a file manager object
        file_manager = fileManager(input_file, output_file)
        print(f"FileManager created for file: [{file}]")
        # check to see if input file exists
        file_manager.check_input_file()
        print(f"Input file exists.")
        # check to see if output file exists
        file_manager.check_output_file()
        print(f"Output file does not already exist.")
        # run ffmpeg to convert the file
        file_manager.run_ffmpeg()
        print(f"FFMPEG: conversion complete!")
        # move the file to the destination
        subprocess.run(f'mv "{output_file}" "{destination}/{file}"', shell=True)
        print(f"File moved to destination: {destination}/{file}")

        # check for the files in the destination path, remove matching files in the input (CLEANUP)
        inputFiles = os.listdir(inputPath)
        destinationFiles = os.listdir(destination)
        for file in destinationFiles:
            if file in inputFiles:
                print(f"CLEANUP: Removing file {file} from inputPath.")
                os.remove(f'{inputPath}/{file}')

# run one of two loops depending on the output type
if outputType == "cmd":
    processfiles_cmd()
elif outputType == "web":
    processfiles_web()

