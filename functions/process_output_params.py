# --- process_output_params.py --- #
# Tell the user where the file is saved, open photo/video file if specified.

# We use os.system to open the captured photo/video if specified.
from os import system


# processOutputParams: takes arguments, tells user where file is saved, opens file if specified.
def processOutputParams(outputFolder, args):

    # Photos are saved as JPGs, videos are saved as AVIs.
    if args.camera_function == "photo":
        extension = ".jpg"
    elif args.camera_function == "video":
        extension = ".avi"
    else:
        # If file location -o or opening argument -open are specified for a stream, tell the user this is not necessary.
        print("Stream is not saved. Do not specify -o or -open arguments for stream.")
        return

    # Take filename, or use default 'output_file' if not provided.
    if args.output_location:
        filename = args.output_location
    else:
        filename = "output_file"
    print(args.camera_function.capitalize()+" saved to "+outputFolder+"/"+filename+extension)

    # If -open is specified, open the file using the system default application. os.system depends on your operating
    # system - modify the code if it is not working on your OS.
    if args.open_file:
        # Mac/UNIX:
        system("open "+outputFolder+"/"+filename+extension)
        # Windows (not tested):
        # os.system(outputFolder+"/"+filename+extension)
