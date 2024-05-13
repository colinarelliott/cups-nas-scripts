# Get files in the destination folder and sort them on the NAS, moving files with dates to the correct folder.
import os, sys, configparser, re

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
    
    def get_date(self, file):
        # get the date from the file name
        # searches for dates with the following formats:
        # YYYY-MM-DD, MM-DD-YYYY, MM-DD-YY, YYYY/MM/DD, MM/DD/YYYY, MM/DD/YY, YYYYMMDD, MMDDYYYY, DDMMYYYY, YYYYDDMM, (MM, DD, YYYY)
        date = ""
        date = re.search(r'\d{4}-\d{2}-\d{2}', file)
        print(f"(YYYY-MM-DD) Finding date... {date}<br>")
        if date:
            date = date.group()
        else:
            date = re.search(r'\d{2}-\d{2}-\d{4}', file)
            print(f"(MM-DD-YYYY) Finding date... {date}<br>")
            if date:
                date = date.group()
            else:
                date = re.search(r'\d{2}-\d{2}-\d{2}', file)
                print(f"(MM-DD-YY) Finding date... {date}<br>")
                if date:
                    date = date.group()
                else:
                    date = re.search(r'\d{4}/\d{2}/\d{2}', file)
                    print(f"(YYYY/MM/DD) Finding date... {date}<br>")
                    if date:
                        date = date.group()
                    else: 
                        date = re.search(r'\d{2}/\d{2}/\d{4}', file)
                        print(f"(MM/DD/YYYY) Finding date... {date}<br>")
                        if date:
                            date = date.group()
                        else: 
                            date = re.search(r'\d{2}/\d{2}/\d{2}', file)
                            print(f"(MM/DD/YY) Finding date... {date}<br>")
                            if date:
                                date = date.group()
                            else:
                                date = re.search(r'\d{2}, \d{2}, \d{4}', file)
                                print(f"(MM, DD, YYYY) Finding date... {date}<br>")
                                if date:
                                    date = re.search(r'20\d{2}', file)
                                    date = date.group()
                                else:
                                    date = re.search(r'\d{4}, \d{2}, \d{2}', file)
                                    print(f"(YYYY, MM, DD) Finding date... {date}<br>")
                                    if date:
                                        date = re.search(r'20\d{2}', file)
                                        date = date.group()
                                    else:
                                        print(f"(YYYYMMDD/MMDDYYYY/DDMMYYYY/YYYYDDMM) Finding date... {date}<br>")
                                        date = re.search(r'\d{8}', file)
                                        if date:
                                            # if its a 8 digit number, grab the part that starts with 20
                                            # THIS WILL GO OUT OF DATE IN THE YEAR 2100
                                            date = re.search(r'20\d{2}', file)
                                            date = date.group()
                                        else:
                                            date = ""
        return date

    def sort_files(self):
        # get files in the destination folder
        # list the files only, not the directories
        destinationFiles = [f for f in os.listdir(self.destination) if os.path.isfile(os.path.join(self.destination, f))]
        print(f"Files in destination: {destinationFiles}<br>")

        for file in destinationFiles:
            if file:
                date = self.get_date(file)
                #print date
                print(f"File has a date?: {date}<br>")
                if not date:
                    print(f"File does not have a date: {file}<br>")
                    # create the folder path
                    folderPath = f'{self.destination}/NODATE'
                    # check if the folder exists
                    if not os.path.exists(folderPath):
                        print(f"Creating folder: {folderPath}<br>")
                        os.makedirs(folderPath)
                else:
                    # extract the year from the date
                    year = date.split('-')[0]
                    print(f"Year: {year}<br>")
                    # create the folder path
                    folderPath = f'{self.destination}/{year}'
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
print(f"<b>Files sorted: {sorter.moveCount}</b><br>")
