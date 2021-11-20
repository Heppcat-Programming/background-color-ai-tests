# Background Color Affect on AI
Tests to figure out which of 4 colors used in training is best for identifying on other colors

# Recreating the Experiment

## Positioning

Using the [Microsoft Studio Webcam](https://www.microsoft.com/en-us/d/lifecam-studio/91dt6wmfdlb3) Craphy Studio Softbox Lights, and a small stool positioned as followed

Left Light 6ft off the ground
Right Light 6ft 2in off the ground
Lights seperated by 45.5in pole to pole

Camera 29in off the ground

Left edge of webcam 5in from the left edge of the tile

Stool 11in off the ground

## Capturing Pictures

### Installing dependencies

The picture script requires you to have both python and the python module `Open CV` installed
To install opencv just run `pip install opencv-python` after installing python 3.10 from https://www.python.org/downloads/

### Runing the script

Following the positioning stated above capture your pictures using [This Script](https://github.com/Heppcat-Programming/background-color-ai-tests/blob/main/pictures.py) to run the script while in the same folder as it run `python pictures.py` it will take a picture every 30 seconds when you are ready press `p` to start and follow the instructions in the terminal.

## Labeling the images

First install the dependencies using `pip install pyqt5 lxml`

Go to the folder named `labelimg` and run `python labelImg.py` then using the buttons on the side open the folder with the first image. Then press w and make the selection. After doing that save the image and go on to the next one. To copy the selection from image to image press `Ctrl + V`, but you have to reselect the object for each background color.
