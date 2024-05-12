# Get files in the destination folder and sort them on the NAS, moving files with dates to the correct folder.
import os, sys, configparser
from dateutil import parser

# read the input, output, and destination paths from the file
config = configparser.RawConfigParser()
config.read_file(open(r'filepaths.cfg'))
destination = config.get('Filepaths', 'destination')

# class to manage sorting files in the destination folder
class Sorter:
    moveCount = 0
    
    def __init__(self, destination):
        self.destination = destination

    def check_destination(self):
        if not os.path.exists(self.destination):
            print(f'Error: {self.destination} does not exist<br>')
            sys.exit(1)

    def sort_files(self):
        # get files in the destination folder
        destinationFiles = os.listdir(self.destination)
        print(f"Files in destination: {destinationFiles}<br>")

        for file in destinationFiles:
            if file:
                print(f"File has a date: {file}<br>")
                # get the date from the file name
                date = parser.parse(file, fuzzy=True)
                print(f"Date: {date}<br>")
                # create the folder path
                folderPath = f'{self.destination}/{date}'
                # check if the folder exists
                if not os.path.exists(folderPath):
                    print(f"Creating folder: {folderPath}<br>")
                    os.makedirs(folderPath)
                # move the file to the folder
                print(f"Moving file: {file} to {folderPath}<br>")
                os.rename(f'{self.destination}/{file}', f'{folderPath}/{file}')
                self.moveCount += 1


# create a sorter object
sorter = Sorter(destination)
# check to see if the destination folder exists
sorter.check_destination()
# sort the files in the destination folder
sorter.sort_files()
# print a message
print(f"Files sorted: {sorter.moveCount}<br>")
