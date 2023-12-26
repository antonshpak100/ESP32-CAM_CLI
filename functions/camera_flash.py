# --- camera_flash.py --- #
# Defines camera flash functions with auto flash feature

# We use requests to control the camera flash by sending HTTP GETs to the ESP32's web server and capture a sample image
# to test luminance for the auto flash feature.
# We use tempfile to create a temporary file that we can read average luminance from.
# We use cv2 to read the temporary file and find the average luminance.
import requests
import tempfile
import cv2


# changeFlash: turn flash on or off by sending an HTTP GET to the specified URL (of the ESP32's web server).
def changeFlash(URL, OnOff):
    if OnOff == "on":
        requests.get(URL+"/control?var=led_intensity&val={}".format(255))
        # 255 is the max brightness of the ESP32's LED. Lower this if you want it to be less bright.
    elif OnOff == "off":
        requests.get(URL+"/control?var=led_intensity&val={}".format(0))


# startFlash: turns on the flash if 'on' specified or if 'auto' specified and test image is sufficiently dark.
def startFlash(URL, flashParam):
    if flashParam == "on":
        changeFlash(URL, "on")

    # Defining auto flash feature
    elif flashParam == "auto":

        # Capturing a sample image and writing it into a temporary file.
        img_data = requests.get(URL + "/capture").content
        with tempfile.NamedTemporaryFile() as tmp:
            tmpName = tmp.name+".jpg"
            with open(tmpName, "wb") as handler:
                handler.write(img_data)

            # Reading the temporary image, converting it to grayscale and finding its average luminance.
            image = cv2.imread(tmpName)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            avgLuminance = cv2.mean(image)[0]

            # Min possible luminance (fully black image) is 0
            # Max luminance (fully white image) is 255
            # Change threshold to change the luminance threshold that activates auto flash.
            if avgLuminance <= 50:
                changeFlash(URL, "on")
    else:
        changeFlash(URL, "off")


# endFlash: turns off the flash by sending an HTTP GET to the specified URL.
def endFlash(URL):
    changeFlash(URL, "off")
