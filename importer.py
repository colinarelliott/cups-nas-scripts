# Imports files from server to be converted and moved to destination (scans path provided in filepaths.cfg)
import os, configparser

# read the input, output, and destination paths from the file
config = configparser.RawConfigParser()
config.read_file(open(r'filepaths.cfg'))
inputPath = config.get('Filepaths', 'inputPath')
scanPath = config.get('Filepaths', 'scanPath')

# list to store files to move
filesToCheck = []
 
# Iterate over files in directorys
for path, folders, files in os.walk(scanPath):
    # loose files
    for filename in files:
        print(f"File found: {filename}")
        filesToCheck.append(scanPath+'/'+filename)
 
    # files in folders
    for folder_name in folders:
        print(f"Folder found: {folder_name}")
        files = os.listdir(f"{path}/{folder_name}")
        for filename in files:
            print(f"File in folder {folder_name} found: {filename}")
            filesToCheck.append(scanPath+"/"+folder_name+'/'+filename)
    break

# list to store valid files
validFiles = []

# Move files to inputPath
for file in filesToCheck:
    # check if the file needs to be converted somehow, and if true
    if (file.endswith('.mp4') or file.endswith('.mov') or file.endswith('.avi')):
        print(f"Valid file found: {file}")
        validFiles.append(file)
        continue
    else:
        print(f"Invalid file found: {file}")

# move valid files to inputPath
for file in validFiles:
    moveFile = f'mv "{file}" "{inputPath}"'
    os.system(moveFile)
    print("File moved to inputPath: ", file + "")

# check if any valid files were found
if len(validFiles) == 0:
    print("No valid files found. Exiting.")