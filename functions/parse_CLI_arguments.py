# --- parse_CLI_arguments.py --- #
# Parse input arguments into variables and provide user with descriptions, error messages, and help displays.

# We use argparse to create the command line interface and parse arguments.
import argparse


# parseInputArgs: creates the CLI, parses input arguments, returns an argparse.Namespace object containing input
# variables.
def parseInputArgs():
    # Creating the parser, printing a description of the CLI.
    parser = argparse.ArgumentParser(description="ESP32-CAM_CLI: command-line interface for capturing and saving photos"
                                                 "/videos and launching streams from an ESP32 microcontroller with a"
                                                 "camera module.",
                                     # We specify RawTextHelpFormatter so we can put newlines in the helptext.
                                     formatter_class=argparse.RawTextHelpFormatter)

    # Defining positional arguments
    parser.add_argument("ip",
                        help="Specify the IP address of your ESP32-CAM (see README for how to find this)")
    parser.add_argument("camera_function",
                        help="Specify basic camera function (photo, video, or stream)",
                        choices=["photo", "video", "stream"])

    # Defining camera presets affecting raw image output
    parser.add_argument("-r", "--resolution",
                        help="Specify resolution (0 for lowest, 13 for highest):\n"
                             "  13 = UXGA (1600x1200)\n"
                             "  12 = SXGA (1280x1024)\n"
                             "  11 = HD    (1280x720)\n"
                             "  10 = XGA   (1024x768)\n"
                             "   9 = SVGA   (800x600)\n"
                             "   8 = VGA    (640x480)\n"
                             "   7 = HVGA   (480x320)\n"
                             "   6 = CIG    (400x296)\n"
                             "   5 = QVGA   (320x240)\n"
                             "   4 =        (240x240)\n"
                             "   3 = HQVGA  (240x176)\n"
                             "   2 = QCIF   (176x144)\n"
                             "   1 = QQVGA  (160x120)\n"
                             "   0 =          (96x96)\n",
                        choices=[str(x) for x in range(14)],
                        metavar="")
    parser.add_argument("-q", "--quality",
                        help="Specify image quality (1 for lowest quality, 100 for highest quality)",
                        # Lower quality makes the image more blocky but retains the same resolution
                        choices=[str(x) for x in range(101)],
                        metavar="")

    # Defining camera presets affecting camera operation
    parser.add_argument("-f", "--flash",
                        help="Set camera flash to on, auto, or off",
                        choices=["on", "auto", "off"])
    parser.add_argument("-e", "--exposure",
                        help="Manually set exposure (0 for shortest, 100 for longest). By default, exposure is "
                             "set automatically.",
                        choices=[str(x) for x in range(101)],
                        metavar="")

    # Defining camera presets affecting post-processing
    parser.add_argument("-b", "--brightness",
                        help="Manually set brightness (must be integer, -2 for lowest, 2 for highest)",
                        choices=[str(x) for x in range(-2, 3)])
    parser.add_argument("-c", "--contrast",
                        help="Manually set saturation (must be integer, -2 for lowest, 2 for highest)",
                        choices=[str(x) for x in range(-2, 3)])
    parser.add_argument("-s", "--saturation",
                        help="Manually set contrast (must be integer, -2 for lowest, 2 for highest)",
                        choices=[str(x) for x in range(-2, 3)])
    parser.add_argument("-hf", "--horizontal_flip",
                        help="Flip image horizontally",
                        action='store_true')

    # Defining output parameters
    parser.add_argument("-o", "--output_location",
                        help="(For photo/video) Specify output filename or filepath within the 'output' folder. By "
                             "default,files are saved under '/output/output_file'",
                        # 'output_file' is the default name of the file and can be changed in save_image.py and
                        # save_video.py.
                        # 'output' is the default output folder. Make sure this folder exists in the same directory
                        # as ESP32-CAM_CLI.py. The output folder can be changed within ESP32-CAM_CLI.py.
                        metavar="")
    parser.add_argument("-open", "--open_file",
                        help="(For photo/video) Open file after saving. Note that this function uses the system command"
                             " prompt to open files with the default application - check process_output_params.py if it"
                             " isn't working in your OS.",
                        action='store_true')
    parser.add_argument("-d", "--show_debug",
                        help="Show parsed arguments as output for debugging.",
                        action="store_true")

    # Parse arguments and return output
    args = parser.parse_args()
    return args
