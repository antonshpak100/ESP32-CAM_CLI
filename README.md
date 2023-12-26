# ESP32-CAM_CLI

Command-line interface for saving photos, videos, and launching live streams from an ESP32 microcontroller with camera module. 
Works by using Python scripts to make calls to the ExampleWebServer for the ESP32-CAM (available through the Arduino IDE).

---

## Table of contents:
* [Setting up ESP32](#setting-up-esp32)
  * [My hardware](#my-hardware)
  * [Software installation and setup](#software-installation-and-setup)
  * [Hardware setup](#hardware-setup)
  * [Uploading code to the ESP32](#uploading-code-to-the-esp32)
* [Running the program](#running-the-program)
  * [Basic operation](#basic-operation)
  * [Parameters](#parameters)
  * [Original features](#original-features)
     * [Auto flash](#auto-flash)
     * [Framerate correction](#framerate-correction)
* [Examples](#examples)

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

* (Note: I actually connected the GND pin on the FTDI with the GND pin below the 5V pin, not the one shown above. For some reason, this seemed to work better for me.)
* Once I had everything connected, I plugged the FTDI programmer into my laptop via the Mini-USB port and checked that the LED indicator light was on.

### Uploading code to the ESP32

* For this project, I am using the ExampleWebServer for the ESP32-CAM. This can be found by going to File -> Examples -> ESP32 -> Camera -> CameraWebServer
* I need to modify the code slightly to make it work in my situation.

## Running the program

### Basic operation
### Parameters 
### Original features
#### Auto flash
#### Framerate correction

## Examples

