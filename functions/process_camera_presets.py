# --- process_camera_presets.py --- #
# Takes parsed input parameters and changes the camera settings where specified.

# We use requests to send HTTP GETs to the ESP32's web server to change the camera parameters.
import requests


# setVariable: sends an HTTP GET at the specified URL, setting camera parameter 'var' to the given value.
def setParameter(URL, var, value):
    requests.get(URL + "/control?var="+var+"&val={}".format(value))


# processCameraPresets: takes parsed arguments and sets camera parameters accordingly.
# All parameters except exposure and horizontal flip persist until changed or the ESP32 is powered off/reset.
# Exposure and horizontal flip reset to default values if not specified.
def processCameraPresets(URL, args):

    # Setting resolution
    if args.resolution:
        setParameter(URL, "framesize", args.resolution)

    # Setting image quality
    if args.quality:
        # Min quality: 0 input corresponds to 63 on webserver
        # Max quality: 100 input corresponds to 4 on webserver
        quality = round(4+(59/100)*(100-int(args.quality)))
        setParameter(URL, "quality", quality)

    # Setting exposure
    # If specified, turn aec (auto exposure control) off and select a specific value for exposure.
    if args.exposure:
        setParameter(URL, "aec", 0)
        # Shortest exposure: 0 input corresponds to 0 on webserver
        # Longest exposure: 100 input corresponds to 1200 on webserver
        exposure = args.exposure*12
        setParameter(URL, "aec_value", exposure)
    else:  # default: turn aec on
        setParameter(URL, "aec", 1)

    # Setting brightness
    if args.brightness:
        setParameter(URL, "brightness", args.brightness)

    # Setting contrast
    if args.contrast:
        setParameter(URL, "contrast", args.contrast)

    # Setting saturation
    if args.saturation:
        setParameter(URL, "saturation", args.saturation)

    # Setting horizontal flip
    if args.horizontal_flip:
        setParameter(URL, "hmirror", 1)
    else:  # default: turn horizontal flip off (don't flip image)
        setParameter(URL, "hmirror", 0)
