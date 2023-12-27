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
* To do this, I go to Tools -> Board -> Boards Manager. 

[image showing  Tools -> Board -> Boards Manager]

* Then, I search for 'esp32' and install the esp32 package by Expressif (specifically, I install version 2.0.14).

[image showing package install]

* After this, I go to Tools -> Board -> ESP32 Arduino and select the 'AI Thinker ESP32-CAM' board from the list.

[image showing selection]

* Now, I have installed and set up all the necessary software to upload code to the ESP32.

### Hardware setup

* To set up the hardware, I connect the pins on the ESP32 with the pins on the FTDI programmer as follows:

[image]

* After this, I make sure the FTDI programmer is set to 5V output (this is controlled by the jumper across the 3 upward pins).
* Once I have everything connected, I plug the FTDI programmer into my laptop via the Mini-USB port, verifying that the LED indicator light turns on.

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

* I connect the ESP32 to my computer and click the upload button.
* Once uploading is completed successfully, I need to disconnect the IO0 and GND ports on the ESP32 from each other to exit the flash mode.
* Then, I go to Tools -> Serial Monitor in the Arduino IDE and set the baud rate to 115200.
* I then press the reset button on the back of the ESP32. The serial monitor should log a short readout and then give the IP address of the ESP32.

[image showing serial monitor]

* This IP address is required to run the CLI program.

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
* For a full list of parameters and arguments, I can run the program with the `-h` tag to get a help message:
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
* All parameters except `--flash`, `--exposure`, `--horizontal_flip`, and `--show_debug` persist until the ESP32 is reset or powered off.

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

#### Example 1:
* Basic example: taking a picture with 800x600 resolution, max quality, adjusting brightness/contrast, saving as banana1.jpg
```
anton@antons-computer ESP32-CAM_CLI % python3 ESP32-CAM_CLI.py 10.0.0.18 photo -r 9 -q 100 -c 1 -s 1 -o banana1
```
> ```
>Selected function: photo
>Photo saved to output/banana1.jpg
> ```
>![banana1.jpg]

#### Example 2:
* Decreasing contrast and saturation, increasing brightness
```
anton@antons-computer ESP32-CAM_CLI % python3 ESP32-CAM_CLI.py 10.0.0.18 photo -r 9 -q 100 -c -2 -s -2 -b 1 -o banana2
```
>```
>Selected function: photo
>Photo saved to output/banana2.jpg
>```
>![banana2.jpg]

#### Example 3:
* Increasing resolution, resetting brightness, contrast and saturation
```
anton@antons-computer ESP32-CAM_CLI % python3 ESP32-CAM_CLI.py 10.0.0.18 photo -r 12 -q 100 -c 0 -s 0 -b 0 -o banana3
```
>```
>Selected function: photo
>Photo saved to output/banana3.jpg
>```
>![banana3.jpg]

#### Example 4:
* Setting exposure to max
* Notice that other parameters (quality, resolution etc.) persist from last time they were specified
```
anton@antons-computer ESP32-CAM_CLI % python3 ESP32-CAM_CLI.py 10.0.0.18 photo -e 100 -o banana4 
```
>```
>Selected function: photo
>Photo saved to output/banana4.jpg
>```
>![banana4.jpg]

#### Example 5:
* Setting quality to min, exposure to max
* Note that I can use either the short flag (as in `-e`) or the full flag (as in `--exposure`) to set parameters
```
anton@antons-computer ESP32-CAM_CLI % python3 ESP32-CAM_CLI.py 10.0.0.18 photo --exposure 100 -q 0 -o banana5 
```
>```
>Selected function: photo
>Photo saved to output/banana5.jpg
>```
>![banana5.jpg]

#### Example 6:
* Setting exposure to max, quality to max, increasing resolution, turning flash on
```
anton@antons-computer ESP32-CAM_CLI % python3 ESP32-CAM_CLI.py 10.0.0.18 photo --exposure 100 -q 100 -r12 -f on -o banana6 
```
>```
>Selected function: photo
>Photo saved to output/banana6.jpg
>```
>![banana6.jpg]

#### Example 7:
* Showing debug output (parsed parameters from user input)
* Observe that flash resets to flash off and exposure resets to auto while other parameters stay the same
```
anton@antons-computer ESP32-CAM_CLI % python3 ESP32-CAM_CLI.py 10.0.0.18 photo -d -o banana7      
```
>```
>Namespace(ip='10.0.0.18', camera_function='photo', resolution=None, quality=None, flash=None, exposure=None, brightness=None, >contrast=None, saturation=None, horizontal_flip=False, output_location='banana7', open_file=False, show_debug=True)
>
>Selected function: photo
>Photo saved to output/banana7.jpg
>```
>![banana7.jpg]

#### Example 8:
* Increasing resolution, flipping image horizontally, setting flash to auto, opening image
* Observe that the order of the flags does not matter
```
anton@antons-computer ESP32-CAM_CLI % python3 ESP32-CAM_CLI.py 10.0.0.18 photo -r 13 -hf -o banana8 -f auto -open 
```
>```
>Selected function: photo
>Photo saved to output/banana8.jpg
>```
>![banana8.jpg]

#### Example 9:
* Recording a video, lowering resolution, opening the video
```
anton@antons-computer ESP32-CAM_CLI % python3 ESP32-CAM_CLI.py 10.0.0.18 video -r 8 -o bananaVideo -open
```
>```
>Selected function: video
>Press S to stop recording.
```
S
```
>```
>Video saved to output/bananaVideo.avi
>```
><img src="https://github.com/antonshpak100/Markdown-test/blob/main/bananaVideo.gif" alt="bananaVideo.avi (converted to gif)" width="640">
>
>(bananaVideo.avi converted to gif)

#### Example 10:
* Launching live stream, setting resolution to SVGA, increasing saturation and contrast, flipping horizontally, showing debug output.
* Note that `-o` and `-open` are not necessary since the stream is not saved.
```
anton@antons-computer ESP32-CAM_CLI % python3 ESP32-CAM_CLI.py 10.0.0.18 stream -r 9 -s 2 -c 2 -hf -d -o stream -open
```
>```
>Namespace(ip='10.0.0.18', camera_function='stream', resolution='9', quality=None, flash=None, exposure=None, brightness=None, >contrast='2', saturation='2', horizontal_flip=True, output_location='stream', open_file=True, show_debug=True)
>
>Selected function: stream
>Stream will now open in a new window.
>
>![Example of stream window](link)
>Press S to end stream.
>```
```
S
```
>```
>Stream is not saved. Do not specify -o or -open arguments for stream.
>```

## Potential improvements
* Rewriting ESP32 web server code
  * Instead of using the existing ExampleWebServer Arduino code, I could write an image capture program and web server for the ESP32 from scratch
  * By writing my own code, I would be able to optimize it specifically for my program
* Adding SD card save feature
  * The ESP32 has the capability to write images directly to an SD card
  * This would reduce reliance on WiFi image transfer and processing on the host system
* Reworking video recording function
  * Currently, the video recording function records frames as they come from a live stream
  * Although this captures the largest possible amount of frames, the interval between frames is uneven
  * A typical video camera works by taking pictures at precise intervals
  * While it would come with additional challenges, I could try to apply this method to the ESP32
* Adding ability to interface with the ESP32 via bluetooth
  * The ESP32 is bluetooth-capable
  * This would allow the program to function without a WiFi connection
  * Although live streaming would not be possible, it may be possible to transfer images or even video via bluetooth
