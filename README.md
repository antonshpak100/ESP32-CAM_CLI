# ESP32-CAM_CLI

Command-line interface for saving photos, videos, and launching live streams from an ESP32 microcontroller with camera module. 
Works by using Python scripts to make calls to the ExampleWebServer for the ESP32-CAM (available through the Arduino IDE).

The program has the following basic capabilities:
* Capturing photos, videos and saving them to a specified directory on a host system
* Opening photos, videos, and live streams for quick and easy visualization
* Changing camera presets and operation over WiFi
  * These include image resolution, image quality, flash, exposure, brightness, contrast, saturation, and horizontal flip
* Original features include an [auto flash feature](#auto-flash) and [framerate correction for video recording](#framerate-correction)

---

## Table of contents:
* [Setting up ESP32](#setting-up-esp32)
  * [My hardware](#my-hardware)
  * [Software installation and setup](#software-installation-and-setup)
  * [Hardware setup](#hardware-setup)
  * [Uploading code to the ESP32](#uploading-code-to-the-esp32)
    * [Troubleshooting upload](#troubleshooting-upload)
* [Running the program](#running-the-program)
  * [Basic operation](#basic-operation)
  * [Parameters and arguments](#parameters-and-arguments)
  * [Original features](#original-features)
     * [Auto flash](#auto-flash)
     * [Framerate correction](#framerate-correction)
* [Examples](#examples)
* [Potential improvements](#potential-improvements)

## Setting up ESP32

### My hardware
* For this project, I am using an ESP32-CAM microcontroller (ESP-32S board with an OV2640 camera module), an FTDI programmer with a TTL serial to Mini-USB adapter, and 5 jumper wires to connect the two.

[image of ESP32 CAM]
[image of FTDI programmer] 

### Software installation and setup
* Before I can set up the ESP32 hardware, I need to install and set up software to be able to upload code to my ESP32 microcontroller. To do this, I first install the [Arduino IDE](https://www.arduino.cc/en/software) (specifically, I am using version 1.8.19, but versions 2.x.x should work also). 

* Then, I need to link the correct JSON file for the ESP32 within the Arduino IDE.
* This can be done by going to Arduino -> Preferences on Mac (File -> Preferences on Windows) and then pasting the following link under "Additional Boards Manager URLs": 

https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json

[image showing Arduino -> Preferences]

[image showing Additional Boards Manager URLs]

* Once this is done, I still need to install the ESP32 board manager package for the Arduino IDE.
* To do this, I go to Tools -> Board -> Board Manager. 

[image showing  Tools -> Board -> Board Manager]

* Then, I search for 'esp32' and install the esp32 package by Expressif. I have version 2.0.14 installed.

[image showing package install]

* After this, I go to Tools -> Board -> ESP32 Arduino and select the 'AI Thinker ESP32-CAM' board from the list.

[image showing selection]

* Now, I have installed and set up all the necessary software to upload code to the ESP32.

### Hardware setup

* To set up the hardware, I connected the pins on the ESP32 with the pins on the FTDI programmer as follows:

[image]

* Make sure the FTDI programmer is set to 5V output (this is controlled by the jumper across the 3 upward pins).
* Once I had everything connected, I plugged the FTDI programmer into my laptop via the Mini-USB port and checked that the LED indicator light was on.

### Uploading code to the ESP32

* For this project, I am using the ExampleWebServer for the ESP32-CAM. This can be found by going to File -> Examples -> ESP32 -> Camera -> CameraWebServer.
* I've also linked the ExampleWebServer files in this repo [here](#insert.link.here).
* I need to modify the code slightly to make it work in my situation.
* First, I need to select the correct camera.
* Within the CameraWebServer.ino file, I comment out CAMERA_MODEL_ESP_EYE and uncomment CAMERA_MODEL_AI_THINKER:

```C++
// ===================
// Select camera model
// ===================
//#define CAMERA_MODEL_WROVER_KIT // Has PSRAM
//#define CAMERA_MODEL_ESP_EYE // Has PSRAM
//#define CAMERA_MODEL_ESP32S3_EYE // Has PSRAM
//#define CAMERA_MODEL_M5STACK_PSRAM // Has PSRAM
//#define CAMERA_MODEL_M5STACK_V2_PSRAM // M5Camera version B Has PSRAM
//#define CAMERA_MODEL_M5STACK_WIDE // Has PSRAM
//#define CAMERA_MODEL_M5STACK_ESP32CAM // No PSRAM
//#define CAMERA_MODEL_M5STACK_UNITCAM // No PSRAM
#define CAMERA_MODEL_AI_THINKER // Has PSRAM
//#define CAMERA_MODEL_TTGO_T_JOURNAL // No PSRAM
//#define CAMERA_MODEL_XIAO_ESP32S3 // Has PSRAM
// ** Espressif Internal Boards **
//#define CAMERA_MODEL_ESP32_CAM_BOARD
//#define CAMERA_MODEL_ESP32S2_CAM_BOARD
//#define CAMERA_MODEL_ESP32S3_CAM_LCD
//#define CAMERA_MODEL_DFRobot_FireBeetle2_ESP32S3 // Has PSRAM
//#define CAMERA_MODEL_DFRobot_Romeo_ESP32S3 // Has PSRAM
#include "camera_pins.h"
```

* Then, I need to add my WiFi network name (ssid) and password at the following lines:

```C++
// ===========================
// Enter your WiFi credentials
// ===========================

const char* ssid = "**********";
const char* password = "**********";
```
* Finally, the code is ready to upload.
* With the ESP32 plugged in, I select the correct port under Tools -> Ports

[image showing Tools -> Ports]

* I connect my ESP32 to my computer and click the upload button.
* Once uploading is completed successfully, I go to Tools -> Serial Monitor in the Arduino IDE and set the baud rate to 115200.
* I then press the reset button on the back of the ESP32. The serial monitor should log a short readout and then give the IP address of the ESP32.

[image showing serial monitor]

* This IP address is required to run the CLI program - note it down somewhere.

#### Troubleshooting upload
* If upload fails (as it did for me), try pressing the reset button while the Arduino IDE says `Connecting.....`, and then try uploading again.
* Try connecting the GND pin on the FTDI with the GND pin below the 5V pin on the ESP32, not the one next to UOT as shown above. This seemed to work better for me.

## Running the program

### Basic operation
* Now, I have everything to run the ESP32-CAM CLI program. I navigate to my project folder in my command prompt terminal:
```
anton@antons-computer ~ % cd .../.../ESP32-CAM_CLI
anton@antons-computer ESP32-CAM_CLI % 
```
* This project folder contains the following:
  * 'ESP32-CAM_CLI.py', the main Python script I will use to run the program.
  * 'functions', a folder containing supporting Python modules.
  * 'output', the default folder for image and video output from the ESP32-CAM.
  * 'requirements.txt', a list of required Python libraries
    * Run `pip install -r requirements.txt` before proceeding if you don't have these already.
    * As for Python version, I'm running Python 3.9 but any newer version of Python 3 should work.
* From the command prompt, I can run the program as follows:
```
anton@antons-computer ESP32-CAM_CLI % python3 ESP32-CAM_CLI.py [ip] [camera_function] [-parameters]
```
where `ip` is the IP address of the ESP32, `camera_function` is a basic camera operation (photo, video, or stream) and `-parameters` are parameters for the camera operation and output. These will be described in the next section.

### Parameters and arguments
* For a full list of parameters and arguments, we can run the program with the `-h` tag to get a help message:
```
anton@antons-computer ESP32-CAM_CLI % python3 ESP32-CAM_CLI.py -h
```
* This outputs the following list of arguments and descriptions:
```
usage: ESP32-CAM_CLI.py [-h] [-r] [-q] [-f {on,auto,off}] [-e] [-b {-2,-1,0,1,2}] [-c {-2,-1,0,1,2}] [-s {-2,-1,0,1,2}] [-hf] [-o] [-open] [-d] ip {photo,video,stream}

ESP32-CAM_CLI: command-line interface for capturing and saving photos/videos and launching streams from an ESP32 microcontroller with acamera module.

positional arguments:
  ip                    Specify the IP address of your ESP32-CAM (see README for how to find this)
  {photo,video,stream}  Specify basic camera function (photo, video, or stream)

optional arguments:
  -h, --help            show this help message and exit
  -r , --resolution     Specify resolution (0 for lowest, 13 for highest):
                          13 = UXGA (1600x1200)
                          12 = SXGA (1280x1024)
                          11 = HD    (1280x720)
                          10 = XGA   (1024x768)
                           9 = SVGA   (800x600)
                           8 = VGA    (640x480)
                           7 = HVGA   (480x320)
                           6 = CIG    (400x296)
                           5 = QVGA   (320x240)
                           4 =        (240x240)
                           3 = HQVGA  (240x176)
                           2 = QCIF   (176x144)
                           1 = QQVGA  (160x120)
                           0 =          (96x96)
  -q , --quality        Specify image quality (1 for lowest quality, 100 for highest quality)
  -f {on,auto,off}, --flash {on,auto,off}
                        Set camera flash to on, auto, or off
  -e , --exposure       Manually set exposure (0 for shortest, 100 for longest). By default, exposure is set automatically.
  -b {-2,-1,0,1,2}, --brightness {-2,-1,0,1,2}
                        Manually set brightness (must be integer, -2 for lowest, 2 for highest)
  -c {-2,-1,0,1,2}, --contrast {-2,-1,0,1,2}
                        Manually set saturation (must be integer, -2 for lowest, 2 for highest)
  -s {-2,-1,0,1,2}, --saturation {-2,-1,0,1,2}
                        Manually set contrast (must be integer, -2 for lowest, 2 for highest)
  -hf, --horizontal_flip
                        Flip image horizontally
  -o , --output_location 
                        (For photo/video) Specify output filename or filepath within the 'output' folder. By default,files are saved under '/output/output_file'
  -open, --open_file    (For photo/video) Open file after saving. Note that this function uses the system command prompt to open files with the default application - check process_output_params.py if it isn't working in your OS.
  -d, --show_debug      Show parsed arguments as output for debugging.
```
* All parameters except `--exposure` and `--horizontal_flip` persist until the ESP32 is reset or powered off.
* `--exposure` and `--horizontal_flip` reset to defaults every time the program is run.

### Original features
* Most features of the program (e.g. changing quality, resolution, contrast etc.) can be done in the ExampleWebServer GUI or can be done with existing programs. However, I haven't seen the following features in other code written to control the ESP32-CAM and so these are fresh implementations.
#### Auto flash
* By specifying `-f auto` when running the program, auto flash is enabled.
* This feature captures a test image, reads its average luminosity, and then enables the flash automatically if the image is too dark.
#### Framerate correction
* The program records video by capturing frames from a live stream of the ESP32's camera output.
* This captures as many frames as possible, however, the interval between frames is inconsistent and also dependent on image resolution and quality.
* Video files must be written with a specified framerate – this is not possible if the interval between frames is unknown.
* To correct this, the program writes a temporary video file with a placeholder framerate.
* The length of the recording is timed and the number of frames is counted to find the true average framerate.
* The program rewrites the output video file from the temporary file with this corrected framerate.

## Examples

## Potential improvements

