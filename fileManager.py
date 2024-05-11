# requires commandline ffmpeg

import os, sys, subprocess

# class to manage file input, output and conversion
class FileManager:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def check_input_file(self):
        if not os.path.exists(self.input_file):
            print(f'Error: {self.input_file} does not exist')
            sys.exit(1)

    def check_output_file(self):
        if os.path.exists(self.output_file):
            print(f'Error: {self.output_file} already exists')
            sys.exit(1)

    def run_ffmpeg(self):
        ffmpeg_cmd = f'ffmpeg -y -i {self.input_file} -loglevel -8 -c:v libx264 -crf 23 -c:a aac -b:a 128k {self.output_file}'
        subprocess.run(ffmpeg_cmd, shell=True)


