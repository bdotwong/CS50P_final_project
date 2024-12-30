# CS50P GIF creator
## Video Demo: [CS50P Final Project](https://www.youtube.com/watch?v=gIytOWUH4wE&ab_channel=BryanWong)
## Description:
This final project for CS50P builds on my previous CS50X final project, a photobooth: [CS50 Final Project](https://www.youtube.com/watch?v=Rf7_giI6qHE&ab_channel=BryanWong)

Some functionalities are similiar using a raspberry Pi and raspberry Pi HQ camera. However, the project is implented in Python (vs C++)

The goal of this project was to create a hardware-based application to capture images and create a stop motion GIF. With a background in mechanical engineering, I have been working to expand my knowledge of software development. This project allowed me to combine my interest in both hardware and software integration.

The program utilizes a few Python libraries, `argprase`, `tkinter`, and `Pillow`. `argparse` handles the flags from the user. `tkinter` creates the window for the user and allows the user to view the camera feed. `Pillow` handles the images processing and creates the GIF

- `argparse` -  Handles user input to customize the parameters of the GIF
- `tkinter` - Creates the GUI window to allow  a live camera feed allowing hte user to see whats being captured
- `Pillow` - Handles the image processing eh creates the final GIF using the paremeters given

## Function Overview
- `main` function - Is the main function which has defaults flags if none are chosen
- `parse_args` function - Parses the command line arguments allowing the user to customize parameters, like, the number of images, time interval, GIF resolution, and to display a camera feed. If no flags are choosen, a set of values for flags are chooses defaults
- `capture_image` function - Opens up the raspberry pi camera. Captures images and saves them to a directory. By default, the camera feed is displayed via tkinter so the user and view what images will be captured
- `create_gif` function - Creates the GIF based from the images taken
- `gif_resolution` functions - Generates the resolution of the GIF in three sizes: small, medium, XL.


## Goals
There were a few goals that were similiar and varied from the CS50X project
- Create a hardware base application
- Create a python application using tkinter
- Incorporate command-line arguments to customize functionality while providing default values for ease of use

## Improvements
- Detect different types of cameras and have a flag to choose. Ie: a USB camera
- Have and `add` and `finish` button so the user can add images and finish via GUI instead of using the CLI

## Conclusion
- This project provided valuable experience using flags via CLI
- It helped me understand the importance of careful planning, and programming. Providing default parameters if none are proivided creating checks if values are within range



## Bill of Materials (BOM)
1. [Raspberry Pi 3](https://www.adafruit.com/product/3775)
4. [Raspberry Pi High Quality HQ Camera](https://www.adafruit.com/product/4561) (or any other camera module)
5. [EYESPI Cable - 18 Pin 100mm long Flex PCB](https://www.adafruit.com/product/5239) (Should be included with HQ camera)
6. [16mm 10MP Telephoto Lens for Raspberry Pi HQ Camera](https://www.adafruit.com/product/4562)
12. [SmartiPi Touch 2 - Stand for Raspberry Pi 7" Touchscreen Display](https://www.adafruit.com/product/4377) (optional)

