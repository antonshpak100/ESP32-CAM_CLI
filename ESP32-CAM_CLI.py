# --- ESP32-CAM_CLI.py --- #
# Runs the command line interface and integrates all the functions together.

# Importing necessary functions (see each function for descriptions).
from functions.test_connection import testConnection
from functions.parse_CLI_arguments import parseInputArgs

from functions.save_image import saveImage
from functions.save_video import saveVideo
from functions.launch_stream import launchStream

from functions.process_camera_presets import processCameraPresets
from functions.camera_flash import startFlash, endFlash
from functions.process_output_params import processOutputParams

# The default output folder is 'output' (relative file path). If you change this, make sure the output folder already
# exists.
outputFolder = "output"

# Parsing CLI argument inputs into variables.
args = parseInputArgs()

# Printing blank lines and debug output (showing all parsed arguments) if -d is specified.
print()
if args.show_debug:
    print(args)
    print()

# Parsing URL from the given IP, testing whether we can connect to the ESP32's web server.
URL = "http://"+args.ip
connected = testConnection(URL)

# If connected, run the program.
# Perform the specified function (photo, video, or stream) with the given parameters.
# Run ESP32-CAM_CLI.py -h or see parse_CLI_arguments.py for descriptions of each parameter.
if connected:
    processCameraPresets(URL, args)  # apply camera parameters
    if args.camera_function == "photo":
        print("Selected function: photo")
        startFlash(URL, args.flash)  # turn the flash on if specified (or automatically)
        saveImage(URL, outputFolder, args.output_location)  # take picture and save it
        endFlash(URL)  # turn the flash off
    elif args.camera_function == "video":
        print("Selected function: video")
        print("Press S to stop recording.")
        startFlash(URL, args.flash)  # turn the flash on if specified (or automatically)
        saveVideo(URL, outputFolder, args.output_location)  # open video recording window, save video when S is pressed
        endFlash(URL)  # turn the flash off

    elif args.camera_function == "stream":
        print("Selected function: stream")
        print("Stream will now open in a new window.\n"
              "Press S to end stream.")
        startFlash(URL, args.flash)  # open stream window, end stream when S is pressed
        launchStream(URL)
        endFlash(URL)

    processOutputParams(outputFolder, args)  # tell the user where the file is saved, open photo/video file if specified
else:
    # If not connected, throw an error message.
    print("error: Connection failed. Check that your ESP32-CAM is set up correctly and that you have correctly "
          "specified its IP address. See README if you are still having problems.")
