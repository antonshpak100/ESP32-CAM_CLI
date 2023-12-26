# --- save_image --- #
# Saves the image from the capture URL on the webserver to the specified output folder and filename.

# We use requests to read image from the capture URL on the web server.
import requests


# saveImage: writes the image from the capture URL on the webserver to the specified output folder and filename.
def saveImage(URL, outputFolder, filename):

    # If no filename specified, use default 'output_file.jpg'
    if filename is None:
        filename = "output_file"
    img_data = requests.get(URL+"/capture").content
    with open(outputFolder+"/"+filename+".jpg", "wb") as handler:
        handler.write(img_data)
