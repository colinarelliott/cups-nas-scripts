# Imports files from server to be converted and moved to destination (scans path provided in filepaths.cfg)
import os, configparser

# read the input, output, and destination paths from the file
config = configparser.RawConfigParser()
config.read_file(open(r'filepaths.cfg'))
inputPath = config.get('Importer', 'inputPath')
scanPath = config.get('Importer', 'scanPath')

# list to store files to move
filesToCheck = []
 
# Iterate over files in directory
for path, folders, files in os.walk(scanPath):
    # loose files
    for filename in files:
        filesToCheck.append(scanPath+"/"+filename)
 
    # files in folders
    for folder_name in folders:
        files = os.listdir(f"{path}/{folder_name}")
        for filename in files:
            filesToCheck.append(scanPath+"/"+folder_name+"/"+filename)
    break

# list to store valid files
validFiles = []

# Move files to inputPath
for file in filesToCheck:
    # check if the file needs to be converted somehow, and if true
    validFiles.append(file)
    print("Valid file found: ", file)

# move valid files to inputPath
for file in validFiles:
    moveFile = f'mv {file} {inputPath}'
    os.system(moveFile)
    print("File moved to inputPath: ", file)

# check if any valid files were found
if len(validFiles) == 0:
    print("No valid files found.")