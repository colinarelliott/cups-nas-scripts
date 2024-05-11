#imports files, sends them to output, then moves them to destination
import os, subprocess, sys
from fileManager import FileManager as fileManager
from colouredPrint import textColour as tc

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
print(f"{tc.YELLOW}Files in inputPath: {tc.ENDC}{tc.CYAN}{inputFiles}{tc.ENDC}")

# if no files to process, exit
if (len(inputFiles) == 0):
    print(f"{tc.BOLD} {tc.RED}No files to process, exiting.{tc.ENDC}")
    sys.exit(0)

# loop through all the files and use filemanager class to process each into an mp4 then send to output
for file in inputFiles:
    print(f'{tc.BLUE}Processing file: {tc.CYAN}[{file}]{tc.ENDC}')
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

# check for the files in the destination path, remove matching files in the input (CLEANUP)
inputFiles = os.listdir(inputPath)
destinationFiles = os.listdir(destination)
for file in destinationFiles:
    if file in inputFiles:
        print(f"{tc.ORANGE}CLEANUP: Removing file {file} from inputPath {tc.ENDC}")
        os.remove(f'{inputPath}/{file}')