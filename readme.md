# Scripts for automating the CUPS NAS
- **CONVERTER**: a script to import files from an input directory, convert them to a specified mp4 format and then copy them to a destination directory (intended to be on remote NAS)
- **IMPORTER**: a script to import files from a specified scan folder
- **SORTER**: a script to sort files on the destination folder once on the NAS by date
- **REPORTER**: runs a Flask server that controls the various functions of the above scripts

## Requirements
- FFMPEG installed on system: https://ffmpeg.org/download.html
- Python 3.12
  - Flask 3.0.3
  - dateutils 0.6.12
