import json
import os
import pandas as pd
import sys
import getopt
import mutagen
from shutil import copyfile
from shutil import SameFileError

def getOpts(argv):
    # Set some output defaults
    inputPath = r"C:\Program Files (x86)\Steam\steamapps\common\Cities_Skylines\Files\Radio\Music"
    outputPath = "out"
    verbose=False

    # Check command line args, and if available, override the defaults
    try:
        opts, args = getopt.getopt(argv, "hi:o:v", ["input=", "output="])
    except getopt.GetoptError:
        print(r"convert_cs1-radio_to_cs2.py [-i <inputPath>] [-o <outputPath>] [-v]")
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
        elif opt in ("-v"):
            verbose = True
    
    # Return final output, either defaults or overridden ones
    return inputPath, outputPath, verbose

def printHelp():
    print(r"convert_music_cs1_to_cs2.py [-i <inputPath>] [-o <outputPath>]")
    print(r"")
    print(r"Automatically copies and tags CS1 radio for CS2, and creates radio network and channel settings files for each supported station.")
    print(r"")
    print(r"Command-line options:")
    print(r"-i path")
    print(r"--input=path")
    print(r"    Path to files to operate on. [default='C:\Program Files (x86)\Steam\steamapps\common\Cities_Skylines\Files\Radio\Music'].")
    print(r"")
    print(r"-o path")
    print(r"--output=path")
    print(r"    Path to output of files [default='out\'].")
    print(r"")
    print(r"-v")
    print(r"    Enable verbose output.")

def copyAndTagTracks(dfMapping: pd.DataFrame, inputPath: str, outputPath: str, verbose: bool):
    # Output some diagnostic info if verbose
    if(verbose): print(f"Converting files in: {inputPath}")
    if(verbose): print(f"Outputting files to: {outputPath}")

    # Execute operation on each file
    for index, row in dfMapping.iterrows():
        # Cache input filepath and output filepath
        inputFilename = row["Source Filename"]
        inputAlbum = row["Source Directory"]
        destFilename = f"{row['Album']} - {row['Artist']} - {row['Title']}.{row['Extension']}"
        inputAlbumFullPath = os.path.join(inputPath, inputAlbum)
        inputFileFullPath = os.path.join(inputAlbumFullPath, inputFilename)
        destFileFullPath = os.path.join(outputPath, destFilename)

        # Debut output
        if(verbose): print(f"Converting: '{os.path.join(inputAlbum, inputFilename)}' -> '{destFileFullPath}'... ", end="", flush=True)

        # Check for input file
        if os.path.exists(inputFileFullPath):
            try:
                # Copy file
                copyfile(inputFileFullPath, destFileFullPath)

                # Update tags
                track = mutagen.File(destFileFullPath)
                track["album"] = f"Cities Skylines: {row['Album']}"
                track["radio channel"] = row['Album']
                track["artist"] = row['Artist']
                track["title"] = row['Title']
                track["type"] = "Music"
                track["radio network"] = "Cities Skylines Classic"
                track.save()

                #Print success if verbose
                if(verbose): print(f"Done")
            
            # If source and destination are same
            except SameFileError:
                print("Source and destination represents the same file.")
            
            # If destination is a directory.
            except IsADirectoryError:
                print("Destination is a directory.")
            
            # If there is any permission issue
            except PermissionError:
                print("Permission denied.")

            # For other errors
            except:
                print("Error occurred while copying file.")
        else:
            # File not found, print diagnostic message
            if(verbose): print(f"WARN - File Not Found")

def serializeSettingsFile(object, type: str, fileFullPath: str):
    # Serializing json
    json_object = json.dumps(object, indent=4)
    
    # Writing to sample.json
    with open(fileFullPath, "w") as outfile:
        outfile.writelines(type)
        outfile.write(json_object)

def serlializeSettingsFiles(dfAlbumsData: pd.DataFrame, outputPath: str, verbose: bool):
    # Prepare and save network JSON settings file
    network = {
        "name": "Cities Skylines Classic",
        "nameId": "Cities Skylines Classic",
        "description": "Commercial radio stations",
        "descriptionId": "Cities Skylines Classic",
        "icon": "Media/Radio/Stations/TEST - Classical.svg",
        "uiPriority": 2,
        "allowAds": True
    }
    outputFile = os.path.join(outputPath, f"{network['nameId']}.coc")
    serializeSettingsFile(network, "Radio Network", outputFile)
    if(verbose): print(f"Serialized network settings file: {outputFile}")

    # Prepare and save radio channel JSON settings files
    for channelName in dfAlbumsData["Album"]:
        radioChannel = {
            "network": network["nameId"],
            "name": channelName,
            "description": channelName,
            "icon": "Media/Radio/Stations/TEST - Pop.svg",
            "uiPriority": -1,
            "programs": [
                {
                    "name": "Music non stop",
                    "description": "Dance all day, dance all night",
                    "icon": "Media/Radio/Stations/TEST - Pop.svg",
                    "type": "Playlist",
                    "startTime": "00:00",
                    "endTime": "00:00",
                    "loopProgram": True,
                    "segments": [
                        {
                            "type": "Playlist",
                            "tags": [
                                "type:Music",
                                f"radio channel:{channelName}"
                            ],
                            "clipsCap": 3
                        },
                        {
                            "type": "Commercial",
                            "tags": [
                                "type:Commercial"
                            ],
                            "clipsCap": 2
                        }
                    ]
                }
            ]
        }
        outputFile = os.path.join(outputPath, f"{radioChannel['name']}.coc")
        serializeSettingsFile(radioChannel, "Radio Channel", outputFile)
        if(verbose): print(f"Serialized radio channel settings file: {outputFile}")

def main(argv):
    # Get options
    inputPath, outputPath, verbose = getOpts(argv)

    print(outputPath)

    # Normalize paths
    inputPath = os.path.normpath(inputPath)
    outputPath = os.path.normpath(outputPath)

    # If input path does not exist, exit early
    if not os.path.exists(inputPath):
        print(f"Input path '{inputPath}' does not exist.")
        sys.exit(2)

    # If output path does not exist, create it
    if not os.path.exists(outputPath):
        os.mkdir(outputPath)

    # Read mapping table
    dfMapping = pd.read_csv("cs1_to_cs2_mapping.csv")

    # Copy and tag all the tracks according to the mappign table
    copyAndTagTracks(dfMapping, inputPath, outputPath, verbose)

    # Prepare a table of all albums with play times etc (at some point, for now just unique album names)
    dfAlbumData = dfMapping.drop_duplicates(subset = "Album")

    # Serialize settings files based on album names along with a main network for all Cities Skylines stations
    serlializeSettingsFiles(dfAlbumData, outputPath, verbose)

if __name__ == "__main__":
    main(sys.argv[1:])
