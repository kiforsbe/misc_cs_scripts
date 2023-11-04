import subprocess
import os
import sys
import getopt
import glob

def getOpts(argv):
    # Set some output defaults
    inputPath = ""
    outputPath = "out"
    ffmpegPath = os.environ.get("FFMPEG")
    verbose=False

    # Check command line args, and if available, override the defaults
    try:
        opts, args = getopt.getopt(argv, "hi:o:f:v", ["input=", "output=", "ffmpeg="])
    except getopt.GetoptError:
        print(r"convert_ogg_to_mp3.py [-i <inputPath>] [-o <outputPath>] [-v]")
        sys.exit(2)

    # Walk through each option and arg
    for opt, arg in opts:
        if opt == '-h':
            printHelp()
            sys.exit()
        elif opt in ("-i", "--input"):
            inputPath = arg
        elif opt in ("-o", "--output"):
            outputPath = arg
        elif opt in ("-f", "--ffmpeg"):
            ffmpegPath = arg
        elif opt in ("-v"):
            verbose = True
    
    # Return final output, either defaults or overridden ones
    return inputPath, outputPath, ffmpegPath, verbose

def printHelp():
    print(r"convert_ogg_to_mp3.py [-i <inputPath>] [-o <outputPath>] [-f <ffmpegPath>] [-v]")
    print(r"")
    print(r"Batch convert all specified .ogg files to .mp3, keeping tags.")
    print(r"")
    print(r"Command-line options:")
    print(r"-i path")
    print(r"--input=path")
    print(r"    Path to files to operate on. Wildcards can be applied. [default=*.ogg].")
    print(r"")
    print(r"-o path")
    print(r"--output=path")
    print(r"    Path to output of files [default='out/'].")
    print(r"")
    print(r"--ffmepg=path")
    print(r"    Path to where on the system the ffmpeg binaries are located [default=%FFMPEG%]")
    print(r"")
    print(r"-v")
    print(r"    Enable verbose output.")

# ffmpeg -n -i $INFILE -c:a libmp3lame -q:a 1 -ar 44100 -map_metadata 0 -map_metadata 0:s:0 -id3v2_version 3 -vn $OUTFILE.mp3
def convert(inputFile: str, outputPath: str, ffmpeg: str):
    outputFile = os.path.join(outputPath, os.path.basename(inputFile).replace(".ogg", ".mp3"))
    ffmpeg = subprocess.check_output([ffmpeg,
                                      "-n",
                                      "-i", inputFile,
                                      "-loglevel", "error",
                                      "-c:a", "libmp3lame",
                                      "-q:a", "1",
                                      "-ar", "44100",
                                      "-map_metadata", "0",
                                      "-map_metadata", "0:s:0",
                                      "-id3v2_version", "3",
                                      "-vn", outputFile])

def main(argv):
    # Get options
    inputPath, outputPath, ffmpegPath, verbose = getOpts(argv)

    print(outputPath)

    # Normalize paths
    inputPath = os.path.normpath(inputPath)
    outputPath = os.path.normpath(outputPath)
    ffmpeg = os.path.join(ffmpegPath, "ffmpeg.exe")

    # If output path does not exist, create it
    if not os.path.exists(outputPath):
        os.mkdir(outputPath)

    # Get list of all files mathing inputPath (can use wild cards, e.g. "inputpath\*.mp4")
    files = glob.glob(inputPath)

    # Execute operation on each file
    for file in files:
        # Convert the file
        if(verbose): print(f"Converting: '{file}'... ", end="", flush=True)
        convert(file, outputPath, ffmpeg)
        if(verbose): print(f"Done")

if __name__ == "__main__":
    main(sys.argv[1:])
