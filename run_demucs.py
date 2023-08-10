import demucs.separate
import glob,os,shutil

PROGRAM_ROOT = "C:\work\python\demucs"

MUSIC_PATH = PROGRAM_ROOT + "\music"
OUTPUT_PATH = PROGRAM_ROOT + "\output"
SEPARETED_PATH = PROGRAM_ROOT + "\separated\htdemucs"

# Get folders under the MUSIC directory
music_dirs = os.listdir(MUSIC_PATH)

for dir in music_dirs:
    # Create an album folder in the output folder
    output_dir = OUTPUT_PATH + "\\" + dir
    os.makedirs(output_dir)

    # get music file location
    music_file = MUSIC_PATH + "\\" + dir + "\\*mp3"
    files = glob.glob(music_file)
    for file in files:
        print(file)
        demucs.separate.main(["--mp3", "--mp3-bitrate", "192000", file,"-d", "cuda"])
        
    # Move the folder under htdemucs to the output folder
    results = os.listdir(SEPARETED_PATH)
    for result in results:
        shutil.move(SEPARETED_PATH + "\\" + result, output_dir)